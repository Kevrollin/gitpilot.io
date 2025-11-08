#!/bin/bash
# Script to push v1.1.1 release to GitHub

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Push Release v1.1.1 to GitHub${NC}                       ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
if [ -z "$CURRENT_BRANCH" ]; then
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
fi

echo -e "${BLUE}Current branch:${NC} ${GREEN}$CURRENT_BRANCH${NC}"
echo -e "${BLUE}Tag to push:${NC} ${GREEN}v1.1.1${NC}"
echo ""

# Check if tag exists
if ! git tag -l "v1.1.1" | grep -q "v1.1.1"; then
    echo -e "${YELLOW}Error: Tag v1.1.1 not found${NC}"
    exit 1
fi

echo -e "${BLUE}Pushing to GitHub...${NC}"
echo ""

# Push branch
echo -e "${BLUE}1. Pushing branch $CURRENT_BRANCH...${NC}"
git push origin "$CURRENT_BRANCH"

# Push tag
echo -e "${BLUE}2. Pushing tag v1.1.1...${NC}"
git push origin v1.1.1

echo ""
echo -e "${GREEN}✓ Release v1.1.1 pushed to GitHub!${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo ""
echo -e "${YELLOW}If GitHub Actions is enabled:${NC}"
echo "1. Wait for GitHub Actions to build and create the release"
echo "2. Check: https://github.com/Kevrollin/gitpilot.io/actions"
echo "3. Check: https://github.com/Kevrollin/gitpilot.io/releases"
echo ""
echo -e "${YELLOW}If GitHub Actions is not available:${NC}"
echo "1. Go to: https://github.com/Kevrollin/gitpilot.io/releases/new"
echo "2. Select tag: v1.1.1"
echo "3. Title: Release v1.1.1 - API Key Error Handling Improvements"
echo "4. Description: See RELEASE_V1.1.1.md for details"
echo "5. Build and attach package files if needed"
echo ""
echo -e "${GREEN}Done! 🚀${NC}"

