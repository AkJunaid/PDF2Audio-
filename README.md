<!-- filepath: /home/junaid/PDF2AB/test/pdftoaudiobook/README.md -->
# PDF to Audiobook Converter

Convert any PDF document into a high-quality audiobook using Microsoft's Edge TTS technology. Features a beautiful web interface with drag-and-drop functionality.

## What Does This Do?

1. **Upload a PDF** - Drag and drop or browse for your PDF file
2. **Extract Text** - Automatically reads all text from every page
3. **Clean Text** - Preserves punctuation for natural pauses
4. **Generate Audio** - Converts text to speech using Microsoft Edge TTS
5. **Download Audiobook** - Get your MP3 file instantly

## Features

- **Web Interface** - Beautiful Streamlit-based web app with drag & drop
- **Microsoft Edge TTS** - High-quality neural voices with NO rate limits
- **Real-time Progress** - Watch the conversion progress live
- **Audio Preview** - Listen before downloading
- **One-Click Download** - Instantly download your audiobook
- **Multiple Accents** - English (US, UK, Australia, India)
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
2. **Drag & drop** your PDF file or click to browse
3. Click **"Convert to Audiobook"**
4. **Preview** the audio in your browser
5. **Download** your audiobook!

---

## Requirements

- Python 3.7 or higher
- Internet connection (for Edge TTS)
- Modern web browser
- ~100MB disk space

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

**Basic Usage:**
```bash
python pdf_to_audiobook.py mybook.pdf -e edge
```

**Custom Output:**
```bash
python pdf_to_audiobook.py mybook.pdf -o audiobook.mp3 -e edge
```

**All Options:**
```bash
python pdf_to_audiobook.py <PDF_FILE> [OPTIONS]

Options:
  -o, --output FILE     Output audio file name
  -e, --engine ENGINE   TTS engine: edge (recommended)
  -l, --language LANG   Language code (default: en)
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

## Why Microsoft Edge TTS?

| Feature | Benefit |
|---------|---------|
| **High Quality** | Natural-sounding neural voices |
| **No Rate Limits** | Convert unlimited PDFs |
| **Fast Processing** | Quick conversion times |
| **Multiple Accents** | US, UK, Australian, Indian English |
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
**Solution:** Use OCR software first to convert images to text, or ensure your PDF has selectable text

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
├── README.md             # This file
├── STREAMLIT_GUIDE.md    # Web app documentation
├── setup.sh              # Quick setup script
└── examples/             # Usage examples
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

## Use Cases

- **Study Materials** - Convert textbooks to audiobooks for studying on-the-go
- **Research Papers** - Listen to papers while commuting
- **Documentation** - Convert technical docs to audio format
- **Accessibility** - Make documents accessible for visually impaired users
- **Multitasking** - Listen to content while doing other tasks

## Limitations

- Only works with **text-based PDFs** (not scanned images/photos)
- Requires **internet connection** for Edge TTS
- Large PDFs may take **several minutes** to process
- Audio file size proportional to PDF length

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Improve documentation
- Submit pull requests

## License

This project is open source and available under the MIT License.

---

**Made with love using Streamlit and Microsoft Edge TTS**

**Start converting your PDFs to audiobooks today!**