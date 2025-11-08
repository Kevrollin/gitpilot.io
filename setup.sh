#!/bin/bash
# Quick setup script for Gitpilot - Auto Commit Assistant

set -e

echo "🚀 Setting up Gitpilot - Auto Commit Assistant"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Virtual environment created!"
echo ""
echo "📥 Installing dependencies..."
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the package
pip install -e .

echo ""
echo "✅ Installation complete!"
echo ""
echo "📝 Next steps:"
echo "1. Set your Gemini API key:"
echo "   export GEMINI_API_KEY='your-api-key-here'"
echo ""
echo "2. Activate the virtual environment (if not already active):"
echo "   source venv/bin/activate"
echo ""
echo "3. Test the installation:"
echo "   cd /path/to/your/git/repo"
echo "   autocommit"
echo ""
echo "💡 Tip: To make the API key persistent, add it to your ~/.bashrc:"
echo "   echo 'export GEMINI_API_KEY=\"your-api-key-here\"' >> ~/.bashrc"
echo "   source ~/.bashrc"

