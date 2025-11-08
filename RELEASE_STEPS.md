# 🚀 Create Release v0.1.3 on GitHub - Step by Step

## ✅ Pre-flight Checklist

- [x] Version updated to 0.1.3
- [x] API key added to code
- [x] Branding updated (dev.mk, Kelvin Mukaria)
- [x] Package built successfully
- [x] Distribution files ready in `dist/` folder

## 📦 Files Ready for Upload

You have these files ready:
- `auto_commit_assistant-0.1.3-py3-none-any.whl` (27 KB)
- `auto_commit_assistant-0.1.3.tar.gz` (33 KB)

Location: `/home/miss-royalty/Kev.Projects/Niru-hackathon/jambosec.ai/auto_commit_assistant/dist/`

## 🎯 Step-by-Step: Create Release on GitHub

### Step 1: Open GitHub Releases Page

1. Open your browser
2. Go to: **https://github.com/Kevrollin/gitpilot.io/releases**
3. Click the **"Draft a new release"** button (green button, top right)

### Step 2: Choose Tag

1. Click **"Choose a tag"** dropdown (or click the input field)
2. Type: `v0.1.3`
3. Since this tag doesn't exist yet, GitHub will show: **"Create new tag: v0.1.3 on publish"**
4. Click on that option
5. Select target branch: **`master`** (should be default)

### Step 3: Release Title

Enter:
```
Release v0.1.3 - dev.mk by Kelvin Mukaria
```

### Step 4: Release Description

Copy and paste this:

```markdown
## dev.mk v0.1.3

**By Kelvin Mukaria**

### 🎉 What's New

- ✨ **No API key required!** Works out of the box with built-in API key
- 🎨 **Updated branding** to dev.mk by Kelvin Mukaria
- 🚀 **Instant setup** - just install and use
- 🔧 Users can still set their own key for unlimited usage

### 📦 Installation

**Using pipx (Recommended):**
```bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3
```

**Using pip:**
```bash
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3
```

**Using install script:**
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/v0.1.3/install.sh | bash
```

### 💻 Usage

```bash
# Works immediately - no API key needed!
autocommit

# Optional: Set your own key for unlimited usage
export GEMINI_API_KEY='your-key-here'
autocommit
```

### 📝 What's Changed

- Built-in API key for instant use
- Updated branding to dev.mk
- Simplified installation process
- Improved user experience

### 🔗 Links

- **Repository**: https://github.com/Kevrollin/gitpilot.io
- **Documentation**: https://github.com/Kevrollin/gitpilot.io#readme
- **Issues**: https://github.com/Kevrollin/gitpilot.io/issues

---

**Enjoy committing! 🚀**
```

### Step 5: Attach Files

1. Scroll down to the **"Attach binaries by dropping them here or selecting them"** section
2. Click **"selecting them"** (or drag and drop)
3. Navigate to: `/home/miss-royalty/Kev.Projects/Niru-hackathon/jambosec.ai/auto_commit_assistant/dist/`
4. Select these **2 files**:
   - ✅ `auto_commit_assistant-0.1.3-py3-none-any.whl`
   - ✅ `auto_commit_assistant-0.1.3.tar.gz`
5. Wait for upload to complete (you'll see checkmarks)

### Step 6: Review and Publish

1. **Review everything:**
   - ✅ Tag: `v0.1.3`
   - ✅ Title: "Release v0.1.3 - dev.mk by Kelvin Mukaria"
   - ✅ Description looks good
   - ✅ 2 files attached
   - ✅ Branch: `master`

2. **Click "Publish release"** (green button at bottom)

### Step 7: Verify Release

After publishing, you should see:
- ✅ Release page with all details
- ✅ 2 assets attached (wheel + source)
- ✅ Tag created (`v0.1.3`)
- ✅ Release is live

### Step 8: Test Installation

Test that it works:

```bash
# Install from the release
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3

# Test it works
autocommit --version
# Should show: dev.mk 0.1.3

# Test it works without API key
cd /path/to/your/git/repo
autocommit --dry-run
```

## 🎉 Done!

Your release is now live! Users can install and use dev.mk without setting an API key.

## 📢 Next Steps

1. **Share the release** with your team/users
2. **Update CHANGELOG.md** with v0.1.3 details
3. **Test installation** from the release
4. **Monitor** for any issues
5. **Celebrate!** 🎊

## 🔗 Quick Links

- **Release page**: https://github.com/Kevrollin/gitpilot.io/releases
- **Latest release**: https://github.com/Kevrollin/gitpilot.io/releases/latest
- **Tag**: https://github.com/Kevrollin/gitpilot.io/releases/tag/v0.1.3

---

**Ready to publish? Follow the steps above!** 🚀

