#!/bin/bash
# Installation script for Gitpilot Auto Commit Assistant

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default repository URL
REPO_URL="${GITPILOT_REPO_URL:-https://github.com/Kevrollin/gitpilot.io.git}"

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}Gitpilot - Auto Commit Assistant${NC}                    ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}  AI-Powered Git Automation                          ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Error: Python 3 is required but not installed.${NC}"
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${YELLOW}Error: Python 3.8 or higher is required.${NC}"
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi

echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION found"
echo ""

# Check if pip is available (either as command or as python module)
PIP_CMD=""
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif python3 -m pip --version &> /dev/null; then
    PIP_CMD="python3 -m pip"
else
    echo -e "${YELLOW}pip is not installed. Installing pip...${NC}"
    echo ""
    
    # Try to install pip using ensurepip (comes with Python 3.4+)
    if python3 -m ensurepip --upgrade &> /dev/null; then
        echo -e "${GREEN}✓${NC} pip installed using ensurepip"
        PIP_CMD="python3 -m pip"
    else
        echo -e "${YELLOW}Could not install pip automatically.${NC}"
        echo ""
        echo "Please install pip manually:"
        echo "  sudo apt install python3-pip"
        echo ""
        echo "Or on macOS:"
        echo "  brew install python3"
        echo ""
        echo "Then run this script again."
        exit 1
    fi
fi

echo -e "${GREEN}Installing Gitpilot...${NC}"
echo ""

# Install from git repository
${PIP_CMD} install --upgrade --force-reinstall "git+${REPO_URL}"

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓${NC} Installation completed successfully!"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Set your Gemini API key:"
    echo "   export GEMINI_API_KEY='your-api-key-here'"
    echo ""
    echo "2. Or create a .env file in your project:"
    echo "   echo 'GEMINI_API_KEY=your-api-key-here' > .env"
    echo ""
    echo "3. Use Gitpilot in any git repository:"
    echo "   autocommit"
    echo ""
    echo -e "${BLUE}To update Gitpilot in the future, run:${NC}"
    echo "   autocommit --update"
    echo ""
    echo -e "${GREEN}Happy committing! 🚀${NC}"
else
    echo ""
    echo -e "${YELLOW}Error: Installation failed.${NC}"
    echo "Please check the error messages above and try again."
    exit 1
fi

