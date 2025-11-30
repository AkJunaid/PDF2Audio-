#!/bin/bash
# Quick setup script for PDF to Audiobook Converter

echo "🚀 Setting up PDF to Audiobook Converter..."
echo ""

# Check Python version
echo "📋 Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install system dependencies
echo ""
echo "🔊 Checking for system dependencies..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Linux detected. You may need to install espeak:"
    echo "  sudo apt-get install espeak"
    echo "  or"
    echo "  sudo yum install espeak"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "macOS detected. Speech synthesis is built-in."
fi

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "To use the converter:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run: python pdf_to_audiobook.py your_file.pdf"
echo ""
echo "For GUI version: python gui.py"
echo ""
