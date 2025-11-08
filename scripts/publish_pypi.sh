#!/bin/bash
# Publish package to PyPI

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Publish dev.mk to PyPI${NC}                            ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Get version
VERSION=$(python3 -c "from auto_commit import __version__; print(__version__)" 2>/dev/null || echo "unknown")
echo -e "${BLUE}Version:${NC} ${GREEN}$VERSION${NC}"
echo ""

# Check if package is built
if [ ! -d "dist" ] || [ -z "$(ls -A dist/*.whl dist/*.tar.gz 2>/dev/null)" ]; then
    echo -e "${YELLOW}Package not built. Building now...${NC}"
    ./scripts/build_package.sh
fi

echo -e "${BLUE}Package files:${NC}"
ls -lh dist/*.whl dist/*.tar.gz 2>/dev/null || echo "No package files found"
echo ""

# Check if twine is installed
if [ -d "venv" ]; then
    source venv/bin/activate
    pip install --upgrade twine > /dev/null 2>&1
    TWINE_CMD="twine"
else
    python3 -m pip install --user --upgrade twine > /dev/null 2>&1
    TWINE_CMD="python3 -m twine"
fi

echo -e "${YELLOW}⚠️  Before publishing to PyPI:${NC}"
echo "1. Make sure you have a PyPI account: https://pypi.org/account/register/"
echo "2. Create an API token: https://pypi.org/manage/account/token/"
echo "3. Configure twine: $TWINE_CMD upload --help"
echo ""

read -p "Do you want to test upload (Test PyPI)? (y/n): " TEST_UPLOAD
if [ "$TEST_UPLOAD" = "y" ] || [ "$TEST_UPLOAD" = "Y" ]; then
    echo -e "${BLUE}Uploading to Test PyPI...${NC}"
    $TWINE_CMD upload --repository testpypi dist/*
    echo ""
    echo -e "${GREEN}✓ Uploaded to Test PyPI!${NC}"
    echo ""
    echo -e "${BLUE}Test installation:${NC}"
    echo "  pip install --index-url https://test.pypi.org/simple/ auto-commit-assistant"
    echo ""
fi

read -p "Do you want to upload to PyPI (production)? (y/n): " PROD_UPLOAD
if [ "$PROD_UPLOAD" = "y" ] || [ "$PROD_UPLOAD" = "Y" ]; then
    echo -e "${BLUE}Uploading to PyPI...${NC}"
    $TWINE_CMD upload dist/*
    echo ""
    echo -e "${GREEN}✓ Uploaded to PyPI!${NC}"
    echo ""
    echo -e "${BLUE}Users can now install with:${NC}"
    echo "  pip install auto-commit-assistant"
    echo "  pipx install auto-commit-assistant"
    echo ""
    echo -e "${BLUE}Package URL:${NC} https://pypi.org/project/auto-commit-assistant/"
fi

if [ -d "venv" ]; then
    deactivate
fi

echo ""
echo -e "${GREEN}Done! 🚀${NC}"

