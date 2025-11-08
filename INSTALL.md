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

### Option 2: Direct pip install from Git

```bash
pip install git+https://github.com/Kevrollin/gitpilot.io.git
```

### Option 3: Install from local source

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

### Command not found: autocommit

Make sure the installation completed successfully and that pip's bin directory is in your PATH:

```bash
# Check if autocommit is installed
which autocommit

# If not found, add pip's bin to PATH
export PATH="$HOME/.local/bin:$PATH"
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
```

## For Developers

If you're developing Gitpilot and want to install from a local repository:

```bash
cd /path/to/auto-commit-assistant
pip install -e .
```

This installs in "editable" mode, so changes to the code are immediately available without reinstalling.

