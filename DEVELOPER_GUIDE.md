# 📢 Share This With Your Developers

## Quick Installation Guide

Copy and paste this to share with your team:

---

### 🚀 Install Gitpilot (One-time setup)

Run this command **anywhere on your machine** (it installs globally):

```bash
# Try these in order:
pip install git+https://github.com/Kevrollin/gitpilot.io.git
# OR if 'pip' not found:
pip3 install git+https://github.com/Kevrollin/gitpilot.io.git
# OR if 'pip3' not found:
python3 -m pip install git+https://github.com/Kevrollin/gitpilot.io.git
```

**If pip is not installed:**
```bash
# Linux
sudo apt install python3-pip

# macOS
brew install python3

# Then try the install command again
```

**Alternative:** Using the install script (handles pip automatically):
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install.sh | bash
```

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

**pip/pip3 not found?**
```bash
# Install pip first
sudo apt install python3-pip  # Linux
brew install python3  # macOS

# Or use python3 -m pip (works even without pip command)
python3 -m pip install git+https://github.com/Kevrollin/gitpilot.io.git
```

**Command not found: autocommit?**
```bash
export PATH="$HOME/.local/bin:$PATH"
# Or install with --user flag
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

**Permission errors?**
```bash
python3 -m pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

---

**Repository:** https://github.com/Kevrollin/gitpilot.io

