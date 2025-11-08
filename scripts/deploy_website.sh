#!/bin/bash
# Deploy website script

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Deploy dev.mk Website${NC}                            ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Get version
VERSION=$(python3 -c "from auto_commit import __version__; print(__version__)" 2>/dev/null || echo "unknown")
echo -e "${BLUE}Version:${NC} ${GREEN}$VERSION${NC}"
echo ""

# Build package
echo -e "${BLUE}Step 1: Building package...${NC}"
./scripts/build_package.sh

# Copy files to website
echo -e "${BLUE}Step 2: Copying files to website...${NC}"
mkdir -p website/dist
cp dist/* website/dist/ 2>/dev/null || echo "No files to copy"

echo -e "${GREEN}✓${NC} Files copied to website/dist/"
echo ""

# Update version in HTML (simple sed replacement)
if [ -f "website/index.html" ]; then
    echo -e "${BLUE}Step 3: Updating version in HTML...${NC}"
    sed -i "s/id=\"version\">v[0-9.]*/id=\"version\">v$VERSION/g" website/index.html
    sed -i "s/auto_commit_assistant-[0-9.]*-py3-none-any.whl/auto_commit_assistant-$VERSION-py3-none-any.whl/g" website/index.html
    sed -i "s/auto_commit_assistant-[0-9.]*.tar.gz/auto_commit_assistant-$VERSION.tar.gz/g" website/index.html
    echo -e "${GREEN}✓${NC} Version updated in HTML"
fi

echo ""
echo -e "${BLUE}Step 4: Ready to deploy!${NC}"
echo ""
echo -e "${YELLOW}Deployment options:${NC}"
echo ""
echo -e "${BLUE}Option 1: GitHub Pages${NC}"
echo "  git checkout -b gh-pages"
echo "  git add website/"
echo "  git commit -m 'Deploy website'"
echo "  git push origin gh-pages"
echo ""
echo -e "${BLUE}Option 2: Netlify${NC}"
echo "  cd website"
echo "  netlify deploy --prod"
echo ""
echo -e "${BLUE}Option 3: Vercel${NC}"
echo "  cd website"
echo "  vercel --prod"
echo ""
echo -e "${BLUE}Option 4: Local server (testing)${NC}"
echo "  cd website"
echo "  python3 -m http.server 8000"
echo "  Then visit: http://localhost:8000"
echo ""

echo -e "${GREEN}Done! 🚀${NC}"

