# Release Guide

This guide explains how to create a new release for Gitpilot.

## Quick Release

Use the release script:

```bash
./scripts/release.sh
```

The script will:
1. Show current version
2. Ask for new version
3. Update version in code
4. Create git tag
5. Push to GitHub (optional)
6. GitHub Actions will automatically create the release

## Manual Release

### Step 1: Update Version

Edit `auto_commit/__init__.py`:
```python
__version__ = "0.1.1"  # Update to new version
```

### Step 2: Update CHANGELOG.md

Add an entry for the new version:
```markdown
## [0.1.1] - 2024-01-XX

### Added
- New feature description

### Changed
- Change description

### Fixed
- Bug fix description
```

### Step 3: Commit Changes

```bash
git add auto_commit/__init__.py CHANGELOG.md
git commit -m "Bump version to 0.1.1"
```

### Step 4: Create and Push Tag

```bash
# Create annotated tag
git tag -a v0.1.1 -m "Release v0.1.1

Description of changes in this release."

# Push tag to GitHub
git push origin v0.1.1
```

### Step 5: Push Changes

```bash
git push origin main
```

### Step 6: GitHub Actions

GitHub Actions will automatically:
- Build the package
- Create a GitHub release
- Upload distribution files (wheel and source)

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

Examples:
- `0.1.0` → `0.1.1` (bug fix)
- `0.1.1` → `0.2.0` (new feature)
- `0.2.0` → `1.0.0` (breaking change)

## Release Checklist

- [ ] Update version in `auto_commit/__init__.py`
- [ ] Update `CHANGELOG.md` with new changes
- [ ] Test installation from git repository
- [ ] Test the `--update` command works
- [ ] Create git tag
- [ ] Push tag to GitHub
- [ ] Verify GitHub Actions workflow completed
- [ ] Check release page on GitHub
- [ ] Update documentation if needed
- [ ] Announce release to team/users

## GitHub Actions

The release workflow (`.github/workflows/release.yml`) automatically:
- Triggers on tags matching `v*.*.*`
- Builds Python package (wheel and source)
- Creates GitHub release
- Uploads distribution files
- Sets release notes from tag message

## Testing a Release

Before releasing, test the installation:

```bash
# Test from specific tag/version
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.0

# Or test locally
pip install -e .

# Test the tool
autocommit --version
autocommit --help
```

## Distribution Files

GitHub Actions creates:
- `auto_commit_assistant-X.X.X.tar.gz` (source distribution)
- `auto_commit_assistant-X.X.X-py3-none-any.whl` (wheel distribution)

These are automatically attached to the GitHub release.

## Installing from a Release

Users can install a specific version:

```bash
# Using pipx
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.0

# Using pip
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.0

# Latest version (default)
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
```

## Troubleshooting

### GitHub Actions Failed

1. Check the Actions tab in GitHub
2. Review error logs
3. Fix issues and push again
4. Delete and recreate the tag if needed

### Tag Already Exists

If you need to recreate a tag:

```bash
# Delete local tag
git tag -d v0.1.0

# Delete remote tag
git push origin --delete v0.1.0

# Recreate tag
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

### Version Not Updating

Make sure you:
1. Updated `auto_commit/__init__.py`
2. Committed the changes
3. Created a new tag with the version
4. Pushed the tag to GitHub

## Next Steps After Release

1. **Update documentation** if needed
2. **Announce release** to users/team
3. **Monitor** for any issues
4. **Plan** next version features

---

For questions or issues, open an issue on GitHub.

