# PDF Preview Setup Guide

The PDF preview feature allows you to see thumbnail images of your selected pages before converting them to audiobook.

## Requirements

### Python Packages
```bash
pip install pdf2image Pillow
```

### System Dependencies

The `pdf2image` library requires **Poppler** to be installed on your system.

## Installation by Operating System

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install poppler-utils
```

### Linux (Arch)
```bash
sudo pacman -S poppler
```

### Linux (Fedora/RHEL)
```bash
sudo yum install poppler-utils
```

### macOS
```bash
# Using Homebrew
brew install poppler
```

### Windows

**Option 1: Using Chocolatey**
```powershell
choco install poppler
```

**Option 2: Manual Installation**
1. Download poppler for Windows from: http://blog.alivate.com.au/poppler-windows/
2. Extract the archive
3. Add the `bin` folder to your system PATH:
   - Right-click "This PC" → Properties
   - Advanced system settings → Environment Variables
   - Edit PATH variable
   - Add path to poppler's `bin` folder (e.g., `C:\poppler\bin`)

## Verifying Installation

Test if poppler is installed:

```bash
# Linux/macOS
pdftoppm -h

# Windows (in Command Prompt or PowerShell)
pdftoppm -h
```

If the command shows help text, poppler is installed correctly!

## Testing PDF Preview

1. Install the Python packages:
```bash
pip install pdf2image Pillow
```

2. Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

3. Upload a PDF file

4. Select "Page Range" or "Specific Pages"

5. Check the "Show page previews" checkbox

6. You should see thumbnail images of your selected pages!

## Features

### Page Range Preview
- Shows thumbnails of pages in your selected range
- Displays up to 10 pages at once
- 3 thumbnails per row for easy viewing
- Each thumbnail labeled with page number

### Specific Pages Preview
- Shows thumbnails of individually selected pages
- Supports comma-separated pages (1,3,5)
- Supports ranges (7-10)
- Preview limited to first 10 pages for performance

### Preview Settings
- Resolution: 100 DPI (optimized for speed)
- Thumbnail width: 300px
- Grid layout: 3 columns
- Maintains aspect ratio

## Troubleshooting

### "pdf2image could not be imported"
**Solution:** Install the package
```bash
pip install pdf2image
```

### "poppler not found" or "Unable to get page count"
**Solution:** Install poppler (see installation instructions above)

### Preview is slow
**Cause:** Large PDFs or high page count

**Solutions:**
1. Select fewer pages
2. Preview is limited to 10 pages max
3. Preview is optional - you can convert without it

### Import error on Windows
**Cause:** Poppler not in PATH

**Solution:**
1. Verify poppler installation
2. Add poppler `bin` folder to PATH
3. Restart terminal/IDE
4. Try again

### Permission errors
**Cause:** Insufficient permissions for temp directory

**Solution:**
- Run with appropriate permissions
- Check temp directory access

## Without Preview

**Don't have poppler?** No problem!

The PDF preview feature is **optional**. You can still:
- Select pages by number
- Convert to audiobook
- Everything works except the visual preview

The app will show a message about missing packages but continue working normally.

## Performance Tips

1. **Large PDFs**: Preview loads faster with fewer pages
2. **Page selection**: More efficient than "All Pages" preview
3. **DPI setting**: 100 DPI is optimized (higher = slower)
4. **Caching**: Streamlit caches previews for faster re-display

## Technical Details

### How It Works
1. PDF uploaded and saved to temp file
2. `pdf2image` calls poppler's `pdftoppm` utility
3. Converts PDF pages to PIL Image objects
4. Images displayed in Streamlit grid layout
5. Temp files cleaned up after use

### Libraries Used
- **pdf2image**: Python wrapper for poppler
- **Pillow (PIL)**: Image processing
- **poppler**: PDF rendering engine
- **streamlit**: Display framework

## Alternative: Without Poppler

If you can't install poppler, you can comment out the preview feature:

1. Open `streamlit_app.py`
2. Find the preview sections
3. Comment out or remove the preview code
4. App will work without preview feature

Or simply don't check the "Show page previews" checkbox!

## System Requirements

### Minimum
- Python 3.7+
- 100MB free disk space
- Poppler utilities

### Recommended
- Python 3.8+
- 500MB free disk space (for temp files)
- Fast SSD for better preview performance

## Security Note

- PDF files are stored temporarily only during processing
- Temp files are automatically deleted after conversion
- No PDFs are uploaded to external servers
- All processing happens locally on your machine

---

**Need Help?**

If you encounter issues:
1. Verify poppler is installed: `pdftoppm -h`
2. Check Python packages: `pip list | grep pdf2image`
3. Try a small PDF first (< 10 pages)
4. Check error messages in terminal
5. Preview is optional - conversion works without it!
