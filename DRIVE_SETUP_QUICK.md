# Quick Google Drive Setup - 5 Minutes

## Step 1: Build Package

```bash
./scripts/build_package.sh
```

## Step 2: Upload to Google Drive

1. **Go to Google Drive:**
   - https://drive.google.com

2. **Create folder:**
   - New → Folder → Name: `dev.mk-packages`

3. **Upload files:**
   - Drag `dist/auto_commit_assistant-1.1.1-py3-none-any.whl`
   - Drag `dist/auto_commit_assistant-1.1.1.tar.gz`

4. **Share folder:**
   - Right-click folder → Share
   - Change to "Anyone with the link can view"
   - Copy link

## Step 3: Get File IDs

For each file:

1. **Right-click file → Get link**
2. **Copy the link:**
   ```
   https://drive.google.com/file/d/FILE_ID_HERE/view?usp=sharing
   ```
3. **Extract the FILE_ID** (the part between `/d/` and `/view`)

Or use the helper script:
```bash
./scripts/get_drive_links.sh
```

## Step 4: Update Website

Edit `website/index.html` and replace:
- `YOUR_FILE_ID_WHL` with your wheel file ID
- `YOUR_FILE_ID_TAR` with your tar.gz file ID

## Step 5: Test

1. **Visit your website**
2. **Click download links** - should download files
3. **Test installation:**
   ```bash
   pip install downloaded-file.whl
   ```

## Direct Download Links Format

```
https://drive.google.com/uc?export=download&id=FILE_ID
```

## Installation for Users

Users can install with:

```bash
# Download and install
pip install https://drive.google.com/uc?export=download&id=YOUR_FILE_ID

# Or download first, then install
curl -L "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID" -o package.whl
pip install package.whl
```

## Done! 🚀

Your package is now hosted on Google Drive and users can download it!

---

**Need help?** See `GOOGLE_DRIVE_HOSTING.md` for detailed instructions.

