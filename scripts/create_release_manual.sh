#!/bin/bash
# Manual release creation script (when GitHub Actions is not available)

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Gitpilot Manual Release Creator${NC}                      ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Get version from tag
if [ -z "$1" ]; then
    echo -e "${YELLOW}Usage: $0 <version>${NC}"
    echo "Example: $0 0.1.2"
    exit 1
fi

VERSION=$1
TAG="v$VERSION"

# Check if tag exists
if ! git rev-parse "$TAG" >/dev/null 2>&1; then
    echo -e "${RED}Error: Tag $TAG does not exist${NC}"
    echo "Create the tag first with: git tag -a $TAG -m 'Release $TAG'"
    exit 1
fi

echo -e "${BLUE}Creating release for version:${NC} ${GREEN}$VERSION${NC}"
echo ""

# Build the package
echo -e "${BLUE}Building package...${NC}"
python3 -m pip install --upgrade build wheel
python3 -m build

if [ ! -d "dist" ]; then
    echo -e "${RED}Error: dist directory not found${NC}"
    exit 1
fi

echo -e "${GREEN}✓${NC} Package built successfully"
echo ""

# Create release notes
echo -e "${BLUE}Release Notes:${NC}"
echo "Enter release notes for this version (press Ctrl+D when done):"
RELEASE_NOTES=$(cat)

# Check if GitHub CLI is installed
if command -v gh &> /dev/null; then
    echo -e "${BLUE}Using GitHub CLI to create release...${NC}"
    
    gh release create "$TAG" \
        --title "Release $TAG" \
        --notes "$RELEASE_NOTES" \
        dist/*.whl dist/*.tar.gz
    
    echo -e "${GREEN}✓${NC} Release created with GitHub CLI"
else
    echo -e "${YELLOW}GitHub CLI not found. Creating release manually...${NC}"
    echo ""
    echo -e "${BLUE}To create the release:${NC}"
    echo "1. Go to: https://github.com/Kevrollin/gitpilot.io/releases/new"
    echo "2. Select tag: $TAG"
    echo "3. Title: Release $TAG"
    echo "4. Description:"
    echo "$RELEASE_NOTES"
    echo ""
    echo -e "${BLUE}Upload these files:${NC}"
    ls -lh dist/
    echo ""
    echo -e "${BLUE}Or install GitHub CLI and run:${NC}"
    echo "  sudo apt install gh  # Linux"
    echo "  brew install gh      # macOS"
    echo "  gh auth login"
    echo "  gh release create $TAG --title 'Release $TAG' --notes '$RELEASE_NOTES' dist/*.whl dist/*.tar.gz"
fi

echo ""
echo -e "${GREEN}Done! 🚀${NC}"

