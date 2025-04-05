#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test Installation Script for PDF to Word Converter

This script verifies that all required dependencies are installed correctly
and provides instructions for testing the PDF to Word converter.
"""

import sys
import importlib
import subprocess
import os
from pathlib import Path

# Required packages
REQUIRED_PACKAGES = [
    "pdf2docx",
    "docx",
    "tqdm",
    "PIL",
    "pdfminer.high_level"
]

def check_dependencies():
    """Check if all required packages are installed"""
    missing_packages = []
    
    print("Checking required dependencies...")
    
    for package in REQUIRED_PACKAGES:
        try:
            # Try to import the package
            importlib.import_module(package)
            print(f"✓ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} is NOT installed")
    
    return missing_packages

def check_pdf_to_word_script():
    """Check if the pdf_to_word.py script exists and is executable"""
    script_path = Path("pdf_to_word.py")
    
    if not script_path.exists():
        print(f"✗ {script_path} not found in the current directory")
        return False
    
    # Try to run the script with --help option
    try:
        result = subprocess.run(
            [sys.executable, str(script_path), "--help"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 and "usage:" in result.stdout.lower():
            print(f"✓ {script_path} is working correctly")
            return True
        else:
            print(f"✗ {script_path} exists but may have issues")
            print(f"  Error: {result.stderr}")
            return False
    
    except subprocess.TimeoutExpired:
        print(f"✗ {script_path} execution timed out")
        return False
    except Exception as e:
        print(f"✗ Error testing {script_path}: {str(e)}")
        return False

def create_test_pdf():
    """Create a simple test PDF file using reportlab if available"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        test_pdf_path = "test_document.pdf"
        
        print(f"Creating a test PDF file: {test_pdf_path}")
        
        # Create a simple PDF with text, table-like structure, and basic formatting
        c = canvas.Canvas(test_pdf_path, pagesize=letter)
        
        # Add a title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "PDF to Word Converter Test Document")
        
        # Add some regular text
        c.setFont("Helvetica", 12)
        c.drawString(100, 720, "This is a simple test document to verify the PDF to Word conversion.")
        c.drawString(100, 700, "It contains text, a simple table, and basic formatting.")
        
        # Add a simple table-like structure
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 650, "Product")
        c.drawString(250, 650, "Quantity")
        c.drawString(400, 650, "Price")
        
        # Draw table lines
        c.line(95, 645, 500, 645)
        c.line(95, 670, 500, 670)
        
        # Table data
        c.setFont("Helvetica", 12)
        data = [
            ("Widget A", "10", "$5.99"),
            ("Widget B", "5", "$10.50"),
            ("Widget C", "20", "$3.75")
        ]
        
        y_position = 620
        for row in data:
            c.drawString(100, y_position, row[0])
            c.drawString(250, y_position, row[1])
            c.drawString(400, y_position, row[2])
            y_position -= 20
        
        # Add a second page with an image if PIL is available
        c.showPage()
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 750, "Page 2 - More Test Content")
        
        try:
            from PIL import Image
            import numpy as np
            
            # Create a simple image using numpy and PIL
            img_path = "test_image.png"
            array = np.zeros([100, 100, 3], dtype=np.uint8)
            # Create a red square
            array[20:80, 20:80] = [255, 0, 0]
            img = Image.fromarray(array)
            img.save(img_path)
            
            # Add the image to the PDF
            c.drawImage(img_path, 100, 600, width=200, height=100)
            c.drawString(100, 580, "This page includes a test image.")
            
            # Clean up the temporary image file
            os.remove(img_path)
            
        except (ImportError, Exception) as e:
            c.drawString(100, 600, "Image creation skipped - PIL or numpy not available.")
        
        # Save the PDF
        c.save()
        
        print(f"✓ Test PDF created successfully: {test_pdf_path}")
        return test_pdf_path
    
    except ImportError:
        print("✗ reportlab package is not installed, skipping test PDF creation")
        print("  To create test PDFs, install reportlab: pip install reportlab")
        return None
    except Exception as e:
        print(f"✗ Error creating test PDF: {str(e)}")
        return None

def main():
    """Main function"""
    print("=" * 60)
    print("PDF to Word Converter - Installation Test")
    print("=" * 60)
    
    # Check dependencies
    missing_packages = check_dependencies()
    
    if missing_packages:
        print("\n❌ Some required packages are missing!")
        print("Please install them using:")
        print(f"pip install {' '.join(missing_packages)}")
        print("Or install all requirements with:")
        print("pip install -r requirements.txt")
        return 1
    
    print("\n✅ All required packages are installed!")
    
    # Check if the main script exists and is executable
    print("\nChecking pdf_to_word.py script...")
    script_ok = check_pdf_to_word_script()
    
    if not script_ok:
        print("\n❌ There are issues with the pdf_to_word.py script")
        print("Please make sure the script exists and is executable")
        return 1
    
    # Try to create a test PDF
    print("\nTrying to create a test PDF file...")
    test_pdf = create_test_pdf()
    
    # Provide instructions for testing
    print("\n" + "=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    
    if test_pdf:
        print(f"1. A test PDF file has been created: {test_pdf}")
        print("2. Try converting it with the following command:")
        print(f"   python pdf_to_word.py -i {test_pdf} -o test_output.docx")
        print("3. Check the resulting Word document to verify conversion quality")
    else:
        print("1. Create or obtain a PDF file for testing")
        print("2. Convert it using the command:")
        print("   python pdf_to_word.py -i your_file.pdf -o output.docx")
    
    print("\nAdditional test commands:")
    print("- Test with high quality settings:")
    print("  python pdf_to_word.py -i your_file.pdf -o output.docx --image-quality high --table-mode accurate")
    print("- Generate a conversion report:")
    print("  python pdf_to_word.py -i your_file.pdf -o output.docx --generate-report")
    
    print("\n✅ Installation test completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
