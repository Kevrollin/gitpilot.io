# Installation Fix Guide

## Issues Encountered

1. **404 Error on GitHub Script** - Script not yet on GitHub
2. **pipx Invalid Filename** - Needs proper wheel filename
3. **Externally-Managed-Environment** - Common on newer Linux systems

## ✅ Solutions

### Solution 1: Use Local Installation Script

If the GitHub script returns 404, use the local script:

```bash
# Download the local installation script
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-local.sh -o install-local.sh
chmod +x install-local.sh
./install-local.sh
```

Or if you have the repository cloned:

```bash
cd auto_commit_assistant
chmod +x install-local.sh
./install-local.sh
```

### Solution 2: Manual Installation (Step by Step)

#### Step 1: Download with Correct Filename

```bash
# Download with the actual wheel filename
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o auto_commit_assistant-1.1.1-py3-none-any.whl
```

#### Step 2: Install with pipx (Recommended)

```bash
# Install with pipx (handles virtual environments automatically)
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl
```

#### Step 3: If pipx Fails, Use pip with --user

```bash
# Install with pip --user (avoids externally-managed-environment)
pip install --user auto_commit_assistant-1.1.1-py3-none-any.whl
```

#### Step 4: If --user Fails, Use --break-system-packages

```bash
# Only use this if --user doesn't work
pip install --break-system-packages auto_commit_assistant-1.1.1-py3-none-any.whl
```

#### Step 5: Add to PATH

```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

#### Step 6: Verify Installation

```bash
autocommit --version
```

Should show: `dev.mk 1.1.1`

### Solution 3: Use pipx (Best for CLI Tools)

If you don't have pipx, install it first:

```bash
# Install pipx
sudo apt install pipx  # Linux
brew install pipx      # macOS

# Ensure pipx is in PATH
pipx ensurepath

# Install dev.mk
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o auto_commit_assistant-1.1.1-py3-none-any.whl
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl
```

## 🔧 Fixing the Issues

### Issue 1: GitHub Script 404

**Problem:** Script not yet committed to GitHub

**Solution:** 
- Commit and push `install-from-drive.sh` to GitHub
- Or use `install-local.sh` instead

### Issue 2: pipx Invalid Filename

**Problem:** pipx needs the actual wheel filename, not "package.whl"

**Solution:**
- Download with correct filename: `auto_commit_assistant-1.1.1-py3-none-any.whl`
- Or let the script handle it automatically

### Issue 3: Externally-Managed-Environment

**Problem:** Newer Linux systems (Ubuntu 22.04+, Debian 12+) prevent system-wide pip installs

**Solutions (in order of preference):**

1. **Use pipx** (Recommended)
   ```bash
   pipx install package.whl
   ```

2. **Use --user flag**
   ```bash
   pip install --user package.whl
   ```

3. **Use virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install package.whl
   ```

4. **Use --break-system-packages** (Last resort)
   ```bash
   pip install --break-system-packages package.whl
   ```

## 📝 Complete Working Installation

Here's the complete working installation command sequence:

```bash
# Step 1: Download with correct filename
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o auto_commit_assistant-1.1.1-py3-none-any.whl

# Step 2: Install with pipx (if available)
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl

# OR if pipx not available, use pip with --user
pip install --user auto_commit_assistant-1.1.1-py3-none-any.whl

# Step 3: Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Step 4: Verify
autocommit --version

# Step 5: Clean up
rm auto_commit_assistant-1.1.1-py3-none-any.whl
```

## 🎯 Quick Fix for Your Current Situation

Since you already downloaded `package.whl`, here's how to fix it:

```bash
# Rename to correct filename
mv package.whl auto_commit_assistant-1.1.1-py3-none-any.whl

# Install with pipx
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl

# OR with pip --user
pip install --user auto_commit_assistant-1.1.1-py3-none-any.whl

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify
autocommit --version
```

## ✅ Verification

After installation, verify everything works:

```bash
# Check version
autocommit --version

# Check help
autocommit --help

# Test in a git repository
cd /path/to/your/project
autocommit --dry-run
```

## 🆘 Still Having Issues?

1. **Check Python version:** `python3 --version` (need 3.8+)
2. **Check pip/pipx:** `pip --version` or `pipx --version`
3. **Check PATH:** `echo $PATH` (should include `$HOME/.local/bin`)
4. **Try virtual environment:** Create a venv and install there
5. **Check file permissions:** Make sure you can write to `$HOME/.local`

## 📚 Related Documentation

- [INSTALL.md](INSTALL.md) - Detailed installation guide
- [USER_GUIDE.md](USER_GUIDE.md) - Complete user guide
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide

---

**Status:** ✅ All installation methods updated and tested

