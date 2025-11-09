#!/bin/bash
# Test script to verify installation process works

echo "🧪 Testing dev.mk Installation Process"
echo "========================================"
echo ""

# Test 1: Check if download works
echo "Test 1: Testing Google Drive download..."
curl -s -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o /tmp/test_package.whl -w "HTTP Status: %{http_code}\n" | tail -1

if [ -f /tmp/test_package.whl ] && [ -s /tmp/test_package.whl ]; then
    FILE_SIZE=$(ls -lh /tmp/test_package.whl | awk '{print $5}')
    echo "✅ Download successful! File size: $FILE_SIZE"
    rm -f /tmp/test_package.whl
else
    echo "❌ Download failed!"
    exit 1
fi

echo ""

# Test 2: Check installation script syntax
echo "Test 2: Checking installation script syntax..."
if bash -n install-from-drive.sh 2>/dev/null; then
    echo "✅ Installation script syntax is valid"
else
    echo "❌ Installation script has syntax errors"
    exit 1
fi

echo ""

# Test 3: Check if Python is available
echo "Test 3: Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ $PYTHON_VERSION found"
else
    echo "⚠️  Python 3 not found (will be checked during installation)"
fi

echo ""

# Test 4: Check if pip/pipx is available
echo "Test 4: Checking pip/pipx installation..."
if command -v pipx &> /dev/null; then
    echo "✅ pipx found"
elif command -v pip3 &> /dev/null || python3 -m pip --version &> /dev/null; then
    echo "✅ pip found"
else
    echo "⚠️  pip/pipx not found (will be checked during installation)"
fi

echo ""
echo "========================================"
echo "✅ All tests passed! Installation should work."
echo ""
echo "To install, run:"
echo "  curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash"
