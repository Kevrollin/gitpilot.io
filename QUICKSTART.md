# Quick Start Guide - dev.mk Auto Commit Assistant

Get started in 5 minutes! 🚀

## ⚡ Quick Installation

### Step 1: Install (1 command)

```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

Wait for it to complete (takes about 1-2 minutes).

### Step 2: Verify Installation

```bash
autocommit --version
```

Should show: `dev.mk 1.1.1`

**If you see "command not found":**
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Step 3: Use It!

```bash
# Go to your project
cd /path/to/your/project

# Make some changes (edit files, create files, etc.)

# Run dev.mk
autocommit
```

That's it! 🎉

---

## 📝 What Happens Next?

1. **dev.mk stages all your changes**
2. **Analyzes what you changed**
3. **Generates an AI commit message**
4. **Shows you a preview**
5. **You accept, edit, or write your own message**
6. **Commits and pushes automatically**

---

## 🎯 Common Commands

```bash
autocommit                  # Interactive mode
autocommit --yes            # Auto-accept AI message
autocommit --dry-run        # Test without committing
autocommit --skip-ai        # Manual commit message
autocommit --help           # Show all options
```

---

## 🔧 Optional: Set API Key

For unlimited usage, set your Gemini API key:

```bash
export GEMINI_API_KEY='your-api-key-here'
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
```

Get your key from: https://makersuite.google.com/app/apikey

**Note:** dev.mk works without an API key (uses built-in key), but setting your own gives you unlimited usage.

---

## 🆘 Having Issues?

### Installation Problems?

1. **Check Python:** `python3 --version` (need 3.8+)
2. **Check pip:** `pip --version` or `pip3 --version`
3. **Try manual install:** See [INSTALL.md](INSTALL.md)

### Usage Problems?

1. **"command not found":** Add to PATH (see Step 2 above)
2. **"Not a git repository":** Run `git init` first
3. **"No changes":** Make some changes to files first

### Need More Help?

- **Full Guide:** See [USER_GUIDE.md](USER_GUIDE.md)
- **Installation:** See [INSTALL.md](INSTALL.md)
- **Troubleshooting:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## ✅ Checklist

- [ ] Installed dev.mk
- [ ] Verified installation (`autocommit --version`)
- [ ] Added to PATH (if needed)
- [ ] Set API key (optional)
- [ ] Tested in a project
- [ ] Ready to use!

---

**That's it! You're ready to use dev.mk! 🎉**

For detailed instructions, see [USER_GUIDE.md](USER_GUIDE.md)
