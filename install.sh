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

# Check if pipx is available (recommended for CLI tools)
if command -v pipx &> /dev/null; then
    echo -e "${GREEN}Installing Gitpilot with pipx (recommended)...${NC}"
    echo ""
    pipx install "git+${REPO_URL}"
    INSTALL_SUCCESS=$?
elif command -v pip3 &> /dev/null || python3 -m pip --version &> /dev/null; then
    # Use pip with --user flag to avoid externally-managed-environment error
    echo -e "${GREEN}Installing Gitpilot with pip (user install)...${NC}"
    echo ""
    
    PIP_CMD=""
    if command -v pip3 &> /dev/null; then
        PIP_CMD="pip3"
    else
        PIP_CMD="python3 -m pip"
    fi
    
    # Try --user first (avoids externally-managed-environment error)
    ${PIP_CMD} install --user --upgrade --force-reinstall "git+${REPO_URL}"
    INSTALL_SUCCESS=$?
    
    if [ $INSTALL_SUCCESS -ne 0 ]; then
        echo -e "${YELLOW}User install failed. Trying with pipx...${NC}"
        echo ""
        echo "pipx is the recommended way to install Python applications."
        echo "Install pipx: sudo apt install pipx"
        echo "Then run: pipx install git+${REPO_URL}"
        echo ""
        exit 1
    fi
else
    echo -e "${YELLOW}pip is not available.${NC}"
    echo ""
    echo "Recommended: Install pipx (best for CLI tools):"
    echo "  sudo apt install pipx"
    echo "  pipx install git+${REPO_URL}"
    echo ""
    echo "Alternative: Install pip:"
    echo "  sudo apt install python3-pip"
    echo "  pip3 install --user git+${REPO_URL}"
    exit 1
fi

if [ $INSTALL_SUCCESS -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓${NC} Installation completed successfully!"
    echo ""
    
    # Check if autocommit is in PATH
    if ! command -v autocommit &> /dev/null; then
        echo -e "${YELLOW}Note: autocommit may not be in your PATH.${NC}"
        echo ""
        if command -v pipx &> /dev/null; then
            echo "If using pipx, make sure pipx's bin directory is in PATH:"
            echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
        else
            echo "Add pip's user bin directory to PATH:"
            echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
            echo "  echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
        fi
        echo ""
    fi
    
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
    if command -v pipx &> /dev/null; then
        echo "   pipx upgrade gitpilot"
    else
        echo "   autocommit --update"
    fi
    echo ""
    echo -e "${GREEN}Happy committing! 🚀${NC}"
else
    echo ""
    echo -e "${YELLOW}Error: Installation failed.${NC}"
    echo "Please check the error messages above and try again."
    exit 1
fi

