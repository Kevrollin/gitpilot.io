# Gitpilot Quick Start Guide

## 🚀 For Developers - Get Started in 2 Minutes

### Step 1: Install Gitpilot (Run anywhere on your machine)

**Option A: One-line install (Recommended)**
```bash
pip install git+https://github.com/Kevrollin/gitpilot.io.git
```

**Option B: Using the install script**
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install.sh | bash
```

**Where to run:** You can run this command from **any directory** - it installs Gitpilot globally on your system.

### Step 2: Set Your API Key

Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

**Option A: Environment variable (system-wide)**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

To make it permanent, add to your `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Option B: Project-specific (recommended)**
```bash
# Navigate to your project directory
cd /path/to/your/project

# Create a .env file
echo 'GEMINI_API_KEY=your-api-key-here' > .env
```

### Step 3: Use Gitpilot in Your Projects

**Navigate to any Git repository:**
```bash
cd /path/to/your/git/project
```

**Run Gitpilot:**
```bash
autocommit
```

That's it! Gitpilot will:
1. Stage all your changes
2. Generate an AI commit message
3. Let you preview/edit the message
4. Commit and push your changes

## 📝 Common Commands

```bash
# Interactive mode (recommended)
autocommit

# Auto-accept AI messages (no preview)
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

## 🔄 Keeping Gitpilot Updated

Whenever the maintainer pushes updates, developers can update with:

```bash
autocommit --update
```

This automatically pulls the latest version from the repository.

## ❓ Troubleshooting

**Command not found?**
```bash
# Add pip's bin directory to PATH
export PATH="$HOME/.local/bin:$PATH"

# Or install with --user flag
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

**Permission errors?**
```bash
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

**Need help?**
- Check the [README.md](README.md) for detailed documentation
- Check [INSTALL.md](INSTALL.md) for installation options

## 🎯 Summary

1. **Install once** (anywhere): `pip install git+https://github.com/Kevrollin/gitpilot.io.git`
2. **Set API key** (once): `export GEMINI_API_KEY="your-key"`
3. **Use in projects**: `cd your-project && autocommit`
4. **Update when needed**: `autocommit --update`

Happy committing! 🚀

