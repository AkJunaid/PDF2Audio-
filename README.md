<!-- filepath: /home/junaid/PDF2AB/test/pdftoaudiobook/README.md -->
# PDF to Audiobook Converter

Convert any PDF document into a high-quality audiobook that you can listen to anywhere. Simple, fast, and supports multiple text-to-speech engines.

## What Does This Do?

1. **Upload a PDF** - The tool reads your PDF file
2. **Extract Text** - Gets all the text from every page
3. **Clean Text** - Preserves punctuation for natural pauses
4. **Generate Audio** - Converts text to speech using AI
5. **Save Audiobook** - Creates an MP3/WAV file you can listen to

## Features

- **Multiple TTS Engines**:
  - **edge-tts** - Microsoft's high-quality TTS (requires internet, NO rate limits) **RECOMMENDED**
  - **espeak** - Fast offline option (robotic voice, always works)
  - **pyttsx3** - Basic offline option (unreliable)

- **Smart Text Processing** - Preserves punctuation for natural pauses
- **Progress Tracking** - See real-time conversion status
- **English Language** - Optimized for English content
- **Easy to Use** - Simple command-line interface

## Requirements

- Python 3.7 or higher
- Internet connection (for edge-tts engine)
- ~100MB disk space

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Convert Your PDF
```bash
python pdf_to_audiobook.py your_document.pdf
```

### Step 3: Listen!
Your audiobook will be saved as `your_document_audiobook.mp3`

---

## Complete Installation Guide

### Option 1: Automated Setup (Linux/Mac)
```bash
./setup.sh
```

### Option 2: Manual Setup
```bash
# Install Python packages
pip install PyPDF2 edge-tts pyttsx3

# For offline espeak engine (Linux only)
sudo pacman -S espeak-ng  # Arch Linux
sudo apt install espeak-ng  # Ubuntu/Debian
```

---

## How to Use

### Basic Command
```bash
python pdf_to_audiobook.py mybook.pdf
```
Creates: `mybook_audiobook.mp3`

### Choose Output Name
```bash
python pdf_to_audiobook.py mybook.pdf -o audiobook.mp3
```

### Choose TTS Engine

**Best Quality (Recommended):**
```bash
python pdf_to_audiobook.py mybook.pdf -e edge
```

**Offline:**
```bash
python pdf_to_audiobook.py mybook.pdf -e espeak
```

### All Options
```bash
python pdf_to_audiobook.py <PDF_FILE> [OPTIONS]

Options:
  -o, --output FILE     Output audio file name
  -e, --engine ENGINE   TTS engine: edge, espeak, pyttsx3
  -l, --language LANG   Language code (default: en)
```

---

## Full Pipeline (How It Works)

```
┌─────────────────┐
│   Upload PDF    │  Your PDF file (any size, any pages)
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
│  Choose Engine  │  Select TTS engine:
└────────┬────────┘  • edge-tts (Microsoft) [RECOMMENDED]
         │           • espeak (Offline)
         ▼
┌─────────────────┐
│ Generate Audio  │  Converts text to speech
└────────┬────────┘  Chunk by chunk if needed
         │
         ▼
┌─────────────────┐
│  Save Output    │  Creates MP3 or WAV file
└────────┬────────┘  Ready to listen!
         │
         ▼
┌─────────────────┐
│   Audiobook!    │  Listen anywhere, anytime
└─────────────────┘
```

## TTS Engine Comparison

| Engine | Quality | Speed | Internet | Rate Limits | Best For |
|--------|---------|-------|----------|-------------|----------|
| **edge-tts** | Excellent | Fast | Yes | None | **Best choice!** |
| **espeak** | Basic | Very Fast | No | None | Offline/backup |
| **pyttsx3** | Basic | Fast | No | None | Not recommended |

## Example Output

```bash
$ python pdf_to_audiobook.py book.pdf

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
Converting text to speech using edge-tts...
Audiobook saved to: book_audiobook.mp3
============================================================
Conversion completed successfully!
============================================================
```

## Troubleshooting

### Problem: "No text extracted from PDF"
**Cause:** PDF contains images/scanned pages (not text)  
**Solution:** Use OCR software first to convert images to text

### Problem: Audio quality is poor (espeak)
**Solution:** Use edge-tts for better quality:
```bash
python pdf_to_audiobook.py file.pdf -e edge
```

### Problem: "espeak not found"
**Solution - Linux:**
```bash
# Arch Linux
sudo pacman -S espeak-ng

# Ubuntu/Debian
sudo apt install espeak-ng

# Create symlink if needed
sudo ln -s /usr/lib/libespeak-ng.so /usr/lib/libespeak.so.1
```

### Problem: Disk space error
**Solution:**
```bash
# Clean pip cache
pip cache purge

# Check available space
df -h
```

## Project Structure

```
pdftoaudiobook/
├── pdf_to_audiobook.py    # Main conversion script
├── gui.py                 # Optional GUI interface
├── requirements.txt       # Python dependencies
├── setup.sh              # Quick setup script
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── examples/             # Usage examples
    └── README.md
```

## Technical Details

### Dependencies
- **PyPDF2** - PDF text extraction
- **edge-tts** - Microsoft Edge TTS (recommended)
- **pyttsx3** - Offline TTS
- **espeak-ng** - System TTS engine

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

1. **Use edge-tts** for best balance of quality and reliability
2. **Check your PDF** - Make sure it's text-based, not scanned images
3. **Small chunks** - For very large PDFs, consider splitting into chapters
4. **Test first** - Try with a small PDF first to check quality
5. **Internet speed** - edge-tts needs stable internet

## Limitations

- Only works with text-based PDFs (not scanned images)
- Large PDFs may take several minutes to process
- Output quality depends on the TTS engine chosen