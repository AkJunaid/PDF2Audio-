<!-- filepath: /home/junaid/PDF2AB/test/pdftoaudiobook/README.md -->
# PDF to Audiobook Converter

Convert any PDF document into a high-quality audiobook using Microsoft's Edge TTS technology. Features a beautiful web interface with drag-and-drop functionality.

**NEW:** Bengali language support, page selection, and custom file naming!

## What Does This Do?

1. **Upload a PDF** - Drag and drop or browse for your PDF file
2. **Extract Text** - Automatically reads all text from every page
3. **Clean Text** - Preserves punctuation for natural pauses
4. **Generate Audio** - Converts text to speech using Microsoft Edge TTS
5. **Download Audiobook** - Get your MP3 file instantly

## Features

- **Web Interface** - Beautiful Streamlit-based web app with drag & drop
- **Microsoft Edge TTS** - High-quality neural voices with NO rate limits
- **Multi-Language Support** - English and Bengali (বাংলা)
- **Page Selection** - Convert all pages, specific range, or individual pages
- **PDF Preview** - See thumbnails of selected pages before converting
- **OCR Support** - Automatically handles scanned PDFs with no selectable text
- **Custom Naming** - Name your audiobook file before downloading
- **Real-time Progress** - Watch the conversion progress live
- **Audio Preview** - Listen before downloading
- **One-Click Download** - Instantly download your audiobook
- **Natural Voices** - Female neural voices for both languages
- **Privacy-Focused** - Files processed securely, not stored

## Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Web App
```bash
streamlit run streamlit_app.py
```

### Step 3: Convert Your PDF!
1. Open your browser (automatically opens to `http://localhost:8501`)
2. **Select Language** - Choose English or Bengali from the sidebar
3. **Drag & drop** your PDF file or click to browse
4. **Choose Pages** - Select all pages, a range (e.g., 1-10), or specific pages
5. **Preview Pages** (optional) - Check "Show page previews" to see thumbnails
6. **Name Your File** - Enter a custom name for your audiobook
7. Click **"Convert to Audiobook"**
8. **Preview Audio** - Listen in your browser
9. **Download** your audiobook!

---

## Requirements

### Core Requirements
- Python 3.7 or higher
- Internet connection (for Edge TTS)
- Modern web browser
- ~100MB disk space

### Optional (for PDF Preview & OCR)
- **Poppler utilities** (for page thumbnails)
  - Arch: `sudo pacman -S poppler`
  - Ubuntu: `sudo apt-get install poppler-utils`
  - See [PDF_PREVIEW_SETUP.md](PDF_PREVIEW_SETUP.md) for other OS

- **Tesseract-OCR** (for scanned PDFs)
  - Arch: `sudo pacman -S tesseract tesseract-data-eng tesseract-data-ben`
  - Ubuntu: `sudo apt-get install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ben`
  - See [OCR_SETUP.md](OCR_SETUP.md) for complete guide

**Note:** PDF preview and OCR are optional - the app works without them!

---

## Two Ways to Use

### Option 1: Web Interface (Recommended)

**Launch the Web App:**
```bash
streamlit run streamlit_app.py
```

**Features:**
- Drag & drop file upload
- Beautiful, modern interface
- Real-time conversion progress
- Built-in audio player
- One-click download
- Easy settings configuration

### Option 2: Command Line

**Basic Usage (English):**
```bash
python pdf_to_audiobook.py mybook.pdf -e edge
```

**Bengali Audiobook:**
```bash
python pdf_to_audiobook.py bengali.pdf -e edge -l bn
```

**Custom Voice:**
```bash
python pdf_to_audiobook.py mybook.pdf -e edge -v bn-BD-NabanitaNeural
```

**All Options:**
```bash
python pdf_to_audiobook.py <PDF_FILE> [OPTIONS]

Options:
  -o, --output FILE     Output audio file name
  -e, --engine ENGINE   TTS engine: edge (recommended)
  -l, --language LANG   Language code: en (English), bn (Bengali)
  -v, --voice VOICE     Voice ID (en-US-AriaNeural, bn-BD-NabanitaNeural)
```

---

## How It Works

```
┌─────────────────┐
│   Upload PDF    │  Drag & drop or browse for PDF
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Extract Text   │  Reads all text from every page
└────────┬────────┘  Using PyPDF2 library
         │
         ▼
┌─────────────────┐
│   Clean Text    │  Preserves: periods, commas, semicolons
└────────┬────────┘  Keeps: question marks, exclamation marks
         │           Result: Natural pauses in speech
         ▼
┌─────────────────┐
│ Microsoft Edge  │  High-quality neural voice
│      TTS        │  Natural intonation & pacing
└────────┬────────┘  NO rate limits
         │
         ▼
┌─────────────────┐
│ Generate Audio  │  Converts text to speech
└────────┬────────┘  Professional quality MP3
         │
         ▼
┌─────────────────┐
│ Preview & Save  │  Listen in browser
└────────┬────────┘  Download with one click
         │
         ▼
┌─────────────────┐
│   Audiobook!    │  Listen anywhere, anytime
└─────────────────┘
```

## Supported Languages

| Language | Code | Voice | Gender |
|----------|------|-------|--------|
| **English (US)** | `en` | Aria Neural | Female |
| **Bengali (বাংলা)** | `bn` | Nabanita Neural | Female |

### How to Use Bengali

**Web Interface:**
1. Open the app: `streamlit run streamlit_app.py`
2. In the sidebar, select "Bengali (বাংলা)" from language dropdown
3. Upload your Bengali PDF
4. Convert and download!

**Command Line:**
```bash
python pdf_to_audiobook.py bengali.pdf -e edge -l bn
```

**For detailed Bengali documentation, see:** [BENGALI_SUPPORT.md](BENGALI_SUPPORT.md)

## OCR for Scanned PDFs

**NEW:** Automatic text extraction from scanned PDFs using OCR!

### What is OCR?

OCR (Optical Character Recognition) extracts text from images and scanned documents. When your PDF has no selectable text (like a scanned book), OCR automatically activates.

### How It Works

1. **Automatic Detection** - App detects pages with little/no text
2. **OCR Activation** - Converts page to high-quality image (300 DPI)
3. **Text Extraction** - Uses Tesseract to read the text
4. **Language Support** - Works for both English and Bengali

### Setup OCR

**Quick Install (Arch Linux):**
```bash
sudo pacman -S tesseract tesseract-data-eng tesseract-data-ben
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ben
```

**For complete setup guide:** [OCR_SETUP.md](OCR_SETUP.md)

### Using OCR

No special steps! Just:
1. Select your language (English or Bengali)
2. Upload a scanned PDF
3. OCR runs automatically on pages without selectable text
4. Watch console for "OCR successful" messages

### Performance Note

OCR takes 2-5 seconds per page (slower than regular extraction). For best results:
- Use high-quality scans
- Ensure text is clear and not skewed
- Works best with printed text (not handwritten)

## Page Selection Feature

Convert only the pages you need! Three options available:

### 1. All Pages (Default)
Converts the entire PDF from start to finish.

### 2. Page Range
Convert a continuous range of pages.

**Examples:**
- Pages 1-10: First 10 pages
- Pages 5-15: Pages 5 through 15
- Pages 20-25: Just pages 20 to 25

**Web Interface:**
1. Select "Page Range" option
2. Enter start page and end page
3. Click Convert

**Command Line:**
```bash
# Not yet supported in CLI - use web interface
```

### 3. Specific Pages
Convert selected individual pages or multiple ranges.

**Examples:**
- `1,3,5,7` - Pages 1, 3, 5, and 7
- `1-5,10,15-20` - Pages 1 through 5, page 10, and pages 15 through 20
- `2,4,6,8,10-15` - Even pages 2-8 plus pages 10-15

**Web Interface:**
1. Select "Specific Pages" option
2. Enter page numbers (comma-separated)
3. Use dash for ranges (e.g., 7-10)
4. Click Convert

**Use Cases:**
- Convert only introduction/summary chapters
- Skip table of contents or index pages
- Convert specific chapters or sections
- Focus on pages with important content
- Faster conversion for large PDFs

## Custom Filename

Name your audiobook before downloading!

**Default:** `original_filename_audiobook.mp3`

**Custom:** Enter any name you want (special characters will be auto-cleaned)

**Examples:**
- `chapter_1` → `chapter_1.mp3`
- `bengali_story` → `bengali_story.mp3`
- `my audiobook 2024` → `my_audiobook_2024.mp3`

## Why Microsoft Edge TTS?

| Feature | Benefit |
|---------|---------|
| **High Quality** | Natural-sounding neural voices |
| **No Rate Limits** | Convert unlimited PDFs |
| **Fast Processing** | Quick conversion times |
| **Multi-Language** | English and Bengali support |
| **Free** | Completely free to use |
| **Reliable** | Stable and consistent results |

## Web Interface Preview

The Streamlit web interface provides:
- **File Upload Status** - Visual confirmation of uploaded file
- **Progress Tracking** - Real-time conversion progress
- **Audio Player** - Preview before downloading
- **Download Button** - One-click audiobook download
- **Smart Tips** - Helpful guidance throughout
- **Settings Panel** - Configure language and options

## Command Line Example

```bash
$ python pdf_to_audiobook.py book.pdf -e edge

============================================================
PDF to Audiobook Converter
============================================================
Opening PDF file: book.pdf
Total pages: 10
Processing page 10/10...
Successfully extracted text from 10 pages
Extracted 15,234 characters
Cleaning text (preserving punctuation for pauses)...
Cleaned text: 14,890 characters
Converting text to speech using Microsoft Edge TTS...
Using voice: en-US-AriaNeural (Natural Female Voice)
Audiobook saved to: book_audiobook.mp3
File size: 12.45 MB
High-quality neural voice audio generated!
============================================================
Conversion completed successfully!
============================================================
```

## Troubleshooting

### Problem: "No text extracted from PDF"
**Cause:** PDF contains images/scanned pages (not text)  
**Solution:** Install Tesseract-OCR for automatic text extraction from scanned PDFs. See [OCR_SETUP.md](OCR_SETUP.md) for details

### Problem: "Connection error" or "Network error"
**Cause:** No internet connection  
**Solution:** Edge TTS requires internet. Check your connection and try again

### Problem: Web app won't open
**Solution:**
```bash
# Check if Streamlit is installed
pip install streamlit

# Try specifying a different port
streamlit run streamlit_app.py --server.port 8080

# Check if port is already in use
netstat -tulpn | grep 8501
```

### Problem: Slow conversion
**Cause:** Large PDF file  
**Solution:** This is normal. Edge TTS processes text in real-time. Check the progress bar for status

### Problem: Audio file too large
**Solution:** The audio file size depends on PDF length. This is expected for long documents

## Project Structure

```
pdftoaudiobook/
├── streamlit_app.py       # Web interface (MAIN)
├── pdf_to_audiobook.py    # Core conversion script
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── STREAMLIT_GUIDE.md     # Web app documentation
├── setup.sh               # Quick setup script
└── examples/              # Usage examples
    └── README.md
```

## Technical Details

### Core Dependencies
- **Streamlit** - Modern web framework for the interface
- **edge-tts** - Microsoft Edge Text-to-Speech
- **PyPDF2** - PDF text extraction library

### Text Cleaning Process
**Removed:**
- Parentheses `()`, Brackets `[]`, Braces `{}`
- Quotes `"` and `'`
- Hyphens and underscores
- Forward/backward slashes
- Extra whitespace

**Preserved for Natural Pauses:**
- Periods (`.`) - Long pauses
- Commas (`,`) - Short pauses
- Semicolons (`;`) and Colons (`:`) - Medium pauses
- Question marks (`?`) - Proper intonation
- Exclamation marks (`!`) - Emphasis

## Tips for Best Results

1. **Use the web interface** - Much easier than command line
2. **Check your PDF** - Ensure it's text-based, not scanned images
3. **Stable internet** - Edge TTS needs a good internet connection
4. **Test first** - Try with a small PDF to check quality
5. **Choose accent** - Select your preferred English accent in settings
6. **Preview audio** - Listen before downloading to ensure quality
7. **Large PDFs** - Be patient, conversion takes time proportional to length
