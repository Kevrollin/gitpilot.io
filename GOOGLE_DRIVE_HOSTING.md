# Hosting Package on Google Drive

This guide explains how to host your Python package on Google Drive so users can download and install it.

## Quick Setup

### Step 1: Build the Package

```bash
./scripts/build_package.sh
```

This creates:
- `dist/auto_commit_assistant-1.1.1-py3-none-any.whl`
- `dist/auto_commit_assistant-1.1.1.tar.gz`

### Step 2: Upload to Google Drive

#### Option A: Using Web Interface (Easiest)

1. **Go to Google Drive:**
   - Visit: https://drive.google.com

2. **Create a folder:**
   - Click "New" → "Folder"
   - Name it: `dev.mk-packages`

3. **Upload files:**
   - Open the folder
   - Drag and drop both files from `dist/` folder:
     - `auto_commit_assistant-1.1.1-py3-none-any.whl`
     - `auto_commit_assistant-1.1.1.tar.gz`

4. **Share the folder:**
   - Right-click the folder → "Share"
   - Click "Change to anyone with the link"
   - Select "Viewer"
   - Click "Copy link"
   - Save the link

5. **Get direct download links:**
   - Right-click each file → "Get link"
   - Copy the link
   - Convert to direct download link (see below)

#### Option B: Using gdrive CLI (Automated)

1. **Install gdrive CLI:**
   ```bash
   # Visit: https://github.com/glotlabs/gdrive/releases
   # Download for your OS
   # Or use: https://github.com/prasmussen/gdrive
   ```

2. **Authenticate:**
   ```bash
   gdrive about
   # This will open browser for authentication
   ```

3. **Upload:**
   ```bash
   ./scripts/upload_to_drive.sh
   ```

### Step 3: Convert to Direct Download Links

Google Drive links need to be converted for direct download.

**Original link format:**
```
https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```

**Direct download format:**
```
https://drive.google.com/uc?export=download&id=FILE_ID
```

**How to get FILE_ID:**
- From the sharing link: `https://drive.google.com/file/d/FILE_ID/view`
- Extract the `FILE_ID` part

### Step 4: Update Website

Update `website/index.html` with the direct download links:

```html
<a href="https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_WHL" class="download-link" download>
    📥 Download Wheel (.whl)
</a>
<a href="https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_TAR" class="download-link secondary" download>
    📥 Download Source (.tar.gz)
</a>
```

## Installation Instructions for Users

### Method 1: Download and Install

1. **Download the file:**
   - Click the download link
   - Save the file (`.whl` or `.tar.gz`)

2. **Install:**
   ```bash
   # For .whl file:
   pip install auto_commit_assistant-1.1.1-py3-none-any.whl
   
   # For .tar.gz file:
   pip install auto_commit_assistant-1.1.1.tar.gz
   
   # Or with pipx:
   pipx install auto_commit_assistant-1.1.1-py3-none-any.whl
   ```

### Method 2: Direct Download with curl/wget

```bash
# Download wheel file
curl -L "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID" -o package.whl

# Install
pip install package.whl
```

### Method 3: One-liner Installation

```bash
# Download and install in one command
pip install https://drive.google.com/uc?export=download&id=YOUR_FILE_ID
```

## Updating Packages

When you release a new version:

1. **Build new package:**
   ```bash
   ./scripts/build_package.sh
   ```

2. **Upload to Google Drive:**
   - Replace old files with new ones
   - Or create versioned folders

3. **Update website links:**
   - Update file IDs in `website/index.html`
   - Update version numbers

## Alternative: Use Google Drive API

For automated updates, you can use Google Drive API:

```python
# Example using PyDrive2
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Upload file
file = drive.CreateFile({'title': 'package.whl', 'parents': [{'id': 'FOLDER_ID'}]})
file.SetContentFile('dist/package.whl')
file.Upload()
```

## Benefits of Google Drive Hosting

✅ **Free:** No cost for hosting  
✅ **Easy:** Simple upload process  
✅ **Accessible:** Works from anywhere  
✅ **No Setup:** No PyPI account needed  
✅ **Fast:** Google's CDN  

## Limitations

⚠️ **File Size:** Google Drive has limits (15GB free)  
⚠️ **Download Limits:** May have rate limits  
⚠️ **Direct Links:** Need to convert to direct download format  
⚠️ **Updates:** Manual process (not automatic like PyPI)  

## Best Practices

1. **Organize by version:**
   - Create folders for each version
   - Keep old versions available

2. **Use descriptive names:**
   - Include version in filename
   - Make it clear which file is which

3. **Share appropriately:**
   - Use "Anyone with the link can view"
   - Don't make it editable

4. **Update website:**
   - Keep download links updated
   - Include installation instructions

## Troubleshooting

### "Download quota exceeded"

- Google Drive has download limits
- Solution: Use PyPI or alternative hosting

### "File not found"

- Check sharing settings
- Verify file ID is correct
- Make sure link is public

### "Installation failed"

- Verify file downloaded correctly
- Check file integrity
- Try downloading again

## Alternative Hosting Options

If Google Drive doesn't work:

1. **GitHub Releases:**
   - Upload to GitHub releases
   - Direct download links
   - No conversion needed

2. **Dropbox:**
   - Similar to Google Drive
   - Direct download links available

3. **AWS S3:**
   - Professional hosting
   - Direct download links
   - Pay per use

4. **GitLab Packages:**
   - Similar to GitHub
   - Free for public repos

---

**Ready to host on Google Drive! 🚀**

Follow the steps above to upload and share your packages.

