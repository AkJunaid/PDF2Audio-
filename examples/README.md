# Examples

This directory contains example usage scripts for the PDF to Audiobook converter.

## Quick Start Examples

### Example 1: Basic Conversion
```bash
python pdf_to_audiobook.py examples/sample.pdf
```

### Example 2: Custom Output Name
```bash
python pdf_to_audiobook.py mybook.pdf -o myaudiobook.mp3
```

### Example 3: Using Offline Engine
```bash
python pdf_to_audiobook.py mybook.pdf -e pyttsx3
```

### Example 4: British English
```bash
python pdf_to_audiobook.py mybook.pdf -l en-gb
```

## Batch Conversion Script

Create a file named `batch_convert.sh`:

```bash
#!/bin/bash
# Convert multiple PDFs to audiobooks

for pdf in *.pdf; do
    echo "Converting $pdf..."
    python pdf_to_audiobook.py "$pdf"
done

echo "All conversions completed!"
```

Make it executable:
```bash
chmod +x batch_convert.sh
```

Run it:
```bash
./batch_convert.sh
```

## Python Script Example

```python
from pdf_to_audiobook import PDFToAudiobook

# Create converter instance
converter = PDFToAudiobook(
    pdf_path="mybook.pdf",
    output_path="myaudiobook.mp3",
    engine="gtts",
    language="en"
)

# Convert
success = converter.convert()

if success:
    print("Conversion successful!")
else:
    print("Conversion failed!")
```
