#!/bin/bash
# Prepare and create release script

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Prepare Release${NC}                                  ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if there are uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}Uncommitted changes detected:${NC}"
    git status --short
    echo ""
    read -p "Do you want to commit these changes? (y/n): " COMMIT
    if [ "$COMMIT" = "y" ] || [ "$COMMIT" = "Y" ]; then
        echo -e "${BLUE}Staging all changes...${NC}"
        git add .
        
        echo -e "${BLUE}Enter commit message (or press Enter for default):${NC}"
        read -r COMMIT_MSG
        if [ -z "$COMMIT_MSG" ]; then
            COMMIT_MSG="feat: Add PyPI publishing and website deployment"
        fi
        
        git commit -m "$COMMIT_MSG"
        echo -e "${GREEN}✓ Changes committed${NC}"
        echo ""
    fi
fi

# Get current version
VERSION=$(python3 -c "from auto_commit import __version__; print(__version__)" 2>/dev/null || echo "unknown")
echo -e "${BLUE}Current version:${NC} ${GREEN}$VERSION${NC}"
echo ""

# Check if tag exists
if git rev-parse "v$VERSION" >/dev/null 2>&1; then
    echo -e "${YELLOW}Tag v$VERSION already exists${NC}"
    echo ""
    echo -e "${BLUE}Options:${NC}"
    echo "1. Create GitHub release for existing tag"
    echo "2. Delete and recreate tag"
    echo "3. Skip tag creation"
    echo ""
    read -p "Choose option (1/2/3): " OPTION
    
    case $OPTION in
        1)
            echo -e "${BLUE}Tag v$VERSION exists. You can create a GitHub release for it.${NC}"
            echo ""
            echo -e "${GREEN}Next steps:${NC}"
            echo "1. Go to: https://github.com/Kevrollin/gitpilot.io/releases/new?tag=v$VERSION"
            echo "2. Fill in release details"
            echo "3. Click 'Publish release'"
            echo "4. GitHub Actions will automatically publish to PyPI"
            ;;
        2)
            echo -e "${BLUE}Deleting existing tag...${NC}"
            git tag -d "v$VERSION" 2>/dev/null || true
            git push origin ":refs/tags/v$VERSION" 2>/dev/null || true
            
            echo -e "${BLUE}Creating new tag v$VERSION...${NC}"
            git tag -a "v$VERSION" -m "Release v$VERSION"
            git push origin "v$VERSION"
            echo -e "${GREEN}✓ Tag created and pushed${NC}"
            ;;
        3)
            echo -e "${BLUE}Skipping tag creation${NC}"
            ;;
    esac
else
    echo -e "${BLUE}Creating tag v$VERSION...${NC}"
    git tag -a "v$VERSION" -m "Release v$VERSION"
    git push origin "v$VERSION"
    echo -e "${GREEN}✓ Tag created and pushed${NC}"
fi

echo ""
echo -e "${BLUE}Push changes to GitHub?${NC}"
read -p "Push to origin? (y/n): " PUSH
if [ "$PUSH" = "y" ] || [ "$PUSH" = "Y" ]; then
    CURRENT_BRANCH=$(git branch --show-current)
    echo -e "${BLUE}Pushing to $CURRENT_BRANCH...${NC}"
    git push origin "$CURRENT_BRANCH"
    echo -e "${GREEN}✓ Pushed to GitHub${NC}"
fi

echo ""
echo -e "${GREEN}✓ Release preparation complete!${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo ""
echo "1. Create GitHub release:"
echo "   https://github.com/Kevrollin/gitpilot.io/releases/new?tag=v$VERSION"
echo ""
echo "2. GitHub Actions will automatically:"
echo "   - Build the package"
echo "   - Publish to PyPI"
echo ""
echo "3. Users can install with:"
echo "   pip install auto-commit-assistant"
echo ""

