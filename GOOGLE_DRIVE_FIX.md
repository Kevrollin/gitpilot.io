# Google Drive Installation Fix

## Problem

pip/pipx cannot install directly from Google Drive URLs. When users try:
```bash
pipx install https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg
```

They get:
```
ERROR: HTTP error 400 while getting https://drive.google.com/uc?export=download
ERROR: Could not install requirement https://drive.google.com/uc?export=download
Cannot determine package name from spec
```

## Root Cause

1. Google Drive URLs with query parameters don't work well with pip/pipx
2. pip/pipx expect direct file downloads, but Google Drive may return HTML or require confirmation
3. The `&` character in URLs can cause shell parsing issues

## Solution

**Always download the file first, then install it.**

### Fixed Installation Methods

#### Method 1: Use Installation Script (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

This script:
1. Downloads the package from Google Drive using curl/wget
2. Verifies the download
3. Installs it automatically
4. Sets up PATH if needed

#### Method 2: Manual Download & Install
```bash
# Download first
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o package.whl

# Then install
pip install --user package.whl
# Or with pipx
pipx install package.whl
```

## Updated Documentation

All documentation has been updated to:
- ✅ Remove direct pip/pipx install from Google Drive URLs
- ✅ Emphasize download-then-install method
- ✅ Highlight the one-command installation script
- ✅ Add warnings about direct URL installation

## Files Updated

1. ✅ `install-from-drive.sh` - Fixed download handling
2. ✅ `INSTALL.md` - Updated all installation methods
3. ✅ `README.md` - Updated installation section
4. ✅ `QUICK_INSTALL.md` - Updated quick reference
5. ✅ `website/index.html` - Updated installation instructions

## User Instructions

Users should now:
1. Use the one-command installation script (easiest)
2. Or download manually, then install
3. Never try to install directly from Google Drive URLs with pip/pipx

## Testing

Test the installation:
```bash
# Test installation script
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash

# Test manual download
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o test.whl
pip install --user test.whl
autocommit --version
```

## Status

✅ **Fixed** - All documentation and scripts updated
✅ **Tested** - Installation script works correctly
✅ **Ready** - Users can now install successfully

---

**Date:** $(date)
**Issue:** pip/pipx cannot install directly from Google Drive URLs
**Solution:** Download first, then install

