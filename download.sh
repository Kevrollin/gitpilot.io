#!/bin/bash
# Download script for dev.mk Auto Commit Assistant from Google Drive
# This script downloads the package from Google Drive without installing it

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Google Drive file IDs
WHEEL_FILE_ID="1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg"
SOURCE_FILE_ID="1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL"
VERSION="1.1.1"

# Package files
WHEEL_FILE="auto_commit_assistant-${VERSION}-py3-none-any.whl"
SOURCE_FILE="auto_commit_assistant-${VERSION}.tar.gz"

# Google Drive direct download URLs
WHEEL_URL="https://drive.google.com/uc?export=download&id=${WHEEL_FILE_ID}"
SOURCE_URL="https://drive.google.com/uc?export=download&id=${SOURCE_FILE_ID}"

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}dev.mk - Auto Commit Assistant${NC}                     ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Download Package from Google Drive${NC}                ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Parse command line arguments
FILE_TYPE="wheel"  # default to wheel
OUTPUT_DIR="."

while [[ $# -gt 0 ]]; do
    case $1 in
        --wheel|-w)
            FILE_TYPE="wheel"
            shift
            ;;
        --source|-s)
            FILE_TYPE="source"
            shift
            ;;
        --output|-o)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  -w, --wheel      Download wheel file (default)"
            echo "  -s, --source     Download source file"
            echo "  -o, --output DIR Output directory (default: current directory)"
            echo "  -h, --help       Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                          # Download wheel file to current directory"
            echo "  $0 --source                 # Download source file"
            echo "  $0 --wheel --output ~/Downloads  # Download wheel to Downloads"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Create output directory if it doesn't exist
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
fi

# Determine which file to download
if [ "$FILE_TYPE" == "wheel" ]; then
    DOWNLOAD_URL="$WHEEL_URL"
    OUTPUT_FILE="${OUTPUT_DIR}/${WHEEL_FILE}"
    FILE_NAME="$WHEEL_FILE"
else
    DOWNLOAD_URL="$SOURCE_URL"
    OUTPUT_FILE="${OUTPUT_DIR}/${SOURCE_FILE}"
    FILE_NAME="$SOURCE_FILE"
fi

echo -e "${BLUE}Downloading: ${FILE_NAME}${NC}"
echo -e "${BLUE}Output: ${OUTPUT_FILE}${NC}"
echo ""

# Check for curl or wget
if command -v curl &> /dev/null; then
    echo -e "${GREEN}Using curl...${NC}"
    curl -L "${DOWNLOAD_URL}" -o "${OUTPUT_FILE}" --progress-bar
    DOWNLOAD_SUCCESS=$?
elif command -v wget &> /dev/null; then
    echo -e "${GREEN}Using wget...${NC}"
    wget "${DOWNLOAD_URL}" -O "${OUTPUT_FILE}" --progress=bar:force
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
if [ ! -f "${OUTPUT_FILE}" ] || [ ! -s "${OUTPUT_FILE}" ]; then
    echo -e "${RED}Error: Download failed or file is empty.${NC}"
    exit 1
fi

# Get file size
FILE_SIZE=$(ls -lh "${OUTPUT_FILE}" | awk '{print $5}')

echo ""
echo -e "${GREEN}✓${NC} Download completed successfully!"
echo -e "${GREEN}✓${NC} File: ${OUTPUT_FILE}"
echo -e "${GREEN}✓${NC} Size: ${FILE_SIZE}"
echo ""

# Verify file type
if command -v file &> /dev/null; then
    FILE_TYPE_INFO=$(file "${OUTPUT_FILE}")
    echo -e "${BLUE}File type:${NC} ${FILE_TYPE_INFO#*: }"
    echo ""
fi

echo -e "${BLUE}Installation:${NC}"
if [ "$FILE_TYPE" == "wheel" ]; then
    echo "  pip install ${OUTPUT_FILE}"
    echo "  # Or with pipx:"
    echo "  pipx install ${OUTPUT_FILE}"
else
    echo "  pip install ${OUTPUT_FILE}"
    echo "  # Or with pipx:"
    echo "  pipx install ${OUTPUT_FILE}"
fi
echo ""

echo -e "${GREEN}Happy committing! 🚀${NC}"
echo ""

