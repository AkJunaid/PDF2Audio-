# PDF to Audiobook - Streamlit Web App

A beautiful web interface for converting PDF documents to audiobooks with drag-and-drop functionality.

## Quick Start

### 1. Install Dependencies

```bash
pip install streamlit edge-tts
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the Web App

```bash
streamlit run streamlit_app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

## Features

### Easy Upload
- **Drag and drop** PDF files directly into the browser
- Or **click to browse** and select files
- Instant file validation and preview

### Multiple TTS Engines
- **Google TTS (gTTS)** - Best quality, requires internet
- **Microsoft Edge TTS** - High quality, no rate limits
- **eSpeak** - Fast, offline, basic quality
- **Pyttsx3** - Offline option

### Language Support
- English (US)
- English (UK)
- English (Australia)
- English (India)

### Download Options
- **Preview audio** directly in the browser
- **Download audiobook** with one click
- Support for MP3 and WAV formats

## User Interface

### Main Features
1. **Upload Section** - Drag and drop or browse for PDF files
2. **Settings Sidebar** - Configure TTS engine and language
3. **Convert Button** - Start the conversion process
4. **Progress Tracking** - Real-time conversion status
5. **Audio Player** - Preview your audiobook
6. **Download Button** - Save the audiobook to your device

### Progress Indicators
- File upload status
- Text extraction progress
- Text cleaning status
- Speech conversion progress
- Download ready notification

## Screenshots

The web interface includes:
- Clean, modern design
- Responsive layout
- Real-time progress tracking
- Built-in audio player
- One-click download

## Configuration

### TTS Engine Selection

**Google TTS (Recommended)**
- Best natural voice quality
- May have rate limits (wait 15-30 minutes if hit)
- Requires internet connection

**Microsoft Edge TTS (Recommended)**
- High-quality neural voices
- No rate limits
- Requires internet connection
- Excellent alternative to gTTS

**eSpeak (Offline)**
- Works without internet
- Basic robotic voice
- Fast processing
- Good for testing

**Pyttsx3**
- Offline option
- May be unreliable
- Not recommended

### Language Options
Select your preferred English accent from the sidebar.

## Privacy & Security

- **No data storage** - Files are processed in temporary memory
- **Secure processing** - Files are deleted after conversion
- **Local processing** - PDFs are processed on the server, not uploaded to external services

## Troubleshooting

### Rate Limit Error (gTTS)
**Problem:** "429 Too Many Requests" error

**Solutions:**
1. Wait 15-30 minutes and try again
2. Use Microsoft Edge TTS (no rate limits)
3. Use eSpeak for offline conversion

### Conversion Failed
**Problem:** Audiobook not generated

**Solutions:**
1. Check if PDF has extractable text (not scanned images)
2. Try a different TTS engine
3. Ensure you have internet connection (for online engines)

### Audio Quality Issues
**Problem:** Audio sounds robotic or unnatural

**Solutions:**
1. Use gTTS or Edge TTS for best quality
2. Avoid pyttsx3 and eSpeak for important documents
3. Check language/accent settings

## Dependencies

- `streamlit` - Web framework
- `PyPDF2` - PDF text extraction
- `gTTS` - Google Text-to-Speech
- `edge-tts` - Microsoft Edge TTS
- `pyttsx3` - Offline TTS
- `pydub` - Audio processing

## Use Cases

- **Study materials** - Convert textbooks to audiobooks
- **Research papers** - Listen to papers while commuting
- **Documentation** - Convert manuals to audio format
- **Accessibility** - Make documents accessible for visually impaired users
- **Multitasking** - Listen to content while doing other tasks

## Advanced Usage

### Running on a Different Port

```bash
streamlit run streamlit_app.py --server.port 8080
```

### Running on Network

```bash
streamlit run streamlit_app.py --server.address 0.0.0.0
```

### Configuration File

Create `.streamlit/config.toml`:

```toml
[server]
port = 8501
address = "localhost"

[theme]
primaryColor = "#4CAF50"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## Tips for Best Results

1. **Use clear PDFs** - Scanned PDFs may not work well
2. **Check text** - Ensure PDF has selectable text
3. **Choose quality** - Use gTTS or Edge TTS for best results
4. **Be patient** - Large PDFs take time to process
5. **Test first** - Try a small PDF before converting large documents

## Contributing

Feel free to contribute improvements:
- Better UI/UX
- Additional TTS engines
- More language support
- Enhanced error handling

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Uses [gTTS](https://github.com/pndurette/gTTS) for Google TTS
- Uses [edge-tts](https://github.com/rany2/edge-tts) for Microsoft TTS
- PDF processing with [PyPDF2](https://github.com/py-pdf/pypdf2)

---

**Enjoy converting your PDFs to audiobooks!**
