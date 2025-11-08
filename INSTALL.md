# Gitpilot Installation & Update Guide

## Quick Install

### Option 1: Install Script (Recommended)

```bash
# Download and run the install script
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install.sh | bash
```

Or manually:

```bash
chmod +x install.sh
./install.sh
```

### Option 2: Using pipx (Recommended for CLI tools)

```bash
# Install pipx first
sudo apt install pipx  # Linux
brew install pipx      # macOS

# Install Gitpilot
pipx install git+https://github.com/Kevrollin/gitpilot.io.git

# Add to PATH (if not already)
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Option 3: Direct pip install from Git (with --user flag)

```bash
# Try these in order (--user flag avoids permission issues):
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
# OR
pip3 install --user git+https://github.com/Kevrollin/gitpilot.io.git
# OR
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

**If pip is not installed:**
```bash
# Linux
sudo apt install python3-pip

# macOS
brew install python3

# Windows (if using Python from python.org)
python -m ensurepip --upgrade
```

### Option 4: Install from local source

```bash
cd auto_commit_assistant
pip install -e .
```

## Update Gitpilot

### Automatic Update

Simply run:

```bash
autocommit --update
```

This will automatically:
- Check the repository for updates
- Download and install the latest version
- Update all dependencies

### Check for Updates

To check if updates are available without installing:

```bash
autocommit --check-updates
```

### Manual Update

If you installed from git, you can update manually:

```bash
pip install --upgrade --force-reinstall git+https://github.com/Kevrollin/gitpilot.io.git
```

## Configuration

### Set Repository URL (for updates)

If you're using a custom repository or private repo, set the environment variable:

```bash
export GITPILOT_REPO_URL="https://github.com/Kevrollin/gitpilot.io.git"
```

Or add it to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
echo 'export GITPILOT_REPO_URL="https://github.com/Kevrollin/gitpilot.io.git"' >> ~/.bashrc
source ~/.bashrc
```

### Set API Key

Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey) and set it:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Or create a `.env` file in your project:

```bash
echo 'GEMINI_API_KEY=your-api-key-here' > .env
```

## Usage After Installation

Once installed, use Gitpilot in any git repository:

```bash
# Interactive mode
autocommit

# Auto-accept AI messages
autocommit --yes

# Check for updates
autocommit --check-updates

# Update to latest version
autocommit --update
```

## Troubleshooting

### Externally-managed-environment error

If you see "externally-managed-environment" error (common on Ubuntu 22.04+, Debian 12+):

**Solution 1: Use pipx (Recommended)**
```bash
sudo apt install pipx
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
export PATH="$HOME/.local/bin:$PATH"
```

**Solution 2: Use --user flag**
```bash
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
export PATH="$HOME/.local/bin:$PATH"
```

**Solution 3: Use pipx (via install script)**
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install.sh | bash
```

### Command not found: pip

If you get `pip: command not found`, try:

```bash
# Linux
sudo apt install python3-pip

# macOS
brew install python3

# Or use python3 -m pip instead
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

### Command not found: autocommit

Make sure the installation completed successfully and that pip's bin directory is in your PATH:

```bash
# Check if autocommit is installed
which autocommit

# If not found, add pip's bin to PATH
export PATH="$HOME/.local/bin:$PATH"

# Or reinstall with --user flag
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

### Update fails

If updates fail, try:

```bash
# Uninstall and reinstall
pip uninstall auto-commit-assistant
pip install git+https://github.com/Kevrollin/gitpilot.io.git
```

### Permission errors

If you get permission errors, use `--user` flag:

```bash
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
# OR
pip3 install --user git+https://github.com/Kevrollin/gitpilot.io.git
# OR
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

## For Developers

If you're developing Gitpilot and want to install from a local repository:

```bash
cd /path/to/auto-commit-assistant
pip install -e .
```

This installs in "editable" mode, so changes to the code are immediately available without reinstalling.

