# Installation Guide - dev.mk Auto Commit Assistant

This guide provides multiple ways to install dev.mk Auto Commit Assistant from Google Drive.

## 🚀 Quick Install (Recommended)

### One-Liner Installation

Copy and paste this command into your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

Or if you prefer wget:

```bash
wget -qO- https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

This will:
1. Download the installation script
2. Download the package from Google Drive
3. Install it automatically
4. Set up the `autocommit` command

### Direct Installation from Google Drive

⚠️ **Note:** pip/pipx cannot install directly from Google Drive URLs. You must download first, then install.

**Recommended: Use the installation script (handles download automatically):**
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

**Or download and install manually:**
```bash
# Download first
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o package.whl

# Then install
pip install --user package.whl
# Or with pipx
pipx install package.whl
```

## 📥 Download & Install Manually

⚠️ **Important:** pip/pipx cannot install directly from Google Drive URLs. You must download the file first, then install it.

### Step 1: Download the Package

#### Option A: Using the Download Script (Recommended)

```bash
# Download wheel file (recommended)
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/download.sh | bash

# Or download source file
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/download.sh | bash -s -- --source
```

#### Option B: Using curl/wget

```bash
# Download wheel file
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o auto_commit_assistant-1.1.1-py3-none-any.whl

# Or download source file
curl -L "https://drive.google.com/uc?export=download&id=1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL" -o auto_commit_assistant-1.1.1.tar.gz
```

#### Option C: Download from Website

Visit the website and click the download buttons for wheel or source files.

### Step 2: Install the Package

#### Install Wheel File (Recommended)

```bash
# With pip
pip install auto_commit_assistant-1.1.1-py3-none-any.whl

# Or with pipx (recommended for CLI tools)
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl
```

#### Install Source File

```bash
# With pip
pip install auto_commit_assistant-1.1.1.tar.gz

# Or with pipx
pipx install auto_commit_assistant-1.1.1.tar.gz
```

## 🔧 Installation Methods

### Method 1: Using pipx (Recommended for CLI Tools)

```bash
# Install pipx first (if not installed)
sudo apt install pipx  # Linux
brew install pipx      # macOS

# Download first (pipx cannot install directly from Google Drive URLs)
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o package.whl

# Then install
pipx install package.whl

# Add pipx to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Method 2: Using pip (User Install)

```bash
# Download first (pip cannot install directly from Google Drive URLs)
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o package.whl

# Then install
pip install --user package.whl

# Add pip's user bin to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Method 3: Using pip (System Install)

```bash
# Requires sudo (not recommended)
sudo pip install https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg
```

## ✅ Verify Installation

After installation, verify that it works:

```bash
# Check if autocommit command is available
autocommit --version

# Should output: dev.mk 1.1.1

# Show help
autocommit --help
```

## 🛠️ Troubleshooting

### Command Not Found: autocommit

If you get "command not found", add the binary directory to your PATH:

```bash
# For pipx installations
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# For pip --user installations
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Python Version Requirements

Make sure you have Python 3.8 or higher:

```bash
python3 --version
```

If not, install Python 3.8+:

```bash
# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install python3.8

# macOS
brew install python3
```

### pip Not Found

Install pip:

```bash
# Linux (Ubuntu/Debian)
sudo apt install python3-pip

# macOS
python3 -m ensurepip --upgrade
```

### Download Failed

If download fails, try:

1. Check your internet connection
2. Verify the Google Drive link is accessible
3. Try downloading from the website instead
4. Use a different method (curl vs wget)
5. Make sure the file is publicly shared on Google Drive

### Cannot Install Directly from Google Drive URL

**Error:** `HTTP error 400` or `Cannot determine package name from spec`

**Solution:** pip/pipx cannot install directly from Google Drive URLs. You must download the file first, then install it.

```bash
# ❌ This will NOT work:
pip install https://drive.google.com/uc?export=download&id=FILE_ID

# ✅ This WILL work:
curl -L "https://drive.google.com/uc?export=download&id=FILE_ID" -o package.whl
pip install package.whl
```

Or use the installation script which handles this automatically:
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

### Installation Failed

If installation fails:

1. Try with `--user` flag: `pip install --user package.whl`
2. Use pipx instead: `pipx install package.whl`
3. Check Python version: `python3 --version` (must be 3.8+)
4. Check pip version: `pip --version`
5. Try upgrading pip: `pip install --upgrade pip`

## 📦 Google Drive File IDs

Current package version: **1.1.1**

- **Wheel File ID:** `1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg`
- **Source File ID:** `1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL`

Direct download URLs:
- Wheel: `https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg`
- Source: `https://drive.google.com/uc?export=download&id=1BWRdca3IcozBTJ6h4ZRiz-piQKY06QCL`

## 🔄 Updating

To update to the latest version:

```bash
# If installed with pipx
pipx upgrade auto-commit-assistant

# If installed with pip
pip install --user --upgrade https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg

# Or use the built-in update command
autocommit --update
```

## 🎯 Quick Start

After installation:

1. Navigate to a git repository:
   ```bash
   cd /path/to/your/project
   ```

2. Run dev.mk:
   ```bash
   autocommit
   ```

3. (Optional) Set your Gemini API key:
   ```bash
   export GEMINI_API_KEY='your-api-key-here'
   echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```

## 📚 Additional Resources

- [README.md](README.md) - Full documentation
- [FAQ.md](FAQ.md) - Frequently asked questions
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Troubleshooting guide

## 💡 Tips

- Use **pipx** for CLI tools (isolated environment, no conflicts)
- Use **pip --user** to avoid permission issues
- Set your own **GEMINI_API_KEY** for unlimited usage
- Check **autocommit --help** for all available options

---

**Happy committing! 🚀**

For more information, visit: https://github.com/Kevrollin/gitpilot.io
