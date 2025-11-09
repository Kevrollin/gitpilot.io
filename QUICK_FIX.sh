#!/bin/bash
# Quick fix for current installation issue
# Run this if you already downloaded package.whl

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}Quick Fix for dev.mk Installation${NC}"
echo ""

# Check if package.whl exists in current directory
if [ ! -f "package.whl" ]; then
    echo -e "${YELLOW}package.whl not found in current directory.${NC}"
    echo "Downloading from Google Drive..."
    curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o auto_commit_assistant-1.1.1-py3-none-any.whl
    WHEEL_FILE="auto_commit_assistant-1.1.1-py3-none-any.whl"
else
    echo -e "${GREEN}Found package.whl, renaming to correct filename...${NC}"
    mv package.whl auto_commit_assistant-1.1.1-py3-none-any.whl
    WHEEL_FILE="auto_commit_assistant-1.1.1-py3-none-any.whl"
fi

echo ""
echo -e "${BLUE}Installing dev.mk...${NC}"
echo ""

INSTALL_SUCCESS=0

# Try pipx first
if command -v pipx &> /dev/null; then
    echo -e "${GREEN}Using pipx (recommended)...${NC}"
    if pipx install "${WHEEL_FILE}" --force; then
        INSTALL_SUCCESS=1
    fi
fi

# If pipx not available or failed, try pip --user
if [ $INSTALL_SUCCESS -eq 0 ]; then
    echo -e "${GREEN}Using pip with --user flag...${NC}"
    pip install --user "${WHEEL_FILE}" && INSTALL_SUCCESS=1
fi

# If that fails, try with --break-system-packages
if [ $INSTALL_SUCCESS -eq 0 ]; then
    echo -e "${YELLOW}Trying with --break-system-packages...${NC}"
    if pip install --break-system-packages "${WHEEL_FILE}"; then
        INSTALL_SUCCESS=1
    fi
fi

if [ $INSTALL_SUCCESS -eq 1 ]; then
    echo ""
    echo -e "${GREEN}✓ Installation successful!${NC}"
    echo ""
    echo -e "${BLUE}Add to PATH:${NC}"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo "  echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
    echo "  source ~/.bashrc"
    echo ""
    echo -e "${BLUE}Verify installation:${NC}"
    echo "  autocommit --version"
    echo ""
    
    # Clean up
    rm -f "${WHEEL_FILE}"
    echo -e "${GREEN}Cleaned up downloaded file.${NC}"
else
    echo -e "${RED}Installation failed. Please check error messages above.${NC}"
    exit 1
fi

