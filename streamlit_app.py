#!/usr/bin/env python3
"""
Streamlit Web Interface for PDF to Audiobook Converter
Upload PDF files, convert to audiobook, and download the result
"""

import streamlit as st
import os
import tempfile
from pathlib import Path
from pdf_to_audiobook import PDFToAudiobook
import time

# Page configuration
st.set_page_config(
    page_title="PDF to Audiobook Converter",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1E88E5;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px;
        border-radius: 8px;
        border: none;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .success-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 20px 0;
    }
    .info-box {
        padding: 15px;
        border-radius: 8px;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        margin: 15px 0;
    }
    .warning-box {
        padding: 15px;
        border-radius: 8px;
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">PDF to Audiobook Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Transform your PDF documents into high-quality audiobooks</div>', unsafe_allow_html=True)

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    
    # Engine selection - Only Edge TTS
    engine = "edge"
    language = "en"  # Default to English (US)
    
    st.info("Microsoft Edge TTS - High quality neural voices with no rate limits")
    
    st.markdown("---")
    
    # About section
    st.header("About")
    st.write("""
    This tool converts PDF documents into audiobooks using advanced text-to-speech technology.
    
    **Features:**
    - Multiple TTS engines
    - High-quality audio output
    - Support for various accents
    - Easy drag-and-drop interface
    """)
    
    st.markdown("---")
    st.caption("AK Junaid")

# Main content area
st.markdown("### Upload Your PDF")

# File uploader with drag and drop
uploaded_file = st.file_uploader(
    "Drag and drop your PDF file here or click to browse",
    type=['pdf'],
    help="Upload a PDF file to convert to audiobook"
)

# Display file info if uploaded
if uploaded_file is not None:
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**File size:** {uploaded_file.size / 1024:.2f} KB")
    with col2:
        st.success("File loaded")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Convert button
    if st.button("Convert to Audiobook", key="convert_btn"):
        
        # Create temporary directory for processing
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save uploaded PDF to temp file
            pdf_path = os.path.join(temp_dir, uploaded_file.name)
            with open(pdf_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            
            # Determine output path
            pdf_name = Path(uploaded_file.name).stem
            extension = '.mp3'
            output_path = os.path.join(temp_dir, f"{pdf_name}_audiobook{extension}")
            
            # Progress indicators
            st.markdown("---")
            st.markdown("### Converting...")
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Update progress - extracting text
                progress_bar.progress(10)
                status_text.text("Extracting text from PDF...")
                time.sleep(0.5)
                
                # Create converter instance
                converter = PDFToAudiobook(
                    pdf_path=pdf_path,
                    output_path=output_path,
                    engine=engine,
                    language=language
                )
                
                # Extract text
                text = converter.extract_text_from_pdf()
                
                if not text or len(text.strip()) == 0:
                    st.error("No text content found in the PDF")
                    st.stop()
                
                progress_bar.progress(30)
                status_text.text(f"Extracted {len(text)} characters")
                time.sleep(0.5)
                
                # Clean text
                progress_bar.progress(40)
                status_text.text("Cleaning and processing text...")
                cleaned_text = converter.clean_text_for_speech(text)
                time.sleep(0.5)
                
                # Convert to speech
                progress_bar.progress(50)
                status_text.text("Converting text to speech using Microsoft Edge TTS... (this may take a while)")
                
                # Perform conversion using Edge TTS
                success = converter.text_to_speech_edge(cleaned_text)
                
                progress_bar.progress(90)
                
                if success and os.path.exists(output_path):
                    progress_bar.progress(100)
                    status_text.text("Conversion completed successfully!")
                    
                    # Success message
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown("### Your audiobook is ready!")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # File info
                    file_size = os.path.getsize(output_path)
                    st.write(f"**Output file:** {os.path.basename(output_path)}")
                    st.write(f"**File size:** {file_size / 1024 / 1024:.2f} MB")
                    
                    # Read the audio file
                    with open(output_path, 'rb') as audio_file:
                        audio_bytes = audio_file.read()
                    
                    # Audio player
                    st.audio(audio_bytes, format=f'audio/{extension[1:]}')
                    
                    # Download button
                    st.download_button(
                        label="Download Audiobook",
                        data=audio_bytes,
                        file_name=os.path.basename(output_path),
                        mime=f'audio/{extension[1:]}',
                        key="download_btn"
                    )
                    
                else:
                    st.error("Conversion failed. Please check your internet connection and try again.")
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.exception(e)
                
else:
    # Instructions when no file is uploaded
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    ### How to use:
    1. **Upload** a PDF file using the file uploader above
    2. **Configure** settings in the sidebar (optional)
    3. **Click** the "Convert to Audiobook" button
    4. **Wait** for the conversion to complete
    5. **Download** your audiobook!
    
    **Note:** Conversion time depends on:
    - PDF length (number of pages)
    - Internet connection speed
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p><b>Tips:</b> For best results, use PDFs with clear text content. Scanned PDFs may not work properly.</p>
        <p>Your files are processed securely and are not stored on our servers.</p>
    </div>
""", unsafe_allow_html=True)
