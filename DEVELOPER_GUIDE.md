# 📢 Share This With Your Developers

## Quick Installation Guide

Copy and paste this to share with your team:

---

### 🚀 Install Gitpilot (One-time setup)

**Recommended: Using pipx** (best for CLI tools, avoids permission issues):
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

**Alternative: Using pip with --user flag:**
```bash
# Try these in order:
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
# OR
pip3 install --user git+https://github.com/Kevrollin/gitpilot.io.git
# OR
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

**Easy way: Using the install script** (handles everything automatically):
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install.sh | bash
```

**Note:** On newer Linux systems, you may see an "externally-managed-environment" error. Use `pipx` or `--user` flag to avoid this.

### 🔑 Set Your API Key

Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

**Option 1: System-wide (recommended)**
```bash
export GEMINI_API_KEY="your-api-key-here"
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Option 2: Project-specific**
```bash
# In your project directory
echo 'GEMINI_API_KEY=your-api-key-here' > .env
```

### 💻 Use Gitpilot

Navigate to any Git repository and run:

```bash
cd /path/to/your/project
autocommit
```

That's it! Gitpilot will automatically:
- Stage all changes
- Generate AI commit messages
- Commit and push your changes

### 🔄 Update Gitpilot

When updates are available, simply run:

```bash
autocommit --update
```

---

## 📝 Quick Reference

```bash
# Interactive mode
autocommit

# Auto-accept AI messages
autocommit --yes

# Check for updates
autocommit --check-updates

# Update to latest version
autocommit --update

# Skip AI, enter manual message
autocommit --skip-ai

# Dry run (see what would happen)
autocommit --dry-run
```

## 📚 Full Documentation

- [Quick Start Guide](QUICKSTART.md)
- [Installation Guide](INSTALL.md)
- [Full README](README.md)

## ❓ Troubleshooting

**Externally-managed-environment error?**
```bash
# Use pipx (recommended - best for CLI tools)
sudo apt install pipx
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
export PATH="$HOME/.local/bin:$PATH"

# OR use --user flag
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
export PATH="$HOME/.local/bin:$PATH"
```

**pip/pip3 not found?**
```bash
# Install pip first
sudo apt install python3-pip  # Linux
brew install python3  # macOS

# Or use python3 -m pip with --user
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
export PATH="$HOME/.local/bin:$PATH"
```

**Command not found: autocommit?**
```bash
export PATH="$HOME/.local/bin:$PATH"
# Or install with --user flag
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

**Permission errors or externally-managed-environment?**
```bash
# Use pipx (best solution)
sudo apt install pipx
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
export PATH="$HOME/.local/bin:$PATH"

# OR use --user flag
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
export PATH="$HOME/.local/bin:$PATH"
```

---

**Repository:** https://github.com/Kevrollin/gitpilot.io

