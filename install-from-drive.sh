#!/bin/bash
# Installation script for dev.mk Auto Commit Assistant from Google Drive
# This script downloads the package from Google Drive and installs it

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Google Drive file IDs (update these when uploading new versions)
WHEEL_FILE_ID="1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg"
SOURCE_FILE_ID="1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL"
VERSION="1.1.1"

# Package name
PACKAGE_NAME="auto-commit-assistant"
PACKAGE_FILE="auto_commit_assistant-${VERSION}-py3-none-any.whl"

# Google Drive direct download URL
DRIVE_URL="https://drive.google.com/uc?export=download&id=${WHEEL_FILE_ID}"

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}dev.mk - Auto Commit Assistant${NC}                     ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}By Kelvin Mukaria${NC}                                   ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}  Installing from Google Drive                      ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${RED}Error: Python 3.8 or higher is required.${NC}"
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi

echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION found"
echo ""

# Check if pip is available
if ! command -v pip3 &> /dev/null && ! python3 -m pip --version &> /dev/null; then
    echo -e "${RED}Error: pip is not available.${NC}"
    echo ""
    echo "Please install pip:"
    echo "  sudo apt install python3-pip  # Debian/Ubuntu"
    echo "  brew install python3          # macOS"
    exit 1
fi

# Determine pip command
PIP_CMD=""
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
else
    PIP_CMD="python3 -m pip"
fi

echo -e "${BLUE}Downloading package from Google Drive...${NC}"
echo ""

# Create temporary directory
TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

# Download the package
echo -e "${BLUE}Downloading: ${PACKAGE_FILE}${NC}"
echo -e "${BLUE}From: Google Drive${NC}"
echo ""

# Download from Google Drive using curl or wget
# Note: pip/pipx cannot install directly from Google Drive URLs, so we download first
if command -v curl &> /dev/null; then
    # Use curl with follow redirects and cookie support
    curl -L "${DRIVE_URL}" -o "${TMP_DIR}/${PACKAGE_FILE}" --progress-bar --cookie-jar "${TMP_DIR}/cookies.txt" --cookie "${TMP_DIR}/cookies.txt"
    DOWNLOAD_SUCCESS=$?
    rm -f "${TMP_DIR}/cookies.txt"
elif command -v wget &> /dev/null; then
    # Use wget with cookie handling
    wget --quiet --show-progress "${DRIVE_URL}" -O "${TMP_DIR}/${PACKAGE_FILE}" --load-cookies /dev/null --save-cookies /dev/null --keep-session-cookies
    DOWNLOAD_SUCCESS=$?
else
    echo -e "${RED}Error: Neither curl nor wget is available.${NC}"
    echo "Please install curl or wget and try again."
    exit 1
fi

if [ $DOWNLOAD_SUCCESS -ne 0 ]; then
    echo -e "${RED}Error: Download failed.${NC}"
    echo "Please check your internet connection and try again."
    exit 1
fi

# Verify download
if [ ! -f "${TMP_DIR}/${PACKAGE_FILE}" ] || [ ! -s "${TMP_DIR}/${PACKAGE_FILE}" ]; then
    echo -e "${RED}Error: Download failed or file is empty.${NC}"
    echo "Please check your internet connection and try again."
    exit 1
fi

echo -e "${GREEN}✓${NC} Download completed"
echo ""

# Check file type (wheel files are ZIP archives)
if command -v file &> /dev/null; then
    FILE_TYPE=$(file "${TMP_DIR}/${PACKAGE_FILE}" | grep -o "Zip\|gzip\|ASCII")
    if [ -z "$FILE_TYPE" ]; then
        echo -e "${YELLOW}Warning: Downloaded file may not be a valid package.${NC}"
        echo "Continuing with installation..."
    fi
fi

# Install the package
echo -e "${BLUE}Installing ${PACKAGE_NAME}...${NC}"
echo ""

# Try pipx first (recommended for CLI tools)
if command -v pipx &> /dev/null; then
    echo -e "${GREEN}Using pipx (recommended for CLI tools)...${NC}"
    pipx install "${TMP_DIR}/${PACKAGE_FILE}" --force
    INSTALL_SUCCESS=$?
    
    if [ $INSTALL_SUCCESS -eq 0 ]; then
        echo -e "${GREEN}✓${NC} Installation completed successfully!"
        echo ""
        echo -e "${BLUE}Note:${NC} Make sure pipx's bin directory is in your PATH:"
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
        echo "  echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
    fi
else
    # Use pip with --user flag
    echo -e "${GREEN}Using pip (user install)...${NC}"
    ${PIP_CMD} install --user --upgrade --force-reinstall "${TMP_DIR}/${PACKAGE_FILE}"
    INSTALL_SUCCESS=$?
    
    if [ $INSTALL_SUCCESS -eq 0 ]; then
        echo -e "${GREEN}✓${NC} Installation completed successfully!"
        echo ""
        echo -e "${BLUE}Note:${NC} Add pip's user bin directory to your PATH:"
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
        echo "  echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
    fi
fi

if [ $INSTALL_SUCCESS -ne 0 ]; then
    echo -e "${RED}Error: Installation failed.${NC}"
    echo "Please check the error messages above and try again."
    exit 1
fi

echo ""
echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Installation Complete!${NC}                              ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if autocommit is in PATH
if command -v autocommit &> /dev/null; then
    echo -e "${GREEN}✓${NC} autocommit command is available"
    echo ""
    echo -e "${BLUE}Usage:${NC}"
    echo "  autocommit              # Run in a git repository"
    echo "  autocommit --help       # Show help"
    echo "  autocommit --version    # Show version"
    echo ""
else
    echo -e "${YELLOW}⚠${NC} autocommit command not found in PATH"
    echo ""
    echo "Please add the following to your PATH:"
    if command -v pipx &> /dev/null; then
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    else
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    fi
    echo "  echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
    echo "  source ~/.bashrc"
    echo ""
    echo "Or restart your terminal."
    echo ""
fi

echo -e "${BLUE}Next steps:${NC}"
echo "1. Navigate to a git repository:"
echo "   cd /path/to/your/project"
echo ""
echo "2. Run dev.mk:"
echo "   autocommit"
echo ""
echo "3. (Optional) Set your own Gemini API key for unlimited usage:"
echo "   export GEMINI_API_KEY='your-api-key-here'"
echo "   echo 'export GEMINI_API_KEY=\"your-api-key-here\"' >> ~/.bashrc"
echo ""
echo -e "${BLUE}Note:${NC} dev.mk works out of the box with a built-in API key."
echo "Set your own key for unlimited usage and better performance."
echo ""
echo -e "${GREEN}Happy committing! 🚀${NC}"
echo ""

