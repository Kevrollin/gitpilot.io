#!/bin/bash
# Upload package files to Google Drive

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Upload Package to Google Drive${NC}                      ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if package is built
if [ ! -d "dist" ] || [ -z "$(ls -A dist/*.whl dist/*.tar.gz 2>/dev/null)" ]; then
    echo -e "${YELLOW}Package not built. Building now...${NC}"
    ./scripts/build_package.sh
fi

# Get version
VERSION=$(python3 -c "from auto_commit import __version__; print(__version__)" 2>/dev/null || echo "unknown")
echo -e "${BLUE}Version:${NC} ${GREEN}$VERSION${NC}"
echo ""

# Check if gdrive CLI is available
if ! command -v gdrive &> /dev/null; then
    echo -e "${YELLOW}gdrive CLI not found. Installing...${NC}"
    echo ""
    echo -e "${BLUE}Option 1: Install gdrive CLI (Recommended)${NC}"
    echo "  Visit: https://github.com/glotlabs/gdrive/releases"
    echo "  Download for your OS and install"
    echo ""
    echo -e "${BLUE}Option 2: Use Google Drive Web Interface${NC}"
    echo "  1. Go to: https://drive.google.com"
    echo "  2. Create a folder: 'dev.mk-packages'"
    echo "  3. Upload files from dist/ folder"
    echo "  4. Right-click folder → Share → Get link"
    echo "  5. Copy the folder ID from the URL"
    echo ""
    read -p "Do you want to continue with manual upload? (y/n): " CONTINUE
    if [ "$CONTINUE" != "y" ] && [ "$CONTINUE" != "Y" ]; then
        exit 0
    fi
    
    echo ""
    echo -e "${BLUE}Manual upload instructions:${NC}"
    echo ""
    echo "1. Package files are in: $(pwd)/dist/"
    echo "   - auto_commit_assistant-$VERSION-py3-none-any.whl"
    echo "   - auto_commit_assistant-$VERSION.tar.gz"
    echo ""
    echo "2. Upload to Google Drive:"
    echo "   - Go to: https://drive.google.com"
    echo "   - Create folder: 'dev.mk-packages'"
    echo "   - Upload both files"
    echo "   - Right-click folder → Share → Anyone with the link can view"
    echo ""
    echo "3. Get the folder link and update website/index.html"
    echo ""
    exit 0
fi

# Check if authenticated
if ! gdrive about &> /dev/null; then
    echo -e "${YELLOW}Not authenticated with Google Drive${NC}"
    echo ""
    echo -e "${BLUE}Authenticating...${NC}"
    echo "This will open your browser to authenticate"
    gdrive about
fi

# Create folder if it doesn't exist
FOLDER_NAME="dev.mk-packages"
FOLDER_ID=$(gdrive list --query "name = '$FOLDER_NAME' and trashed = false" --no-header --format csv 2>/dev/null | cut -d',' -f1 | head -1)

if [ -z "$FOLDER_ID" ]; then
    echo -e "${BLUE}Creating folder: $FOLDER_NAME${NC}"
    FOLDER_ID=$(gdrive mkdir "$FOLDER_NAME" --format csv --no-header 2>/dev/null | cut -d',' -f1)
    echo -e "${GREEN}✓ Folder created${NC}"
else
    echo -e "${BLUE}Using existing folder: $FOLDER_ID${NC}"
fi

# Upload files
echo ""
echo -e "${BLUE}Uploading package files...${NC}"

for file in dist/*.whl dist/*.tar.gz; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo -e "${BLUE}Uploading: $filename${NC}"
        
        # Check if file already exists
        EXISTING_ID=$(gdrive list --query "name = '$filename' and '$FOLDER_ID' in parents and trashed = false" --no-header --format csv 2>/dev/null | cut -d',' -f1 | head -1)
        
        if [ -z "$EXISTING_ID" ]; then
            gdrive upload --parent "$FOLDER_ID" "$file"
            echo -e "${GREEN}✓ Uploaded: $filename${NC}"
        else
            echo -e "${YELLOW}File exists, updating: $filename${NC}"
            gdrive update "$EXISTING_ID" "$file"
            echo -e "${GREEN}✓ Updated: $filename${NC}"
        fi
    fi
done

# Get share link
echo ""
echo -e "${BLUE}Getting share link...${NC}"
gdrive share "$FOLDER_ID" --type anyone --role reader &> /dev/null || true

# Get folder link
FOLDER_LINK="https://drive.google.com/drive/folders/$FOLDER_ID"
echo ""
echo -e "${GREEN}✓ Upload complete!${NC}"
echo ""
echo -e "${BLUE}Folder link:${NC} $FOLDER_LINK"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Make sure folder is shared: Anyone with the link can view"
echo "2. Update website/index.html with download links"
echo "3. Users can download and install with: pip install <downloaded-file>"
echo ""

