#!/usr/bin/env python3
"""
PDF to Audiobook Converter
Converts PDF files to audio (MP3) format using text-to-speech technology
"""

import os
import argparse
import re
import subprocess
import time
import asyncio
from pathlib import Path
import PyPDF2
from gtts import gTTS
import pyttsx3
import warnings
warnings.filterwarnings('ignore')


class PDFToAudiobook:
    def __init__(self, pdf_path, output_path=None, engine='gtts', language='en'):
        """
        Initialize the PDF to Audiobook converter
        
        Args:
            pdf_path (str): Path to the input PDF file
            output_path (str): Path for the output audio file (optional)
            engine (str): TTS engine to use ('gtts', 'pyttsx3', or 'espeak')
            language (str): Language code (default: 'en' for English)
        """
        self.pdf_path = pdf_path
        self.engine = engine
        self.language = language
        
        # Set output path
        if output_path:
            self.output_path = output_path
        else:
            pdf_name = Path(pdf_path).stem
            # Use WAV for espeak, MP3 for others
            extension = '.wav' if engine == 'espeak' else '.mp3'
            self.output_path = f"{pdf_name}_audiobook{extension}"
    
    def clean_text_for_speech(self, text):
        """
        Clean text while preserving punctuation for natural pauses
        
        Args:
            text (str): Raw text from PDF
            
        Returns:
            str: Cleaned text suitable for speech synthesis with proper pauses
        """
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        
        # Keep periods, commas, semicolons, colons for natural pauses
        # TTS engines use these for pacing and intonation
        # Ensure proper spacing after punctuation
        text = re.sub(r'\.(\S)', r'. \1', text)  # Period followed by non-space
        text = re.sub(r',(\S)', r', \1', text)   # Comma followed by non-space
        text = re.sub(r';(\S)', r'; \1', text)   # Semicolon followed by non-space
        text = re.sub(r':(\S)', r': \1', text)   # Colon followed by non-space
        
        # Keep question marks and exclamation marks as they affect intonation
        text = re.sub(r'\?(\S)', r'? \1', text)
        text = re.sub(r'!(\S)', r'! \1', text)
        
        # Remove parentheses and brackets but keep their content
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        text = text.replace('{', ' ')
        text = text.replace('}', ' ')
        
        # Remove quotation marks (they don't add value to speech)
        text = text.replace('"', ' ')
        text = text.replace("'", ' ')
        text = text.replace('`', ' ')
        
        # Replace dashes and underscores with spaces
        text = text.replace('--', ' ')  # Double dash
        text = text.replace('-', ' ')   # Single dash
        text = text.replace('_', ' ')
        
        # Remove backslashes and forward slashes
        text = text.replace('/', ' ')
        text = text.replace('\\', ' ')
        
        # Clean up multiple spaces again
        text = re.sub(r'\s+', ' ', text)
        
        # Clean up spacing around punctuation (avoid double spaces)
        text = re.sub(r'\s+([.,;:?!])', r'\1', text)  # Remove space before punctuation
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        return text
    
    def extract_text_from_pdf(self):
        """
        Extract text content from the PDF file
        
        Returns:
            str: Extracted text from all pages
        """
        print(f"Opening PDF file: {self.pdf_path}")
        text = ""
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                total_pages = len(pdf_reader.pages)
                print(f"Total pages: {total_pages}")
                
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    print(f"Processing page {page_num}/{total_pages}...", end='\r')
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                
                print(f"\nSuccessfully extracted text from {total_pages} pages")
                
        except FileNotFoundError:
            print(f"Error: PDF file not found at {self.pdf_path}")
            return None
        except Exception as e:
            print(f"Error reading PDF: {str(e)}")
            return None
        
        return text
    
    def text_to_speech_gtts(self, text, chunk_size=5000, retry_delay=60):
        """
        Convert text to speech using Google Text-to-Speech (gTTS)
        Split into chunks to avoid rate limiting
        
        Args:
            text (str): Text to convert to speech
            chunk_size (int): Size of text chunks (in characters)
            retry_delay (int): Delay in seconds before retry
        """
        print(f"Converting text to speech using gTTS...")
        
        # Split text into sentences for better chunking
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        chunks = []
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk) + len(sentence) < chunk_size:
                current_chunk += " " + sentence
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        print(f"Split text into {len(chunks)} chunks to avoid rate limits")
        
        # Generate audio for each chunk
        temp_files = []
        
        try:
            for i, chunk in enumerate(chunks, 1):
                print(f"Processing chunk {i}/{len(chunks)}...")
                
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        temp_file = f"temp_chunk_{i}.mp3"
                        tts = gTTS(text=chunk, lang=self.language, slow=False)
                        tts.save(temp_file)
                        temp_files.append(temp_file)
                        print(f"Chunk {i} completed")
                        
                        # Small delay between chunks to avoid rate limiting
                        if i < len(chunks):
                            time.sleep(2)
                        break
                        
                    except Exception as e:
                        if "429" in str(e) or "Too Many Requests" in str(e):
                            if attempt < max_retries - 1:
                                print(f"Rate limit hit, waiting {retry_delay} seconds...")
                                time.sleep(retry_delay)
                            else:
                                raise
                        else:
                            raise
            
            # Combine all chunks
            if len(temp_files) == 1:
                os.rename(temp_files[0], self.output_path)
            else:
                print(f"Combining {len(temp_files)} audio chunks...")
                self._combine_audio_files(temp_files, self.output_path)
                
                # Clean up temp files
                for temp_file in temp_files:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
            
            print(f"Audiobook saved to: {self.output_path}")
            return True
            
        except Exception as e:
            # Clean up temp files on error
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            
            print(f"Error during text-to-speech conversion: {str(e)}")
            if "429" in str(e) or "Too Many Requests" in str(e):
                print("Rate limit reached for gTTS API.")
                print("Solutions:")
                print("   1. Wait 15-30 minutes and try again")
                print("   2. Use espeak for offline conversion:")
                print("      python pdf_to_audiobook.py your_file.pdf -e espeak")
            return False
    
    def _combine_audio_files(self, input_files, output_file):
        """
        Combine multiple MP3 files into one
        Uses pydub if available, otherwise uses ffmpeg
        """
        try:
            from pydub import AudioSegment
            
            combined = AudioSegment.empty()
            for file in input_files:
                audio = AudioSegment.from_mp3(file)
                combined += audio
            
            combined.export(output_file, format="mp3")
            
        except ImportError:
            # Fallback to ffmpeg if pydub not available
            print("Using ffmpeg to combine audio files")
            
            # Create file list for ffmpeg
            with open('file_list.txt', 'w') as f:
                for file in input_files:
                    f.write(f"file '{file}'\n")
            
            subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 
                          'file_list.txt', '-c', 'copy', output_file], 
                          check=True, capture_output=True)
            
            os.remove('file_list.txt')
    
    def text_to_speech_pyttsx3(self, text):
        """
        Convert text to speech using pyttsx3 (offline engine)
        
        Args:
            text (str): Text to convert to speech
        """
        print(f"Converting text to speech using pyttsx3 (offline)...")
        print(f"Note: pyttsx3 may have issues saving MP3 files.")
        print(f"Recommended: Use gTTS instead (remove -e pyttsx3)")
        
        try:
            # Change output to WAV format which pyttsx3 supports better
            wav_path = self.output_path.replace('.mp3', '.wav')
            
            engine = pyttsx3.init()
            
            # Configure speech properties
            engine.setProperty('rate', 150)  # Speed of speech
            engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
            
            # Get available voices and set English voice
            voices = engine.getProperty('voices')
            english_voice_found = False
            for voice in voices:
                if 'english' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    print(f"Using voice: {voice.name}")
                    english_voice_found = True
                    break
            
            if not english_voice_found:
                print(f"No English voice found, using default voice")
            
            # Save to WAV file (more reliable than MP3)
            print(f"Saving as WAV format: {wav_path}")
            engine.save_to_file(text, wav_path)
            engine.runAndWait()
            
            # Check if file was created
            import os
            if os.path.exists(wav_path):
                print(f"Audiobook saved to: {wav_path}")
                print(f"Note: Saved as WAV format (MP3 not supported by pyttsx3)")
                return True
            else:
                print(f"File was not created. pyttsx3 may not be working properly.")
                print(f"Try using gTTS instead: python pdf_to_audiobook.py your_file.pdf")
                return False
            
        except Exception as e:
            print(f"Error during text-to-speech conversion: {str(e)}")
            print("Try using gTTS instead (it's more reliable)")
            return False
    
    def text_to_speech_espeak(self, text):
        """
        Convert text to speech using espeak-ng command line with improved quality settings
        
        Args:
            text (str): Text to convert to speech
        """
        print(f"Converting text to speech using espeak-ng (offline)...")
        print(f"Note: For better quality, wait and use gTTS later")
        
        try:
            # Check if espeak-ng is installed
            result = subprocess.run(['which', 'espeak-ng'], 
                                  capture_output=True, text=True)
            
            if result.returncode != 0:
                print("espeak-ng not found. Install it: sudo pacman -S espeak-ng")
                return False
            
            # Use WAV output
            wav_path = self.output_path if self.output_path.endswith('.wav') else self.output_path.replace('.mp3', '.wav')
            
            print(f"Generating audio file: {wav_path}")
            print(f"Using improved quality settings...")
            
            # Improved espeak-ng settings for better quality:
            # -v en-us: US English voice (clearer than default)
            # -s 160: Slightly slower speed for clarity
            # -p 50: Default pitch
            # -a 100: Amplitude/volume
            # -g 10: Word gap (slight pause between words)
            cmd = ['espeak-ng', '-v', 'en-us', '-w', wav_path, '-s', '160', '-p', '50', '-a', '100', '-g', '8']
            
            # Split text into smaller chunks to avoid potential issues
            chunk_size = 1000
            words = text.split()
            chunks = []
            current_chunk = []
            current_length = 0
            
            for word in words:
                current_chunk.append(word)
                current_length += len(word) + 1
                if current_length >= chunk_size:
                    chunks.append(' '.join(current_chunk))
                    current_chunk = []
                    current_length = 0
            
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            
            print(f"Processing {len(chunks)} text segments...")
            
            # Process all chunks into one file
            temp_wavs = []
            for i, chunk in enumerate(chunks, 1):
                print(f"   Segment {i}/{len(chunks)}...", end='\r')
                temp_wav = f"temp_espeak_{i}.wav"
                temp_cmd = cmd.copy()
                temp_cmd[temp_cmd.index('-w') + 1] = temp_wav
                
                subprocess.run(temp_cmd, input=chunk, text=True, 
                             capture_output=True, check=True)
                temp_wavs.append(temp_wav)
            
            print()
            
            # Combine WAV files if multiple chunks
            if len(temp_wavs) == 1:
                os.rename(temp_wavs[0], wav_path)
            else:
                print(f"Combining audio segments...")
                # Use sox or ffmpeg to combine
                try:
                    # Try ffmpeg first
                    with open('wav_list.txt', 'w') as f:
                        for wav in temp_wavs:
                            f.write(f"file '{wav}'\n")
                    
                    subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 
                                  'wav_list.txt', '-c', 'copy', wav_path], 
                                 check=True, capture_output=True)
                    os.remove('wav_list.txt')
                    
                except:
                    # Fallback: just use the first chunk if combining fails
                    print("Could not combine segments, using first segment only")
                    os.rename(temp_wavs[0], wav_path)
                
                # Clean up temp files
                for temp_wav in temp_wavs:
                    if os.path.exists(temp_wav):
                        os.remove(temp_wav)
            
            # Check if file was created
            if os.path.exists(wav_path):
                file_size = os.path.getsize(wav_path)
                print(f"Audiobook saved to: {wav_path}")
                print(f"File size: {file_size / 1024 / 1024:.2f} MB")
                print(f"For natural voice quality, try gTTS later: python pdf_to_audiobook.py file.pdf")
                return True
            else:
                print(f"File was not created")
                return False
            
        except subprocess.CalledProcessError as e:
            print(f"Error running espeak-ng: {str(e)}")
            if e.stderr:
                print(f"   stderr: {e.stderr}")
            return False
        except Exception as e:
            print(f"Error during text-to-speech conversion: {str(e)}")
            return False
    
    def text_to_speech_vibevoice(self, text):
        """
        Convert text to speech using Microsoft's VibeVoice-1.5B model
        High-quality neural TTS with no rate limits
        
        Args:
            text (str): Text to convert to speech
        """
        print(f"Converting text to speech using VibeVoice-1.5B (Neural TTS)...")
        print(f"Loading AI model (this may take a moment on first run)...")
        
        try:
            # Import required libraries
            try:
                import torch
                from transformers import AutoTokenizer, AutoModelForCausalLM
                import scipy.io.wavfile as wavfile
                import numpy as np
            except ImportError as e:
                print(f"Missing required libraries for VibeVoice")
                print(f"Install with: pip install torch transformers scipy numpy")
                return False
            
            # Check if model is available
            model_name = "microsoft/VibeVoice-1.5B"
            
            print(f"Loading model: {model_name}")
            print(f"First time will download ~6GB model (cached for future use)")
            
            try:
                # Load tokenizer and model
                tokenizer = AutoTokenizer.from_pretrained(model_name)
                model = AutoModelForCausalLM.from_pretrained(
                    model_name,
                    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                    device_map="auto" if torch.cuda.is_available() else "cpu"
                )
                
                device = "cuda" if torch.cuda.is_available() else "cpu"
                print(f"Using device: {device}")
                
                # Split text into manageable chunks
                max_length = 500
                words = text.split()
                chunks = []
                current_chunk = []
                
                for word in words:
                    current_chunk.append(word)
                    if len(' '.join(current_chunk)) >= max_length:
                        chunks.append(' '.join(current_chunk))
                        current_chunk = []
                
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                
                print(f"Processing {len(chunks)} text segments...")
                
                # Generate audio for each chunk
                audio_segments = []
                
                for i, chunk in enumerate(chunks, 1):
                    print(f"Generating audio for segment {i}/{len(chunks)}...", end='\r')
                    
                    # Tokenize input
                    inputs = tokenizer(chunk, return_tensors="pt").to(device)
                    
                    # Generate audio
                    with torch.no_grad():
                        outputs = model.generate(**inputs, max_length=1000)
                    
                    # Convert to audio (model-specific processing)
                    audio_data = outputs[0].cpu().numpy()
                    audio_segments.append(audio_data)
                
                print()
                
                # Combine audio segments
                print(f"Combining audio segments...")
                combined_audio = np.concatenate(audio_segments)
                
                # Save as WAV file
                wav_path = self.output_path.replace('.mp3', '.wav')
                sample_rate = 22050  # Standard sample rate for TTS
                
                wavfile.write(wav_path, sample_rate, combined_audio.astype(np.int16))
                
                print(f"Audiobook saved to: {wav_path}")
                print(f"High-quality neural TTS audio generated!")
                
                file_size = os.path.getsize(wav_path)
                print(f"File size: {file_size / 1024 / 1024:.2f} MB")
                
                return True
                
            except Exception as model_error:
                print(f"Error loading/using VibeVoice model: {str(model_error)}")
                print(f"This model requires significant resources.")
                print(f"   Alternative: Wait for gTTS rate limit to reset (1 hour)")
                return False
            
        except Exception as e:
            print(f"Error during text-to-speech conversion: {str(e)}")
            return False
    
    def text_to_speech_edge(self, text):
        """
        Convert text to speech using Microsoft Edge TTS (edge-tts)
        High-quality, no rate limits, works offline after first use
        
        Args:
            text (str): Text to convert to speech
        """
        print(f"Converting text to speech using Microsoft Edge TTS...")
        print(f"High-quality neural voice with no rate limits!")
        
        try:
            import edge_tts
        except ImportError:
            print(f"edge-tts not installed")
            print(f"Install with: pip install edge-tts")
            return False
        
        try:
            # Use asyncio to run edge-tts
            async def generate_audio():
                # Use English US voice - natural and clear
                voice = "en-US-AriaNeural"  # Female voice, very natural
                # Alternative voices:
                # "en-US-GuyNeural" - Male voice
                # "en-GB-SoniaNeural" - British female
                # "en-GB-RyanNeural" - British male
                
                communicate = edge_tts.Communicate(text, voice)
                await communicate.save(self.output_path)
            
            # Run the async function
            print(f"Using voice: en-US-AriaNeural (Natural Female Voice)")
            asyncio.run(generate_audio())
            
            # Check if file was created
            if os.path.exists(self.output_path):
                file_size = os.path.getsize(self.output_path)
                print(f"Audiobook saved to: {self.output_path}")
                print(f"File size: {file_size / 1024 / 1024:.2f} MB")
                print(f"High-quality neural voice audio generated!")
                return True
            else:
                print(f"File was not created")
                return False
            
        except Exception as e:
            print(f"Error during edge-tts conversion: {str(e)}")
            print(f"Try: python pdf_to_audiobook.py your_file.pdf -e edge")
            return False
    
    def convert(self):
        """
        Main conversion method - extracts text from PDF and converts to audio
        """
        print("=" * 60)
        print("PDF to Audiobook Converter")
        print("=" * 60)
        
        # Extract text from PDF
        text = self.extract_text_from_pdf()
        
        if not text or len(text.strip()) == 0:
            print("No text content found in the PDF")
            return False
        
        print(f"Extracted {len(text)} characters")
        
        # Clean text for better speech output
        print("Cleaning text (preserving punctuation for pauses)...")
        text = self.clean_text_for_speech(text)
        print(f"Cleaned text: {len(text)} characters")
        
        # Convert text to speech
        success = False
        if self.engine == 'gtts':
            success = self.text_to_speech_gtts(text)
        elif self.engine == 'pyttsx3':
            success = self.text_to_speech_pyttsx3(text)
        elif self.engine == 'espeak':
            success = self.text_to_speech_espeak(text)
        elif self.engine == 'vibevoice':
            success = self.text_to_speech_vibevoice(text)
        elif self.engine == 'edge':
            success = self.text_to_speech_edge(text)
        else:
            print(f"Unknown engine: {self.engine}")
            return False
        
        print("=" * 60)
        if success:
            print("Conversion completed successfully!")
        else:
            print("Conversion failed!")
        print("=" * 60)
        return success


def main():
    """
    Command-line interface for PDF to Audiobook converter
    """
    parser = argparse.ArgumentParser(
        description='Convert PDF files to audiobooks in English',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pdf_to_audiobook.py input.pdf
  python pdf_to_audiobook.py input.pdf -o output.mp3
  python pdf_to_audiobook.py input.pdf -e pyttsx3
  python pdf_to_audiobook.py input.pdf -l en-gb
        """
    )
    
    parser.add_argument('pdf_file', help='Path to the PDF file to convert')
    parser.add_argument('-o', '--output', help='Output audio file path (default: <pdf_name>_audiobook.mp3)')
    parser.add_argument('-e', '--engine', choices=['gtts', 'edge', 'espeak', 'pyttsx3', 'vibevoice'], default='gtts',
                        help='TTS engine: gtts (best, rate limited), edge (Microsoft, high quality, no limits), espeak (fast, basic), pyttsx3 (unreliable), vibevoice (not working yet)')
    parser.add_argument('-l', '--language', default='en',
                        help='Language code (default: en for English)')
    
    args = parser.parse_args()
    
    # Create converter instance and run conversion
    converter = PDFToAudiobook(
        pdf_path=args.pdf_file,
        output_path=args.output,
        engine=args.engine,
        language=args.language
    )
    
    converter.convert()


if __name__ == "__main__":
    main()
