# Publishing v0.1.3 - Quick Guide

## Current Situation

- ✅ Version 0.1.3 is built locally
- ✅ Files ready in `dist/` folder
- ❌ Not yet pushed to GitHub
- ❌ No release created yet

**That's why pipx shows 0.1.2 as latest** - it's checking GitHub, not your local files.

## Option 1: Test Local Build First (Recommended)

Before publishing, test the local build:

```bash
cd ~/Kev.Projects/Niru-hackathon/jambosec.ai/auto_commit_assistant

# Install from local wheel file
pipx install dist/auto_commit_assistant-0.1.3-py3-none-any.whl --force

# Test it
autocommit --version
# Should show: dev.mk 0.1.3
```

## Option 2: Publish to GitHub (After Testing)

### Step 1: Commit Your Changes

```bash
cd ~/Kev.Projects/Niru-hackathon/jambosec.ai/auto_commit_assistant

# Check what's changed
git status

# Add all changes
git add .

# Commit
git commit -m "feat: Add API key, update branding to dev.mk, improve update logic"
```

### Step 2: Create Tag and Push

```bash
# Create tag
git tag -a v0.1.3 -m "Release v0.1.3 - dev.mk with built-in API key"

# Push changes and tag
git push origin master
git push origin v0.1.3
```

### Step 3: Create Release on GitHub

1. Go to: https://github.com/Kevrollin/gitpilot.io/releases/new
2. Select tag: `v0.1.3`
3. Upload files from `dist/`:
   - `auto_commit_assistant-0.1.3-py3-none-any.whl`
   - `auto_commit_assistant-0.1.3.tar.gz`
4. Add release notes
5. Publish

### Step 4: Test Installation

After publishing:

```bash
# Now pipx will see the new version
pipx upgrade auto-commit-assistant

# Or install fresh
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3
```

## Quick Command Summary

```bash
# 1. Test local build
pipx install dist/auto_commit_assistant-0.1.3-py3-none-any.whl --force

# 2. Commit and push
git add .
git commit -m "feat: v0.1.3 - dev.mk with built-in API key"
git tag -a v0.1.3 -m "Release v0.1.3"
git push origin master
git push origin v0.1.3

# 3. Create release on GitHub (upload dist/* files)

# 4. Test from GitHub
pipx upgrade auto-commit-assistant
```

## Why pipx Shows 0.1.2

- pipx checks GitHub repository for latest version
- GitHub currently has v0.1.2 as latest tag
- Your v0.1.3 exists locally but not on GitHub yet
- Once you push v0.1.3 and create release, pipx will see it

## Next Steps

1. **Test local build** (Option 1 above)
2. **If it works, commit and push** (Option 2 above)
3. **Create release on GitHub**
4. **Verify pipx can upgrade**

---

**Ready to publish? Follow the steps above!** 🚀

