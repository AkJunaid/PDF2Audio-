# OCR Setup Guide

This guide explains how to set up OCR (Optical Character Recognition) for handling scanned PDFs.

## What is OCR?

OCR allows the application to extract text from scanned PDFs or images. When a PDF page has no selectable text (like a scanned document), the app automatically uses OCR to extract the text.

## System Requirements

OCR requires two system packages:

1. **Tesseract-OCR**: The OCR engine
2. **Poppler**: PDF rendering utilities (already needed for PDF preview)

## Installation Instructions

### Arch Linux (Your System)

```bash
# Install Tesseract and language packs
sudo pacman -S tesseract tesseract-data-eng tesseract-data-ben

# Install Poppler (if not already installed)
sudo pacman -S poppler
```

### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ben poppler-utils
```

### Fedora/RHEL

```bash
sudo yum install tesseract tesseract-langpack-eng tesseract-langpack-ben poppler-utils
```

### macOS

```bash
brew install tesseract tesseract-lang poppler
```

### Windows

1. Download Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. During installation, select "Bengali" and "English" language packs
3. Add Tesseract to your PATH
4. Install poppler from: https://github.com/oschwartz10612/poppler-windows/releases/

## Verification

After installation, verify Tesseract is working:

```bash
# Check Tesseract version
tesseract --version

# List installed languages
tesseract --list-langs
```

You should see both `eng` and `ben` in the language list.

## How OCR Works in This App

1. **Automatic Detection**: When a PDF page has little or no extractable text (< 50 characters), OCR is automatically triggered
2. **Language Support**: OCR works for both English and Bengali documents
3. **High Quality**: Uses 300 DPI for better accuracy
4. **Fallback**: If OCR fails, the app continues with other pages

## OCR Performance

- **Speed**: OCR is slower than regular text extraction (2-5 seconds per page)
- **Accuracy**: Depends on scan quality. Better scans = better accuracy
- **Languages**: Currently supports English and Bengali

## Troubleshooting

### "tesseract: command not found"

**Solution**: Tesseract is not installed. Follow installation instructions above.

### "Failed to load language 'ben'"

**Solution**: Bengali language pack not installed. Install with:

```bash
# Arch Linux
sudo pacman -S tesseract-data-ben

# Ubuntu/Debian
sudo apt-get install tesseract-ocr-ben
```

### OCR produces gibberish

**Possible causes**:
1. Very poor scan quality
2. Wrong language selected (e.g., Bengali PDF with English OCR)
3. Handwritten text (OCR works best with printed text)

**Solution**: Try rescanning the document at higher quality, or ensure correct language is selected.

### OCR is too slow

**Solutions**:
1. Reduce page range (convert fewer pages at once)
2. Use specific pages instead of all pages
3. Consider pre-processing: Convert scanned PDF to text PDF using external tools first

## Using OCR

No special steps needed! Just:

1. Select your language (English or Bengali)
2. Upload your PDF
3. If it's a scanned PDF, OCR will activate automatically
4. Watch the console for OCR progress messages

## Example Console Output

```
Processing page 1 of 10...
Page 1: Little/no text found, trying OCR...
Page 1: OCR successful, extracted 450 characters

Processing page 2 of 10...
Page 2: OCR successful, extracted 520 characters
```

## Python Packages

OCR requires these Python packages (already in requirements.txt):

- `pytesseract>=0.3.10` - Python wrapper for Tesseract
- `pdf2image>=1.16.0` - Convert PDF pages to images
- `Pillow>=10.0.0` - Image processing

Install with:

```bash
pip install -r requirements.txt
```

## Advanced Configuration

The OCR method in `pdf_to_audiobook.py` can be customized:

```python
# Current settings
dpi=300  # Higher = better quality but slower
lang='ben+eng'  # Bengali + English for Bengali PDFs
lang='eng'  # English only for English PDFs
```

## Bengali OCR Notes

- Bengali OCR accuracy may vary depending on font and quality
- Best results with clear, printed Bengali text
- Handwritten Bengali text may not work well
- Mixed Bengali-English pages are supported (ben+eng)

## Support

For OCR issues, check:
1. Tesseract is installed: `tesseract --version`
2. Language packs are installed: `tesseract --list-langs`
3. Python packages are installed: `pip list | grep pytesseract`
4. PDF is actually scanned (no selectable text)

If problems persist, try testing Tesseract directly:

```bash
# Convert PDF page to image first
pdftoppm -png -f 1 -l 1 yourfile.pdf page
# Then test OCR
tesseract page-1.png output -l eng
cat output.txt
```
