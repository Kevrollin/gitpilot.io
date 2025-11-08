# Quick Release Guide

## 🚀 Creating Your First Release

### Step 1: Prepare Your Release

1. **Update CHANGELOG.md** with new changes
2. **Test your code** to make sure everything works
3. **Commit all changes** to your repository

### Step 2: Create the Release

**Option A: Use the Release Script (Easiest)**
```bash
./scripts/release.sh
```

The script will:
- Show current version
- Ask for new version (e.g., `0.1.1`)
- Update version in code
- Create git tag
- Push to GitHub (optional)

**Option B: Manual Release**
```bash
# 1. Update version in auto_commit/__init__.py
# 2. Update CHANGELOG.md
# 3. Commit changes
git add .
git commit -m "Bump version to 0.1.1"

# 4. Create and push tag
git tag -a v0.1.1 -m "Release v0.1.1"
git push origin main
git push origin v0.1.1
```

### Step 3: GitHub Actions Does the Rest

Once you push the tag, GitHub Actions will automatically:
- ✅ Build the package (wheel and source)
- ✅ Create a GitHub release
- ✅ Upload distribution files
- ✅ Add release notes

### Step 4: Verify Release

1. Go to: https://github.com/Kevrollin/gitpilot.io/releases
2. Check that the release was created
3. Verify distribution files are attached
4. Edit release notes if needed

## 📦 What Gets Created

- **GitHub Release** with version tag
- **Source distribution** (`.tar.gz`)
- **Wheel distribution** (`.whl`)
- **Release notes** from tag message

## 🔄 Release Workflow

```
1. Update version → 2. Create tag → 3. Push tag → 4. GitHub Actions → 5. Release!
```

## 📝 Example Release

```bash
# Current version: 0.1.0
# New version: 0.1.1

./scripts/release.sh
# Enter: 0.1.1
# Enter release notes (optional)
# Push? (y/n): y

# Wait ~2 minutes for GitHub Actions
# Check: https://github.com/Kevrollin/gitpilot.io/releases
```

## ✅ Release Checklist

- [ ] Code is tested and working
- [ ] CHANGELOG.md is updated
- [ ] Version is updated in `auto_commit/__init__.py`
- [ ] All changes are committed
- [ ] Tag is created and pushed
- [ ] GitHub Actions completed successfully
- [ ] Release page looks good
- [ ] Distribution files are attached

## 🎯 Version Numbering

Follow semantic versioning: **MAJOR.MINOR.PATCH**

- `0.1.0` → `0.1.1` (bug fix)
- `0.1.1` → `0.2.0` (new feature)
- `0.2.0` → `1.0.0` (breaking change)

## 🔗 Useful Links

- **Releases**: https://github.com/Kevrollin/gitpilot.io/releases
- **Actions**: https://github.com/Kevrollin/gitpilot.io/actions
- **Full Release Guide**: See [RELEASE.md](RELEASE.md)

## 💡 Tips

- Always test before releasing
- Update CHANGELOG.md with changes
- Use meaningful release notes
- Tag format: `v0.1.1` (must start with `v`)
- GitHub Actions runs automatically on tag push

---

**That's it! Your release will be automatically created by GitHub Actions.** 🎉

