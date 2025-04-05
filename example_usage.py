#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example Usage of PDF to Word Converter

This script demonstrates how to use the PDFConverter class programmatically
in your own Python scripts, rather than using the command-line interface.
"""

import os
import sys
from pdf_to_word import PDFConverter

def single_file_example():
    """Example of converting a single PDF file"""
    print("\n=== Single File Conversion Example ===")
    
    # Define input and output paths
    pdf_path = "example.pdf"  # Replace with your PDF file path
    docx_path = "example.docx"  # Replace with your desired output path
    
    # Check if the input file exists
    if not os.path.exists(pdf_path):
        print(f"Error: Input file '{pdf_path}' not found.")
        print("Please update the script with a valid PDF file path.")
        return False
    
    # Define conversion options
    options = {
        'image_quality': 'high',
        'table_mode': 'accurate',
        'layout_fidelity': 'high',
        'enable_fallback': True,
        'text_only_fallback': True,
        'generate_report': True,
        'verbose': True
    }
    
    # Create converter instance
    converter = PDFConverter(options)
    
    try:
        # Perform conversion
        print(f"Converting {pdf_path} to {docx_path}...")
        success, report = converter.convert_file(pdf_path, docx_path)
        
        if success:
            print(f"Conversion successful! Output saved to {docx_path}")
            
            # Print some statistics from the report
            print("\nConversion Statistics:")
            print(f"- Pages processed: {report.stats['pages_processed']}")
            print(f"- Conversion time: {report.stats['conversion_time']:.2f} seconds")
            print(f"- Fallback used: {'Yes' if report.stats['fallback_used'] else 'No'}")
            
            if report.warnings:
                print("\nWarnings:")
                for warning in report.warnings:
                    print(f"- {warning}")
            
            return True
        else:
            print("Conversion failed.")
            return False
            
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False


def batch_conversion_example():
    """Example of batch converting multiple PDF files"""
    print("\n=== Batch Conversion Example ===")
    
    # Define input and output directories
    pdf_dir = "pdf_files"  # Replace with your PDF directory
    output_dir = "converted_files"  # Replace with your desired output directory
    
    # Check if the input directory exists
    if not os.path.exists(pdf_dir):
        print(f"Error: Input directory '{pdf_dir}' not found.")
        print("Please update the script with a valid directory path.")
        return False
    
    # Define conversion options
    options = {
        'image_quality': 'medium',
        'table_mode': 'standard',
        'layout_fidelity': 'medium',
        'enable_fallback': True,
        'verbose': True
    }
    
    # Create converter instance
    converter = PDFConverter(options)
    
    try:
        # Perform batch conversion
        print(f"Converting all PDFs in {pdf_dir} to {output_dir}...")
        success = converter.batch_convert(pdf_dir, output_dir, recursive=True)
        
        if success:
            print(f"Batch conversion successful! Results saved to {output_dir}")
            return True
        else:
            print("Batch conversion failed.")
            return False
            
    except Exception as e:
        print(f"Error during batch conversion: {str(e)}")
        return False


def custom_page_range_example():
    """Example of converting specific pages from a PDF"""
    print("\n=== Custom Page Range Example ===")
    
    # Define input and output paths
    pdf_path = "example.pdf"  # Replace with your PDF file path
    docx_path = "example_pages_1_3_5.docx"  # Replace with your desired output path
    
    # Check if the input file exists
    if not os.path.exists(pdf_path):
        print(f"Error: Input file '{pdf_path}' not found.")
        print("Please update the script with a valid PDF file path.")
        return False
    
    # Define conversion options with page range
    options = {
        'image_quality': 'high',
        'page_range': '1,3,5',  # Only convert pages 1, 3, and 5
        'enable_fallback': True
    }
    
    # Create converter instance
    converter = PDFConverter(options)
    
    try:
        # Perform conversion
        print(f"Converting pages 1, 3, 5 from {pdf_path} to {docx_path}...")
        success, _ = converter.convert_file(pdf_path, docx_path)
        
        if success:
            print(f"Conversion successful! Output saved to {docx_path}")
            return True
        else:
            print("Conversion failed.")
            return False
            
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False


if __name__ == "__main__":
    print("PDF to Word Converter - Example Usage")
    print("=====================================")
    print("This script demonstrates how to use the PDFConverter class programmatically.")
    print("Before running this example, make sure you have valid PDF files at the specified paths.")
    print("You may need to modify the file paths in this script to match your environment.")
    
    # Run examples
    single_file_example()
    batch_conversion_example()
    custom_page_range_example()
    
    print("\nExamples completed.")
