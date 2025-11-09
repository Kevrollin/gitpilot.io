#!/bin/bash
# Helper script to get direct download links from Google Drive

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Get Google Drive Direct Download Links${NC}              ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${YELLOW}How to get direct download links from Google Drive:${NC}"
echo ""
echo -e "${BLUE}Step 1: Share your files${NC}"
echo "1. Go to: https://drive.google.com"
echo "2. Right-click your file → Share"
echo "3. Change to 'Anyone with the link can view'"
echo "4. Copy the link"
echo ""

echo -e "${BLUE}Step 2: Extract File ID${NC}"
echo "Your sharing link looks like:"
echo "  https://drive.google.com/file/d/FILE_ID/view?usp=sharing"
echo ""
echo "The FILE_ID is the part between /d/ and /view"
echo ""

echo -e "${BLUE}Step 3: Convert to Direct Download Link${NC}"
echo ""
read -p "Paste your Google Drive sharing link: " DRIVE_LINK

# Extract file ID
FILE_ID=$(echo "$DRIVE_LINK" | sed -n 's/.*\/d\/\([a-zA-Z0-9_-]*\).*/\1/p')

if [ -z "$FILE_ID" ]; then
    echo -e "${YELLOW}Could not extract file ID from link${NC}"
    echo ""
    echo "Please extract the FILE_ID manually:"
    echo "  From: https://drive.google.com/file/d/FILE_ID/view"
    echo "  Copy: FILE_ID"
    echo ""
    read -p "Enter FILE_ID manually: " FILE_ID
fi

if [ -n "$FILE_ID" ]; then
    DIRECT_LINK="https://drive.google.com/uc?export=download&id=$FILE_ID"
    
    echo ""
    echo -e "${GREEN}✓ Direct download link:${NC}"
    echo "$DIRECT_LINK"
    echo ""
    echo -e "${BLUE}Use this link in your website HTML:${NC}"
    echo "<a href=\"$DIRECT_LINK\" download>Download</a>"
    echo ""
    echo -e "${BLUE}Or for pip installation:${NC}"
    echo "pip install $DIRECT_LINK"
    echo ""
else
    echo -e "${YELLOW}No file ID found${NC}"
fi

echo ""
echo -e "${BLUE}For multiple files:${NC}"
echo "1. Get sharing link for each file"
echo "2. Extract FILE_ID from each link"
echo "3. Convert using: https://drive.google.com/uc?export=download&id=FILE_ID"
echo ""

