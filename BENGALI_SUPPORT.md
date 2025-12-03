# Bengali Language Support (বাংলা ভাষা সমর্থন)

This PDF to Audiobook converter now supports **Bengali language** with high-quality neural voice!

## Voice Details

- **Language**: Bengali (বাংলা)
- **Voice Name**: Nabanita Neural
- **Voice Code**: `bn-BD-NabanitaNeural`
- **Gender**: Female
- **Quality**: High-quality neural voice from Microsoft Edge TTS

## How to Use - Web Interface

### Step 1: Start the Application
```bash
streamlit run streamlit_app.py
```

### Step 2: Select Bengali Language
1. Look at the **sidebar** on the left
2. Under **"Settings"** → **"Language"**
3. Select **"Bengali (বাংলা)"** from the dropdown
4. You'll see: 🇧🇩 Bengali voice: Nabanita (Female)

### Step 3: Upload Your Bengali PDF
1. Drag and drop your Bengali PDF file
2. Or click "Browse files" to select it

### Step 4: Convert
1. Click the **"Convert to Audiobook"** button
2. Wait for the conversion (progress bar will show)
3. Status message will appear in Bengali: "বাংলায় অডিও তৈরি হচ্ছে..."

### Step 5: Download
1. Preview the audio in the browser
2. Click **"Download Audiobook"** to save the MP3 file

## How to Use - Command Line

### Basic Bengali Conversion
```bash
python pdf_to_audiobook.py bengali_book.pdf -e edge -l bn
```

### With Custom Output Name
```bash
python pdf_to_audiobook.py bengali_book.pdf -e edge -l bn -o my_audiobook.mp3
```

### Specify Voice Explicitly
```bash
python pdf_to_audiobook.py bengali_book.pdf -e edge -l bn -v bn-BD-NabanitaNeural
```

## Example Output

```bash
$ python pdf_to_audiobook.py bangla.pdf -e edge -l bn

============================================================
PDF to Audiobook Converter
============================================================
Opening PDF file: bangla.pdf
Total pages: 5
Processing page 5/5...
Successfully extracted text from 5 pages
Extracted 2,450 characters
Cleaning text (preserving punctuation for pauses)...
Cleaned text: 2,390 characters
Converting text to speech using Microsoft Edge TTS...
Using voice: Bengali - Nabanita (Female)
Audiobook saved to: bangla_audiobook.mp3
File size: 1.23 MB
High-quality neural voice audio generated!
============================================================
Conversion completed successfully!
============================================================
```

## Language Comparison

| Feature | English | Bengali |
|---------|---------|---------|
| Language Code | `en` | `bn` |
| Voice | Aria Neural | Nabanita Neural |
| Gender | Female | Female |
| Region | US | Bangladesh |
| Voice ID | `en-US-AriaNeural` | `bn-BD-NabanitaNeural` |

## Tips for Best Results

### For Bengali PDFs:
1. **Font encoding**: Ensure your PDF uses Unicode Bengali fonts
2. **Text-based**: PDF must contain selectable Bengali text (not scanned images)
3. **Clean text**: PDFs with clear Bengali typography work best
4. **Internet required**: Edge TTS needs internet connection for conversion

### Testing Bengali Support:
1. Create a simple text file with Bengali text
2. Convert to PDF
3. Use this converter to test
4. Verify the pronunciation is correct

## Sample Bengali Text

If you want to test, here's sample Bengali text:

```
আমার সোনার বাংলা, আমি তোমায় ভালোবাসি।
চিরদিন তোমার আকাশ, তোমার বাতাস, আমার প্রাণে বাজায় বাঁশি।
```

Save this in a PDF and convert it to test the Bengali voice!

## Troubleshooting

### Issue: Bengali text appears as boxes or ???
**Solution**: Your PDF may not have proper Unicode encoding. Re-create the PDF with Unicode Bengali fonts.

### Issue: Voice sounds wrong
**Solution**: Make sure you selected "Bengali (বাংলা)" in the language dropdown. The voice should show as "Nabanita".

### Issue: Conversion fails
**Solution**: 
1. Check internet connection (Edge TTS requires it)
2. Verify the PDF contains text (not just images)
3. Try a smaller PDF first to test

## Future Enhancements

Potential future additions:
- [ ] More Bengali voices (male voice)
- [ ] Regional variations (if available)
- [ ] Speed control for Bengali speech
- [ ] Pitch adjustment
- [ ] More South Asian languages

## Technical Details

### How It Works:
1. **Text Extraction**: PyPDF2 extracts Bengali text from PDF
2. **Text Cleaning**: Preserves Bengali punctuation (।, ৷, etc.)
3. **TTS Conversion**: Microsoft Edge TTS with bn-BD-NabanitaNeural voice
4. **Audio Output**: High-quality MP3 file with natural Bengali speech

### Voice Specifications:
- **Sample Rate**: 24kHz
- **Format**: MP3
- **Bitrate**: Variable (optimized for speech)
- **Neural Network**: Microsoft's latest neural TTS model

## Credits

- **Voice Provider**: Microsoft Edge TTS
- **Voice**: Nabanita Neural (bn-BD)
- **Developer**: AK Junaid
- **Technology**: Python, Streamlit, edge-tts

## Support

For questions or issues with Bengali support:
1. Check that your PDF has proper Bengali Unicode text
2. Ensure internet connection is stable
3. Try with a small Bengali PDF first
4. Verify language selection in settings

---

**বাংলায় PDF থেকে অডিওবুক তৈরি করুন সহজেই!**

*Create Bengali audiobooks from PDFs easily!*
