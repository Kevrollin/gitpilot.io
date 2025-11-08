# Publishing to PyPI

This guide explains how to publish `auto-commit-assistant` to PyPI so users can install it with:

```bash
pip install auto-commit-assistant
```

## Prerequisites

1. **PyPI Account:**
   - Create an account at: https://pypi.org/account/register/
   - Verify your email address

2. **API Token:**
   - Go to: https://pypi.org/manage/account/token/
   - Create a new API token
   - Save it securely (you'll need it for uploading)

## Quick Publish

### Option 1: Use the Script (Recommended)

```bash
./scripts/publish_pypi.sh
```

This script will:
1. Build the package (if not already built)
2. Ask if you want to test on Test PyPI
3. Ask if you want to publish to PyPI
4. Upload the package

### Option 2: Manual Publishing

1. **Build the package:**
   ```bash
   ./scripts/build_package.sh
   ```

2. **Install twine:**
   ```bash
   pip install --upgrade twine
   ```

3. **Test on Test PyPI (recommended):**
   ```bash
   twine upload --repository testpypi dist/*
   ```

4. **Test installation from Test PyPI:**
   ```bash
   pip install --index-url https://test.pypi.org/simple/ auto-commit-assistant
   ```

5. **Publish to PyPI:**
   ```bash
   twine upload dist/*
   ```

## Authentication

### Option 1: API Token (Recommended)

Create a `~/.pypirc` file:

```ini
[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
username = __token__
password = pypi-your-test-api-token-here
```

### Option 2: Environment Variables

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-your-api-token-here
```

### Option 3: Interactive

Twine will prompt for credentials if not configured.

## After Publishing

### Users can install with:

```bash
# Using pip
pip install auto-commit-assistant

# Using pipx (recommended for CLI tools)
pipx install auto-commit-assistant

# Using pip with --user
pip install --user auto-commit-assistant
```

### Package will be available at:

- PyPI: https://pypi.org/project/auto-commit-assistant/
- Installation: `pip install auto-commit-assistant`

## Updating the Package

1. **Update version:**
   ```bash
   # Edit auto_commit/__init__.py
   __version__ = "1.1.2"
   ```

2. **Build:**
   ```bash
   ./scripts/build_package.sh
   ```

3. **Publish:**
   ```bash
   ./scripts/publish_pypi.sh
   ```

## Best Practices

1. **Test First:**
   - Always test on Test PyPI first
   - Verify installation works
   - Check package contents

2. **Version Numbers:**
   - Follow semantic versioning (1.1.1, 1.1.2, etc.)
   - Don't reuse version numbers
   - Increment appropriately (major.minor.patch)

3. **Package Name:**
   - Package name on PyPI: `auto-commit-assistant`
   - Import name: `auto_commit`
   - CLI command: `autocommit`

4. **Documentation:**
   - Update README.md
   - Add changelog entries
   - Update installation instructions

## Troubleshooting

### "File already exists"

- Version number is already published
- Update version in `auto_commit/__init__.py`
- Rebuild and publish

### "Invalid credentials"

- Check your API token
- Verify `~/.pypirc` file format
- Try interactive authentication

### "Package not found after publishing"

- Wait a few minutes for PyPI to update
- Check package name spelling
- Verify package was uploaded successfully

## Benefits of PyPI Publishing

✅ **Easy Installation:**
   - Users can just `pip install auto-commit-assistant`
   - No need to download files manually
   - Works with all Python package managers

✅ **Version Management:**
   - Users can upgrade with `pip install --upgrade`
   - Version history on PyPI
   - Easy to track updates

✅ **Distribution:**
   - Available worldwide via PyPI CDN
   - Fast downloads
   - Reliable hosting

✅ **Discovery:**
   - Searchable on pypi.org
   - Shows up in `pip search` (if enabled)
   - Better visibility

## Next Steps

1. **Publish to PyPI:**
   ```bash
   ./scripts/publish_pypi.sh
   ```

2. **Update Documentation:**
   - Add PyPI installation instructions
   - Update website with PyPI link
   - Update README.md

3. **Share:**
   - Share the PyPI link
   - Update website download page
   - Announce the release

---

**Ready to publish! 🚀**

For questions, see PyPI documentation: https://packaging.python.org/

