# Installation Instructions for Users

## Download from Google Drive

Your package is hosted on Google Drive. Users can download and install it in several ways:

## Method 1: Direct Install (Recommended)

Install directly from Google Drive without downloading first:

```bash
# Install wheel file (recommended - faster)
pip install https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg

# Or install source file
pip install https://drive.google.com/uc?export=download&id=1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL
```

## Method 2: Download Then Install

### Using curl:

```bash
# Download wheel file
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o auto_commit_assistant.whl

# Install
pip install auto_commit_assistant.whl
```

### Using wget:

```bash
# Download wheel file
wget --no-check-certificate "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -O auto_commit_assistant.whl

# Install
pip install auto_commit_assistant.whl
```

## Method 3: Using pipx (Recommended for CLI Tools)

```bash
# Download first
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o auto_commit_assistant.whl

# Install with pipx
pipx install auto_commit_assistant.whl
```

## Method 4: From Website

1. Visit your website
2. Click "Download Wheel (.whl)" button
3. Install the downloaded file:
   ```bash
   pip install auto_commit_assistant-1.1.1-py3-none-any.whl
   ```

## File Information

**Wheel File (.whl):**
- File ID: `1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg`
- Direct link: https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg
- Size: ~30KB
- Recommended for: Quick installation

**Source File (.tar.gz):**
- File ID: `1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL`
- Direct link: https://drive.google.com/uc?export=download&id=1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL
- Size: ~40KB
- Recommended for: Custom builds or inspection

## After Installation

Once installed, you can use the tool:

```bash
# Run the tool
autocommit

# Check version
autocommit --version

# Get help
autocommit --help
```

## Troubleshooting

### "pip: command not found"

Install pip first:
```bash
# Linux
sudo apt install python3-pip

# macOS
brew install python3
```

### "externally-managed-environment" error

Use pipx or --user flag:
```bash
# Using pipx (recommended)
pipx install auto_commit_assistant.whl

# Or with --user flag
pip install --user auto_commit_assistant.whl
```

### "Download failed"

- Check your internet connection
- Verify the Google Drive links are accessible
- Try downloading from the website instead

### "File not found"

- Make sure you're using the correct file ID
- Verify the files are still on Google Drive
- Check that files are publicly shared

## Verification

After installation, verify it works:

```bash
# Check if installed
which autocommit

# Check version
autocommit --version

# Should show: dev.mk 1.1.1
```

## Updating

To update to a new version:

```bash
# Uninstall old version
pip uninstall auto-commit-assistant

# Install new version
pip install https://drive.google.com/uc?export=download&id=NEW_FILE_ID
```

## Alternative: Install from GitHub

Users can also install directly from GitHub:

```bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
```

---

**Installation complete! 🚀**

For more information, visit: https://github.com/Kevrollin/gitpilot.io

