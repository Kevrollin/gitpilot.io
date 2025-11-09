#!/bin/bash
# Local installation script - Use this if the GitHub script isn't available yet
# This script can be run directly from the repository

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Google Drive file IDs
WHEEL_FILE_ID="1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg"
VERSION="1.1.1"
PACKAGE_FILE="auto_commit_assistant-${VERSION}-py3-none-any.whl"
DRIVE_URL="https://drive.google.com/uc?export=download&id=${WHEEL_FILE_ID}"

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}dev.mk - Auto Commit Assistant${NC}                     ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Local Installation Script${NC}                          ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION found"
echo ""

# Determine pip command
PIP_CMD=""
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif python3 -m pip --version &> /dev/null; then
    PIP_CMD="python3 -m pip"
else
    echo -e "${RED}Error: pip is not available.${NC}"
    exit 1
fi

# Create temporary directory
TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

# Download the package
echo -e "${BLUE}Downloading package from Google Drive...${NC}"
echo ""

if command -v curl &> /dev/null; then
    curl -L "${DRIVE_URL}" -o "${TMP_DIR}/${PACKAGE_FILE}" --progress-bar
    DOWNLOAD_SUCCESS=$?
elif command -v wget &> /dev/null; then
    wget "${DRIVE_URL}" -O "${TMP_DIR}/${PACKAGE_FILE}" --quiet --show-progress
    DOWNLOAD_SUCCESS=$?
else
    echo -e "${RED}Error: Neither curl nor wget is available.${NC}"
    exit 1
fi

if [ $DOWNLOAD_SUCCESS -ne 0 ] || [ ! -f "${TMP_DIR}/${PACKAGE_FILE}" ] || [ ! -s "${TMP_DIR}/${PACKAGE_FILE}" ]; then
    echo -e "${RED}Error: Download failed.${NC}"
    exit 1
fi

FILE_SIZE=$(ls -lh "${TMP_DIR}/${PACKAGE_FILE}" | awk '{print $5}')
echo -e "${GREEN}✓${NC} Download completed (${FILE_SIZE})"
echo ""

# Install the package
echo -e "${BLUE}Installing dev.mk...${NC}"
echo ""

INSTALL_SUCCESS=1

# Try pipx first
if command -v pipx &> /dev/null; then
    echo -e "${GREEN}Using pipx (recommended)...${NC}"
    pipx install "${TMP_DIR}/${PACKAGE_FILE}" --force && INSTALL_SUCCESS=0
fi

# If pipx failed or not available, try pip
if [ $INSTALL_SUCCESS -ne 0 ]; then
    echo -e "${GREEN}Using pip...${NC}"
    
    # Try --user first
    ${PIP_CMD} install --user "${TMP_DIR}/${PACKAGE_FILE}" 2>&1 | grep -v "externally-managed-environment" || true
    ${PIP_CMD} install --user "${TMP_DIR}/${PACKAGE_FILE}" && INSTALL_SUCCESS=0
    
    # If that fails due to externally-managed-environment, try with --break-system-packages
    if [ $INSTALL_SUCCESS -ne 0 ]; then
        echo -e "${YELLOW}Trying with --break-system-packages flag...${NC}"
        ${PIP_CMD} install --break-system-packages "${TMP_DIR}/${PACKAGE_FILE}" && INSTALL_SUCCESS=0
    fi
fi

if [ $INSTALL_SUCCESS -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓ Installation completed successfully!${NC}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Add to PATH:"
    echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo "   echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
    echo "   source ~/.bashrc"
    echo ""
    echo "2. Verify installation:"
    echo "   autocommit --version"
    echo ""
else
    echo -e "${RED}Installation failed.${NC}"
    exit 1
fi

