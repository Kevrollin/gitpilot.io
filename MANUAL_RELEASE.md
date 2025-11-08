# Manual Release Guide

If GitHub Actions is not available (billing issues, private repo limits, etc.), you can create releases manually.

## Option 1: Using GitHub CLI (Recommended)

### Install GitHub CLI

```bash
# Linux
sudo apt install gh

# macOS
brew install gh

# Authenticate
gh auth login
```

### Create Release

```bash
# Build the package first
python3 -m pip install --upgrade build wheel
python3 -m build

# Create release with GitHub CLI
gh release create v0.1.2 \
    --title "Release v0.1.2" \
    --notes "Release notes here" \
    dist/*.whl dist/*.tar.gz
```

### Or Use the Script

```bash
./scripts/create_release_manual.sh 0.1.2
```

## Option 2: Using GitHub Web Interface

### Step 1: Build the Package

```bash
# Install build tools
python3 -m pip install --upgrade build wheel

# Build the package
python3 -m build
```

This creates files in the `dist/` directory:
- `auto_commit_assistant-0.1.2.tar.gz` (source distribution)
- `auto_commit_assistant-0.1.2-py3-none-any.whl` (wheel distribution)

### Step 2: Create Release on GitHub

1. Go to: https://github.com/Kevrollin/gitpilot.io/releases/new
2. **Select tag**: Choose `v0.1.2` (or create a new tag)
3. **Release title**: `Release v0.1.2`
4. **Description**: Add release notes
5. **Attach files**: Upload the files from `dist/` directory:
   - `auto_commit_assistant-0.1.2.tar.gz`
   - `auto_commit_assistant-0.1.2-py3-none-any.whl`
6. Click **"Publish release"**

## Option 3: Fix GitHub Actions Billing

If you want to use automated releases:

1. **For Public Repositories**: 
   - GitHub Actions is free for public repos
   - No billing required
   - Make sure your repo is public

2. **For Private Repositories**:
   - Go to: https://github.com/settings/billing
   - Set up billing (GitHub Actions is free up to 2000 minutes/month)
   - Or make the repository public

3. **Check Usage**:
   - Go to: https://github.com/settings/billing
   - Check if you've exceeded free tier limits

## Quick Release Script

Use the manual release script:

```bash
# After creating and pushing a tag
./scripts/create_release_manual.sh 0.1.2
```

The script will:
1. Build the package
2. Create release using GitHub CLI (if installed)
3. Or provide instructions for manual upload

## Complete Manual Release Workflow

```bash
# 1. Update version
# Edit auto_commit/__init__.py

# 2. Commit and tag
git add .
git commit -m "Bump version to 0.1.2"
git tag -a v0.1.2 -m "Release v0.1.2"
git push origin master
git push origin v0.1.2

# 3. Build package
python3 -m pip install --upgrade build wheel
python3 -m build

# 4. Create release (choose one):
# Option A: GitHub CLI
gh release create v0.1.2 --title "Release v0.1.2" --notes "Notes" dist/*

# Option B: Web interface
# Go to https://github.com/Kevrollin/gitpilot.io/releases/new
# Upload dist/*.whl and dist/*.tar.gz
```

## Troubleshooting

### GitHub CLI Not Found

```bash
# Install GitHub CLI
sudo apt install gh  # Linux
brew install gh      # macOS

# Authenticate
gh auth login
```

### Build Fails

```bash
# Install build dependencies
python3 -m pip install --upgrade pip build wheel

# Try building again
python3 -m build
```

### Can't Upload Files

- Make sure files are in `dist/` directory
- Check file sizes (should be reasonable, not too large)
- Try uploading one file at a time in web interface

## Summary

Even without GitHub Actions, you can easily create releases:
1. **Build** the package locally
2. **Create release** via GitHub CLI or web interface
3. **Upload** distribution files

The manual process takes just a few minutes!

