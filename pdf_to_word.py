#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PDF to Word Converter

A comprehensive tool to convert PDF files to Word documents with advanced options
for handling complex PDFs containing tables, images, and formatting.

Usage:
    Single file: python pdf_to_word.py -i input.pdf -o output.docx
    Batch mode:  python pdf_to_word.py -d /path/to/pdfs -o /output/dir
"""

import os
import sys
import argparse
import logging
import time
import shutil
from datetime import datetime
from pathlib import Path
import traceback
import json

# Check if required packages are installed, if not provide instructions
try:
    from pdf2docx import Converter
    from docx import Document
    from tqdm import tqdm
except ImportError as e:
    missing_package = str(e).split("'")[1]
    print(f"Error: Required package '{missing_package}' is not installed.")
    print("\nPlease install the required packages using:")
    print("pip install pdf2docx python-docx tqdm pillow")
    sys.exit(1)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('pdf2word')

# Constants
VERSION = "1.0.0"
QUALITY_LEVELS = ["high", "medium", "low"]
TABLE_MODES = ["standard", "accurate", "fast"]
LAYOUT_FIDELITY = ["high", "medium", "low"]


class ConversionReport:
    """Class to generate and manage conversion reports"""
    
    def __init__(self, output_path=None):
        self.issues = []
        self.warnings = []
        self.stats = {
            "pages_processed": 0,
            "tables_detected": 0,
            "images_extracted": 0,
            "conversion_time": 0,
            "fallback_used": False
        }
        self.output_path = output_path
    
    def add_issue(self, page_num, element_type, description):
        """Add an issue to the report"""
        self.issues.append({
            "page": page_num,
            "element_type": element_type,
            "description": description
        })
    
    def add_warning(self, message):
        """Add a warning to the report"""
        self.warnings.append(message)
    
    def update_stats(self, key, value):
        """Update statistics"""
        if key in self.stats:
            if isinstance(self.stats[key], int) and isinstance(value, int):
                self.stats[key] += value
            else:
                self.stats[key] = value
    
    def generate_report(self):
        """Generate a text report"""
        report = []
        report.append("=" * 60)
        report.append("PDF TO WORD CONVERSION REPORT")
        report.append("=" * 60)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        report.append("\nSTATISTICS:")
        report.append(f"- Pages processed: {self.stats['pages_processed']}")
        report.append(f"- Tables detected: {self.stats['tables_detected']}")
        report.append(f"- Images extracted: {self.stats['images_extracted']}")
        report.append(f"- Conversion time: {self.stats['conversion_time']:.2f} seconds")
        report.append(f"- Fallback methods used: {'Yes' if self.stats['fallback_used'] else 'No'}")
        
        if self.warnings:
            report.append("\nWARNINGS:")
            for i, warning in enumerate(self.warnings, 1):
                report.append(f"{i}. {warning}")
        
        if self.issues:
            report.append("\nPOTENTIAL ISSUES:")
            for i, issue in enumerate(self.issues, 1):
                report.append(f"{i}. Page {issue['page']}, {issue['element_type']}: {issue['description']}")
        
        if not self.issues and not self.warnings:
            report.append("\nNo issues or warnings detected during conversion.")
        
        report.append("\nRECOMMENDATIONS:")
        if self.issues:
            report.append("- Review the converted document for accuracy")
            report.append("- Consider using higher quality settings for better results")
            if any(issue['element_type'] == 'table' for issue in self.issues):
                report.append("- Tables with complex formatting may need manual adjustment")
        else:
            report.append("- The conversion appears successful with no detected issues")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)
    
    def save_report(self, filename=None):
        """Save the report to a file"""
        if not filename and not self.output_path:
            return False
        
        if not filename:
            base_path = Path(self.output_path)
            filename = base_path.parent / f"{base_path.stem}_report.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.generate_report())
            logger.info(f"Conversion report saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save report: {str(e)}")
            return False
    
    def save_json_report(self, filename=None):
        """Save the report as JSON"""
        if not filename and not self.output_path:
            return False
        
        if not filename:
            base_path = Path(self.output_path)
            filename = base_path.parent / f"{base_path.stem}_report.json"
        
        try:
            report_data = {
                "timestamp": datetime.now().isoformat(),
                "statistics": self.stats,
                "warnings": self.warnings,
                "issues": self.issues
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2)
            
            logger.info(f"JSON report saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save JSON report: {str(e)}")
            return False


class PDFConverter:
    """Main PDF to Word converter class with enhanced features"""
    
    def __init__(self, options=None):
        self.options = options or {}
        self.report = ConversionReport()
    
    def _get_conversion_params(self):
        """Get conversion parameters based on quality settings"""
        params = {}
        
        # Image quality settings
        image_quality = self.options.get('image_quality', 'medium').lower()
        if image_quality == 'high':
            params['zoom'] = 2.0
        elif image_quality == 'medium':
            params['zoom'] = 1.5
        else:  # low
            params['zoom'] = 1.0
        
        # Table mode settings
        table_mode = self.options.get('table_mode', 'standard').lower()
        if table_mode == 'accurate':
            params['debug'] = True
            params['line_overlap_threshold'] = 0.7
        elif table_mode == 'fast':
            params['detect_table'] = False
        
        # Layout fidelity settings
        layout_fidelity = self.options.get('layout_fidelity', 'medium').lower()
        if layout_fidelity == 'high':
            params['multi_processing'] = False  # More accurate but slower
        elif layout_fidelity == 'low':
            params['ignore_page_error'] = True
            params['multi_processing'] = True
        
        # Page range
        if self.options.get('page_range'):
            params['start'] = self.options.get('page_start', 0)
            params['end'] = self.options.get('page_end')
        
        return params
    
    def convert_file(self, pdf_path, docx_path):
        """Convert a single PDF file to Word with enhanced options"""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(docx_path)), exist_ok=True)
        
        # Set up the report
        self.report = ConversionReport(docx_path)
        
        # Get conversion parameters
        params = self._get_conversion_params()
        
        start_time = time.time()
        success = False
        
        try:
            # Primary conversion
            logger.info(f"Converting {pdf_path} to {docx_path}")
            cv = Converter(pdf_path)
            
            # Parse page range if specified
            page_ranges = []
            if self.options.get('page_range'):
                for part in self.options['page_range'].split(','):
                    if '-' in part:
                        start, end = map(int, part.split('-'))
                        page_ranges.extend(range(start-1, end))  # Convert to 0-based indexing
                    else:
                        page_ranges.append(int(part)-1)  # Convert to 0-based indexing
                
                # Update params with page ranges
                params['pages'] = page_ranges
            
            # Perform the conversion
            cv.convert(docx_path, **params)
            cv.close()
            
            # Update statistics
            self.report.update_stats("pages_processed", cv.pages_num)
            success = True
            
        except Exception as e:
            logger.error(f"Primary conversion failed: {str(e)}")
            self.report.add_warning(f"Primary conversion failed: {str(e)}")
            
            # Try fallback if enabled
            if self.options.get('enable_fallback', False):
                logger.info("Attempting fallback conversion...")
                self.report.update_stats("fallback_used", True)
                
                try:
                    # Simplified fallback conversion
                    cv = Converter(pdf_path)
                    fallback_params = {
                        'detect_table': False,
                        'ignore_page_error': True,
                        'multi_processing': False
                    }
                    cv.convert(docx_path, **fallback_params)
                    cv.close()
                    
                    self.report.add_warning("Used fallback conversion with simplified settings")
                    success = True
                    
                except Exception as fallback_e:
                    logger.error(f"Fallback conversion also failed: {str(fallback_e)}")
                    self.report.add_warning(f"Fallback conversion also failed: {str(fallback_e)}")
                    
                    # Last resort: text-only extraction if that option is enabled
                    if self.options.get('text_only_fallback', False):
                        try:
                            self._text_only_conversion(pdf_path, docx_path)
                            self.report.add_warning("Used text-only fallback conversion")
                            success = True
                        except Exception as text_e:
                            logger.error(f"Text-only fallback failed: {str(text_e)}")
                            self.report.add_warning(f"Text-only fallback failed: {str(text_e)}")
        
        # Calculate conversion time
        conversion_time = time.time() - start_time
        self.report.update_stats("conversion_time", conversion_time)
        
        # Generate reports if requested
        if self.options.get('generate_report', False):
            self.report.save_report()
            
        if self.options.get('generate_json_report', False):
            self.report.save_json_report()
        
        return success, self.report
    
    def _text_only_conversion(self, pdf_path, docx_path):
        """Last resort text-only conversion"""
        from pdfminer.high_level import extract_text
        
        # Extract text from PDF
        text = extract_text(pdf_path)
        
        # Create a new Word document
        doc = Document()
        doc.add_paragraph(text)
        doc.save(docx_path)
    
    def batch_convert(self, pdf_dir, output_dir, recursive=False):
        """Convert all PDF files in a directory"""
        if not os.path.exists(pdf_dir):
            raise FileNotFoundError(f"PDF directory not found: {pdf_dir}")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Find all PDF files
        pdf_files = []
        if recursive:
            for root, _, files in os.walk(pdf_dir):
                for file in files:
                    if file.lower().endswith('.pdf'):
                        pdf_files.append(os.path.join(root, file))
        else:
            pdf_files = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) 
                        if f.lower().endswith('.pdf') and os.path.isfile(os.path.join(pdf_dir, f))]
        
        if not pdf_files:
            logger.warning(f"No PDF files found in {pdf_dir}")
            return False
        
        # Process each PDF file
        success_count = 0
        total_files = len(pdf_files)
        
        logger.info(f"Found {total_files} PDF files to convert")
        
        for pdf_file in tqdm(pdf_files, desc="Converting PDFs", unit="file"):
            # Create relative path structure in output directory if recursive
            if recursive:
                rel_path = os.path.relpath(os.path.dirname(pdf_file), pdf_dir)
                target_dir = os.path.join(output_dir, rel_path)
                os.makedirs(target_dir, exist_ok=True)
            else:
                target_dir = output_dir
            
            # Generate output filename
            filename = os.path.basename(pdf_file)
            docx_filename = os.path.splitext(filename)[0] + '.docx'
            docx_path = os.path.join(target_dir, docx_filename)
            
            try:
                success, _ = self.convert_file(pdf_file, docx_path)
                if success:
                    success_count += 1
                    logger.info(f"Successfully converted: {pdf_file} -> {docx_path}")
                else:
                    logger.error(f"Failed to convert: {pdf_file}")
            except Exception as e:
                logger.error(f"Error converting {pdf_file}: {str(e)}")
                if self.options.get('verbose', False):
                    traceback.print_exc()
        
        logger.info(f"Batch conversion completed. {success_count}/{total_files} files converted successfully.")
        return success_count > 0


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Word documents with enhanced options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert a single file
  python pdf_to_word.py -i input.pdf -o output.docx
  
  # Batch convert all PDFs in a directory
  python pdf_to_word.py -d /path/to/pdfs -o /output/directory
  
  # Convert with high quality settings
  python pdf_to_word.py -i input.pdf -o output.docx --image-quality high --table-mode accurate
  
  # Generate a conversion report
  python pdf_to_word.py -i input.pdf -o output.docx --generate-report
  
  # Use fallback mechanisms for problematic PDFs
  python pdf_to_word.py -i input.pdf -o output.docx --enable-fallback --text-only-fallback
"""
    )
    
    # Input/Output options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-i', '--input', help='Input PDF file')
    input_group.add_argument('-d', '--directory', help='Directory containing PDF files to convert')
    
    parser.add_argument('-o', '--output', required=True, 
                        help='Output DOCX file (for single file) or directory (for batch conversion)')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Recursively process subdirectories (batch mode only)')
    
    # Quality and conversion settings
    parser.add_argument('--image-quality', choices=QUALITY_LEVELS, default='medium',
                        help='Image quality level (default: medium)')
    parser.add_argument('--table-mode', choices=TABLE_MODES, default='standard',
                        help='Table detection and conversion mode (default: standard)')
    parser.add_argument('--layout-fidelity', choices=LAYOUT_FIDELITY, default='medium',
                        help='Layout preservation level (default: medium)')
    parser.add_argument('--page-range', 
                        help='Page range to convert, e.g., "1-5,8,11-13" (single file only)')
    
    # Fallback options
    parser.add_argument('--enable-fallback', action='store_true',
                        help='Enable fallback conversion methods for problematic files')
    parser.add_argument('--text-only-fallback', action='store_true',
                        help='Enable text-only extraction as last resort fallback')
    
    # Reporting options
    parser.add_argument('--generate-report', action='store_true',
                        help='Generate a conversion report')
    parser.add_argument('--generate-json-report', action='store_true',
                        help='Generate a JSON conversion report')
    
    # Other options
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    parser.add_argument('--version', action='version', version=f'PDF to Word Converter v{VERSION}')
    
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    
    # Configure logging based on verbosity
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled")
    
    # Prepare conversion options
    options = {
        'image_quality': args.image_quality,
        'table_mode': args.table_mode,
        'layout_fidelity': args.layout_fidelity,
        'enable_fallback': args.enable_fallback,
        'text_only_fallback': args.text_only_fallback,
        'generate_report': args.generate_report,
        'generate_json_report': args.generate_json_report,
        'verbose': args.verbose
    }
    
    # Add page range if specified
    if args.page_range:
        options['page_range'] = args.page_range
    
    # Create converter instance
    converter = PDFConverter(options)
    
    try:
        if args.input:  # Single file conversion
            logger.info(f"Starting conversion of {args.input} to {args.output}")
            success, report = converter.convert_file(args.input, args.output)
            
            if success:
                print(f"\nSuccessfully converted {args.input} to {args.output}")
                if args.generate_report:
                    print(f"Conversion report saved alongside the output file")
            else:
                print(f"\nFailed to convert {args.input}. Check the logs for details.")
                return 1
                
        else:  # Batch conversion
            logger.info(f"Starting batch conversion from {args.directory} to {args.output}")
            success = converter.batch_convert(args.directory, args.output, args.recursive)
            
            if success:
                print(f"\nBatch conversion completed. Results saved to {args.output}")
            else:
                print(f"\nBatch conversion failed. Check the logs for details.")
                return 1
    
    except Exception as e:
        logger.error(f"Conversion error: {str(e)}")
        if args.verbose:
            traceback.print_exc()
        print(f"\nError: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
