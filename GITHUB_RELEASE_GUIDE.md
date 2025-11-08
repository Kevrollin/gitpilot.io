# Creating a Release on GitHub Dashboard

## Step-by-Step Guide

### Step 1: Prepare Your Files

First, make sure you've built the package:

```bash
cd auto_commit_assistant
python3 -m pip install --upgrade build wheel
python3 -m build
```

This creates files in the `dist/` directory:
- `auto_commit_assistant-0.1.3-py3-none-any.whl` (wheel file)
- `auto_commit_assistant-0.1.3.tar.gz` (source distribution)

### Step 2: Go to GitHub Releases

1. Open your browser
2. Go to: https://github.com/Kevrollin/gitpilot.io
3. Click on **"Releases"** (right sidebar, or go to: https://github.com/Kevrollin/gitpilot.io/releases)
4. Click **"Draft a new release"** button (or "Create a new release")

### Step 3: Fill in Release Details

1. **Choose a tag:**
   - Click "Choose a tag" dropdown
   - Type: `v0.1.3` (or your version)
   - If tag doesn't exist, type it and select "Create new tag: v0.1.3 on publish"
   - Select your branch: `master` (or `main`)

2. **Release title:**
   - Enter: `Release v0.1.3` or `dev.mk v0.1.3`

3. **Release description:**
   ```
   ## dev.mk v0.1.3
   
   ### What's New
   - ✨ No API key required - works out of the box!
   - 🎨 Updated branding to dev.mk by Kelvin Mukaria
   - 🚀 Built-in API key for instant use
   - 🔧 Users can still set their own key for unlimited usage
   
   ### Installation
   
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
   
   ### Usage
   
   ```bash
   # Works immediately - no API key needed!
   autocommit
   
   # Optional: Set your own key for unlimited usage
   export GEMINI_API_KEY='your-key-here'
   ```
   
   ### What's Changed
   
   See [CHANGELOG.md](https://github.com/Kevrollin/gitpilot.io/blob/master/CHANGELOG.md) for details.
   ```

### Step 4: Upload Distribution Files

1. Scroll down to **"Attach binaries"** section
2. Click **"selecting them"** link (or drag and drop)
3. Navigate to your `dist/` folder:
   ```
   /home/miss-royalty/Kev.Projects/Niru-hackathon/jambosec.ai/auto_commit_assistant/dist/
   ```
4. Select these files:
   - `auto_commit_assistant-0.1.3-py3-none-any.whl`
   - `auto_commit_assistant-0.1.3.tar.gz`
5. Wait for upload to complete

### Step 5: Publish Release

1. Review your release details
2. Make sure files are uploaded
3. Click **"Publish release"** button (green button at bottom)

### Step 6: Verify Release

1. You'll be redirected to the release page
2. Verify:
   - ✅ Release title is correct
   - ✅ Description looks good
   - ✅ Files are attached (you should see 2 files)
   - ✅ Tag is created

### Step 7: Test Installation

Test that users can install from the release:

```bash
# Install from the release tag
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3

# Or install from the wheel file directly
pipx install https://github.com/Kevrollin/gitpilot.io/releases/download/v0.1.3/auto_commit_assistant-0.1.3-py3-none-any.whl

# Test it works
autocommit --version
```

## Quick Checklist

Before publishing, make sure:

- [ ] Version number is correct (v0.1.3)
- [ ] Release title is set
- [ ] Release description includes installation instructions
- [ ] Both distribution files are uploaded (.whl and .tar.gz)
- [ ] Tag will be created (or already exists)
- [ ] Branch is correct (master/main)

## Troubleshooting

### Files Not Uploading

- Check file sizes (should be reasonable, not too large)
- Try uploading one at a time
- Check your internet connection
- Try a different browser

### Tag Already Exists

- If tag exists, you can't create it again
- Either use a new version number
- Or delete the old tag first (in repository → Tags)

### Can't Find dist/ Folder

- Make sure you ran `python3 -m build`
- Check you're in the right directory
- Files should be in `auto_commit_assistant/dist/`

## After Publishing

1. **Share the release** with your team/users
2. **Update documentation** if needed
3. **Monitor** for any issues
4. **Test installation** from the release
5. **Celebrate!** 🎉

## Next Steps

After the release is published:

1. Update `CHANGELOG.md` with the new version
2. Announce the release to your users
3. Monitor GitHub for issues/feedback
4. Plan the next release

---

**Ready to publish? Follow the steps above!** 🚀

