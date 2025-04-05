# PDF to Word Converter

A comprehensive Python tool to convert PDF files to Word documents with advanced options for handling complex PDFs containing tables, images, and formatting.

## Features

- **Single file and batch conversion** - Convert individual PDFs or entire directories
- **Advanced formatting preservation** - Maintains tables, images, and layout
- **Quality control options** - Adjust settings for image quality, table detection, and layout fidelity
- **Fallback mechanisms** - Multiple conversion methods for problematic PDFs
- **Detailed reporting** - Generate reports on conversion process and potential issues
- **Command-line interface** - Easy to use from terminal or integrate into scripts

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - pdf2docx
  - python-docx
  - tqdm
  - pillow
  - pdfminer.six (for text-only fallback)

## Installation

1. Clone or download this repository
2. Install the required packages:

```bash
pip install pdf2docx python-docx tqdm pillow pdfminer.six
```

## Usage

### Basic Usage

**Convert a single PDF file:**
```bash
python pdf_to_word.py -i input.pdf -o output.docx
```

**Batch convert all PDFs in a directory:**
```bash
python pdf_to_word.py -d /path/to/pdfs -o /output/directory
```

**Recursively process subdirectories:**
```bash
python pdf_to_word.py -d /path/to/pdfs -o /output/directory -r
```

### Advanced Options

**Adjust quality settings:**
```bash
python pdf_to_word.py -i input.pdf -o output.docx --image-quality high --table-mode accurate --layout-fidelity high
```

**Convert specific page ranges:**
```bash
python pdf_to_word.py -i input.pdf -o output.docx --page-range "1-5,8,11-13"
```

**Enable fallback mechanisms for problematic PDFs:**
```bash
python pdf_to_word.py -i input.pdf -o output.docx --enable-fallback --text-only-fallback
```

**Generate conversion reports:**
```bash
python pdf_to_word.py -i input.pdf -o output.docx --generate-report --generate-json-report
```

**Enable verbose output for debugging:**
```bash
python pdf_to_word.py -i input.pdf -o output.docx -v
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `-i, --input` | Input PDF file |
| `-d, --directory` | Directory containing PDF files to convert |
| `-o, --output` | Output DOCX file (for single file) or directory (for batch conversion) |
| `-r, --recursive` | Recursively process subdirectories (batch mode only) |
| `--image-quality` | Image quality level: high, medium, low (default: medium) |
| `--table-mode` | Table detection mode: standard, accurate, fast (default: standard) |
| `--layout-fidelity` | Layout preservation level: high, medium, low (default: medium) |
| `--page-range` | Page range to convert, e.g., "1-5,8,11-13" (single file only) |
| `--enable-fallback` | Enable fallback conversion methods for problematic files |
| `--text-only-fallback` | Enable text-only extraction as last resort fallback |
| `--generate-report` | Generate a conversion report |
| `--generate-json-report` | Generate a JSON conversion report |
| `-v, --verbose` | Enable verbose output |
| `--version` | Show version information and exit |
| `-h, --help` | Show help message and exit |

## Understanding Quality Settings

### Image Quality
- **high**: Maximum image resolution preservation (slower)
- **medium**: Balanced quality and performance
- **low**: Faster conversion with reduced image quality

### Table Mode
- **accurate**: Enhanced table detection and structure preservation (slower)
- **standard**: Balanced table detection
- **fast**: Minimal table detection (faster)

### Layout Fidelity
- **high**: Maximum layout preservation (slower)
- **medium**: Balanced layout preservation
- **low**: Basic layout preservation (faster)

## Troubleshooting

### Common Issues

1. **Missing dependencies**
   - The script will check for required packages and provide installation instructions if any are missing.

2. **Conversion failures**
   - Enable fallback mechanisms with `--enable-fallback` and `--text-only-fallback`
   - Use verbose mode `-v` to see detailed error messages
   - Generate reports with `--generate-report` to identify problematic elements

3. **Poor conversion quality**
   - Try increasing quality settings with `--image-quality high --table-mode accurate --layout-fidelity high`
   - Complex PDFs with unusual formatting may require manual adjustments after conversion

4. **Memory issues with large PDFs**
   - Convert specific page ranges using `--page-range`
   - Split large PDFs into smaller files before conversion

## Limitations

- Very complex tables with merged cells or nested tables might not convert perfectly
- PDFs with interactive elements, form fields, or complex mathematical equations may not convert accurately
- The exact layout might not be 100% preserved, especially for documents with complex multi-column layouts or floating elements

## License

This project is open source and available under the MIT License.
