#!/bin/bash
# Build script for creating distributable packages

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Building dev.mk Package${NC}                            ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Get version
VERSION=$(python3 -c "from auto_commit import __version__; print(__version__)" 2>/dev/null || echo "unknown")
echo -e "${BLUE}Version:${NC} ${GREEN}$VERSION${NC}"
echo ""

# Create dist directory
mkdir -p dist
echo -e "${BLUE}Cleaning old builds...${NC}"
rm -rf dist/* build/* *.egg-info

# Install build dependencies
echo -e "${BLUE}Installing build dependencies...${NC}"
if [ -d "venv" ]; then
    source venv/bin/activate
    python -m pip install --upgrade build wheel setuptools > /dev/null 2>&1 || echo "Build tools already installed"
    PYTHON_CMD=python
else
    python3 -m pip install --user --upgrade build wheel setuptools > /dev/null 2>&1 || echo "Build tools already installed"
    PYTHON_CMD=python3
fi

# Build package
echo -e "${BLUE}Building package...${NC}"
$PYTHON_CMD -m build
if [ -d "venv" ]; then
    deactivate
fi

# Check if build was successful
if [ -d "dist" ] && [ "$(ls -A dist)" ]; then
    echo -e "${GREEN}✓${NC} Package built successfully!"
    echo ""
    echo -e "${BLUE}Built files:${NC}"
    ls -lh dist/
    echo ""
    echo -e "${BLUE}Package location:${NC} ${GREEN}dist/${NC}"
    echo ""
    echo -e "${YELLOW}Next steps:${NC}"
    echo "1. Upload dist/* files to your website"
    echo "2. Update download links in your HTML page"
    echo "3. Test installation with: pip install <package-file>"
else
    echo -e "${YELLOW}Error: Build failed or no files created${NC}"
    exit 1
fi

echo -e "${GREEN}Done! 🚀${NC}"

