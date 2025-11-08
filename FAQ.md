# Frequently Asked Questions (FAQ)

## Environment Variables

### How do I remove GEMINI_API_KEY?

**Quick answer:**
```bash
unset GEMINI_API_KEY
```

**If set permanently in ~/.bashrc or ~/.zshrc:**
```bash
# Remove from ~/.bashrc
sed -i '/GEMINI_API_KEY/d' ~/.bashrc
source ~/.bashrc

# Remove from ~/.zshrc
sed -i '/GEMINI_API_KEY/d' ~/.zshrc
source ~/.zshrc
```

**If in .env file:**
```bash
rm .env
# Or edit the file to remove the line
```

See [ENV_VARIABLE_GUIDE.md](ENV_VARIABLE_GUIDE.md) for detailed instructions.

## Updates

### Do I need to reinstall when you release updates?

**Yes, you need to update/reinstall to get new versions.**

**Why:**
- When you install, you get a specific version of the code
- New updates are in the repository, not in your installed version
- You need to fetch and install the new version

**How to update:**

**If installed with pipx:**
```bash
pipx upgrade auto-commit-assistant
```

**If installed with pip:**
```bash
autocommit --update
# Or manually
pip install --user --upgrade git+https://github.com/Kevrollin/gitpilot.io.git
```

**Just running `autocommit`** will use your currently installed version - you won't get updates automatically.

See [UPDATE_GUIDE.md](UPDATE_GUIDE.md) for detailed instructions.

### Will `autocommit --update` work with pipx?

**It depends.** The `autocommit --update` command now detects pipx installations and uses `pipx upgrade` automatically. However, if it fails, you can manually update:

```bash
pipx upgrade auto-commit-assistant
```

### How do I know if there's an update available?

```bash
autocommit --check-updates
```

This will tell you if a new version is available.

## Installation

### Do I need to set an API key?

**No!** dev.mk works out of the box with a built-in API key. You can use it immediately after installation.

**Optional:** Set your own key for unlimited usage:
```bash
export GEMINI_API_KEY='your-key-here'
```

### Which installation method should I use?

**Recommended: pipx** (best for CLI tools)
```bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
```

**Alternative: pip with --user**
```bash
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

## Usage

### Can I use it in any git repository?

Yes! Just navigate to any git repository and run:
```bash
autocommit
```

### Does it work with private repositories?

Yes, it works with both public and private git repositories.

### What if I don't like the AI-generated commit message?

You can:
1. **Edit it inline** - choose option 2 when prompted
2. **Edit in editor** - choose option 3 to open in your editor
3. **Enter manual message** - choose option 4 to write your own
4. **Skip AI** - use `autocommit --skip-ai` flag

## Troubleshooting

### Command not found: autocommit

Make sure the installation completed and add to PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Externally-managed-environment error

Use pipx or --user flag:
```bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
# Or
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

### API key errors

dev.mk has a built-in key, so this shouldn't happen. If you see API key errors:
1. Check your internet connection
2. Try setting your own key: `export GEMINI_API_KEY='your-key'`
3. Check the logs for detailed error messages

### Update fails

**If using pipx:**
```bash
pipx upgrade auto-commit-assistant
```

**If using pip:**
```bash
pip install --user --upgrade --force-reinstall git+https://github.com/Kevrollin/gitpilot.io.git
```

## General

### Who created this?

**dev.mk** by **Kelvin Mukaria**

### Is it free to use?

Yes! The tool is free and open-source. The built-in API key has rate limits. For unlimited usage, set your own API key.

### Where can I get help?

- **GitHub Issues**: https://github.com/Kevrollin/gitpilot.io/issues
- **Documentation**: See README.md and other guide files
- **Troubleshooting**: See TROUBLESHOOTING.md

### Can I contribute?

Yes! Contributions are welcome. See the repository for details.

---

For more detailed guides, see:
- [ENV_VARIABLE_GUIDE.md](ENV_VARIABLE_GUIDE.md) - Managing environment variables
- [UPDATE_GUIDE.md](UPDATE_GUIDE.md) - Updating dev.mk
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues and solutions

