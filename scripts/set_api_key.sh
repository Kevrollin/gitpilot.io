#!/bin/bash
# Script to set API key securely for building releases

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}  ${GREEN}dev.mk - API Key Setup${NC}                              ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if API key is provided as argument
if [ -z "$1" ]; then
    echo -e "${YELLOW}Usage: $0 <your-gemini-api-key>${NC}"
    echo ""
    echo "This will:"
    echo "1. Set DEV_MK_GEMINI_API_KEY environment variable"
    echo "2. Build the package with the key embedded"
    echo "3. Create a release with the key included"
    echo ""
    echo -e "${RED}⚠️  WARNING:${NC} This key will be embedded in the built package."
    echo "Only use this if you're okay with the key being in distribution files."
    echo ""
    read -p "Enter your Gemini API key: " API_KEY
else
    API_KEY=$1
fi

if [ -z "$API_KEY" ]; then
    echo -e "${RED}Error: API key cannot be empty${NC}"
    exit 1
fi

echo -e "${BLUE}Setting API key...${NC}"
export DEV_MK_GEMINI_API_KEY="$API_KEY"

# Update the ai.py file to include the key (temporary for build)
echo -e "${BLUE}Updating code with API key...${NC}"
cd "$(dirname "$0")/.."

# Create a temporary version of ai.py with the key
sed "s|DEFAULT_API_KEY = os.getenv(\"DEV_MK_GEMINI_API_KEY\", \"\")|DEFAULT_API_KEY = os.getenv(\"DEV_MK_GEMINI_API_KEY\", \"$API_KEY\")|" auto_commit/ai.py > auto_commit/ai.py.tmp
mv auto_commit/ai.py.tmp auto_commit/ai.py

echo -e "${GREEN}✓${NC} API key set"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Build the package: python3 -m build"
echo "2. Create release: ./scripts/release.sh"
echo ""
echo -e "${YELLOW}Note:${NC} The API key is now in the code. Make sure to:"
echo "- Test the build works"
echo "- Create the release"
echo "- Consider reverting the key after release (for security)"

