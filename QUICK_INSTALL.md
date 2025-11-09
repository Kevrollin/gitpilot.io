# Quick Install - dev.mk Auto Commit Assistant

## 🚀 One-Command Installation

Copy and paste this command to install dev.mk:

```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

## 📥 Download & Install from Google Drive

⚠️ **Note:** pip/pipx cannot install directly from Google Drive URLs. Download first, then install.

```bash
# Download the package
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o package.whl

# Install with pip
pip install --user package.whl

# Or with pipx (recommended)
pipx install package.whl
```

## 🔧 Add to PATH

After installation, add to PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## ✅ Verify Installation

```bash
autocommit --version
```

## 🎯 Usage

```bash
cd /path/to/your/project
autocommit
```

## 📖 More Info

For detailed installation instructions, see [INSTALL.md](INSTALL.md)

For full documentation, see [README.md](README.md)

---

**Happy committing! 🚀**

