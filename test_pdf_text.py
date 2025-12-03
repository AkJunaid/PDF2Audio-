#!/usr/bin/env python3
"""
Quick test to check if a PDF has extractable text (especially Bengali)
Usage: python test_pdf_text.py your_file.pdf
"""

import sys
import PyPDF2

def test_pdf_extraction(pdf_path):
    """Test if PDF has extractable text"""
    print("=" * 60)
    print(f"Testing PDF: {pdf_path}")
    print("=" * 60)
    print()
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            
            print(f"📄 Total Pages: {total_pages}")
            print()
            
            total_text = ""
            bengali_count = 0
            english_count = 0
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                print(f"Processing page {page_num}/{total_pages}...")
                
                # Try standard extraction
                try:
                    text = page.extract_text()
                    if text:
                        total_text += text
                        
                        # Count Bengali characters (Unicode range 0980-09FF)
                        bengali_chars = sum(1 for c in text if '\u0980' <= c <= '\u09FF')
                        bengali_count += bengali_chars
                        
                        # Count English characters
                        english_chars = sum(1 for c in text if c.isalpha() and ord(c) < 128)
                        english_count += english_chars
                        
                        print(f"  ✓ Page {page_num}: {len(text)} chars, {bengali_chars} Bengali, {english_chars} English")
                    else:
                        print(f"  ✗ Page {page_num}: No text found")
                except Exception as e:
                    print(f"  ✗ Page {page_num}: Error - {e}")
            
            print()
            print("=" * 60)
            print("RESULTS")
            print("=" * 60)
            print(f"Total Characters: {len(total_text)}")
            print(f"Bengali Characters: {bengali_count}")
            print(f"English Characters: {english_count}")
            print()
            
            if len(total_text) == 0:
                print("❌ NO TEXT FOUND")
                print()
                print("This PDF likely contains:")
                print("  • Scanned images (not actual text)")
                print("  • Graphics/pictures only")
                print("  • Non-standard encoding")
                print()
                print("Solutions:")
                print("  1. Use OCR software to convert images to text")
                print("  2. Re-create the PDF with selectable text")
                print("  3. Try a different PDF")
                return False
            
            elif bengali_count > 0:
                print("✅ BENGALI TEXT FOUND!")
                print()
                print("Sample text (first 200 characters):")
                print("-" * 60)
                sample = total_text[:200].replace('\n', ' ')
                print(sample)
                print("-" * 60)
                print()
                print("✓ This PDF should work with Bengali conversion!")
                return True
            
            elif english_count > 0:
                print("✅ ENGLISH TEXT FOUND!")
                print()
                print("Sample text (first 200 characters):")
                print("-" * 60)
                sample = total_text[:200].replace('\n', ' ')
                print(sample)
                print("-" * 60)
                print()
                print("✓ This PDF should work with English conversion!")
                return True
            
            else:
                print("⚠️  TEXT FOUND BUT UNCERTAIN")
                print()
                print(f"Characters found: {len(total_text)}")
                print("But couldn't identify language clearly.")
                print()
                print("Sample text (first 200 characters):")
                print("-" * 60)
                sample = total_text[:200].replace('\n', ' ')
                print(sample)
                print("-" * 60)
                print()
                print("Try converting and see if it works!")
                return True
                
    except FileNotFoundError:
        print(f"❌ ERROR: File not found - {pdf_path}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_pdf_text.py <pdf_file>")
        print()
        print("Example:")
        print("  python test_pdf_text.py bengali.pdf")
        print("  python test_pdf_text.py mybook.pdf")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    success = test_pdf_extraction(pdf_path)
    
    sys.exit(0 if success else 1)
