#!/bin/bash
# Release script for Gitpilot

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Gitpilot Release Script${NC}                              ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Get current version
CURRENT_VERSION=$(python3 -c "from auto_commit import __version__; print(__version__)" 2>/dev/null || echo "0.1.0")
echo -e "${BLUE}Current version:${NC} ${GREEN}$CURRENT_VERSION${NC}"
echo ""

# Ask for new version
read -p "Enter new version (current: $CURRENT_VERSION): " NEW_VERSION

if [ -z "$NEW_VERSION" ]; then
    echo -e "${RED}Error: Version cannot be empty${NC}"
    exit 1
fi

# Validate version format (semantic versioning)
if ! [[ "$NEW_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo -e "${YELLOW}Warning: Version doesn't follow semantic versioning (x.y.z)${NC}"
    read -p "Continue anyway? (y/n): " CONTINUE
    if [ "$CONTINUE" != "y" ] && [ "$CONTINUE" != "Y" ]; then
        exit 1
    fi
fi

# Update version in __init__.py
echo -e "${BLUE}Updating version in code...${NC}"
sed -i "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" auto_commit/__init__.py

# Verify version was updated
UPDATED_VERSION=$(python3 -c "from auto_commit import __version__; print(__version__)")
if [ "$UPDATED_VERSION" != "$NEW_VERSION" ]; then
    echo -e "${RED}Error: Failed to update version${NC}"
    exit 1
fi

echo -e "${GREEN}✓${NC} Version updated to $NEW_VERSION"
echo ""

# Ask for release notes
echo -e "${BLUE}Release Notes:${NC}"
echo "Enter release notes (press Ctrl+D when done, or leave empty):"
RELEASE_NOTES=$(cat)

# Commit changes
echo -e "${BLUE}Committing version change...${NC}"
git add auto_commit/__init__.py
git commit -m "Bump version to $NEW_VERSION" || echo "No changes to commit"

# Create tag
echo -e "${BLUE}Creating git tag v$NEW_VERSION...${NC}"
git tag -a "v$NEW_VERSION" -m "Release v$NEW_VERSION

$RELEASE_NOTES"

echo -e "${GREEN}✓${NC} Tag created: v$NEW_VERSION"
echo ""

# Get current branch name
CURRENT_BRANCH=$(git branch --show-current)
if [ -z "$CURRENT_BRANCH" ]; then
    # Fallback if --show-current is not supported
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
fi

# Ask to push
read -p "Push to GitHub? (y/n): " PUSH
if [ "$PUSH" = "y" ] || [ "$PUSH" = "Y" ]; then
    echo -e "${BLUE}Pushing to GitHub...${NC}"
    echo -e "${BLUE}Current branch: ${CURRENT_BRANCH}${NC}"
    git push origin "$CURRENT_BRANCH"
    git push origin "v$NEW_VERSION"
    echo -e "${GREEN}✓${NC} Pushed to GitHub"
    echo ""
    echo -e "${GREEN}Tag v$NEW_VERSION pushed to GitHub!${NC}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo ""
    echo -e "${YELLOW}If GitHub Actions is enabled:${NC}"
    echo "1. Wait for GitHub Actions to build and create the release"
    echo "2. Check: https://github.com/Kevrollin/gitpilot.io/actions"
    echo "3. Check: https://github.com/Kevrollin/gitpilot.io/releases"
    echo ""
    echo -e "${YELLOW}If GitHub Actions is not available:${NC}"
    echo "1. Build package: python3 -m pip install --upgrade build wheel && python3 -m build"
    echo "2. Create release manually: ./scripts/create_release_manual.sh $NEW_VERSION"
    echo "3. Or use GitHub web interface: https://github.com/Kevrollin/gitpilot.io/releases/new"
    echo "4. See MANUAL_RELEASE.md for detailed instructions"
else
    echo -e "${YELLOW}Tag created locally. Push manually with:${NC}"
    echo "  git push origin $CURRENT_BRANCH"
    echo "  git push origin v$NEW_VERSION"
fi

echo ""
echo -e "${GREEN}Done! 🚀${NC}"

