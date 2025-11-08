# Create GitHub Release for v1.1.1

The tag `v1.1.1` already exists. Here's how to create a GitHub release for it:

## Option 1: Via GitHub Web Interface (Easiest)

1. **Go to your repository:**
   - Visit: https://github.com/Kevrollin/gitpilot.io/releases

2. **Click "Draft a new release":**

3. **Select the tag:**
   - Choose tag: `v1.1.1`
   - If tag doesn't appear, type `v1.1.1` in the tag field

4. **Fill in release details:**
   - **Release title:** `Release v1.1.1 - API Key Error Handling Improvements`
   - **Description:**
     ```
     ## Changes in v1.1.1
     
     - Improved API key error handling with clear user instructions
     - Enhanced error messages for better user experience
     - Better guidance for users to set their own API key
     - Fixed timeout issues and safety filter handling
     - Added timeout protection for API requests
     - Improved response handling for blocked content
     
     ## Installation
     
     ```bash
     pip install auto-commit-assistant
     ```
     
     Or from GitHub:
     ```bash
     pipx install git+https://github.com/Kevrollin/gitpilot.io.git
     ```
     ```

5. **Click "Publish release"**

6. **Watch the magic:**
   - GitHub Actions will automatically build and publish to PyPI
   - Check the Actions tab to see the workflow running
   - Your package will be available on PyPI shortly!

## Option 2: Via GitHub CLI

If you have `gh` CLI installed:

```bash
gh release create v1.1.1 \
  --title "Release v1.1.1 - API Key Error Handling Improvements" \
  --notes "## Changes in v1.1.1

- Improved API key error handling with clear user instructions
- Enhanced error messages for better user experience
- Better guidance for users to set their own API key
- Fixed timeout issues and safety filter handling
- Added timeout protection for API requests
- Improved response handling for blocked content

## Installation

\`\`\`bash
pip install auto-commit-assistant
\`\`\`

Or from GitHub:
\`\`\`bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
\`\`\`"
```

## Option 3: Delete and Recreate Tag (If Needed)

If you need to update the tag:

```bash
# Delete local tag
git tag -d v1.1.1

# Delete remote tag
git push origin :refs/tags/v1.1.1

# Create new tag
git tag -a v1.1.1 -m "Release v1.1.1"
git push origin v1.1.1
```

## After Creating the Release

1. **Check GitHub Actions:**
   - Go to: https://github.com/Kevrollin/gitpilot.io/actions
   - You should see "Publish to PyPI" workflow running
   - Wait for it to complete

2. **Verify on PyPI:**
   - Visit: https://pypi.org/project/auto-commit-assistant/
   - Your package should be listed with version 1.1.1

3. **Test installation:**
   ```bash
   pip install auto-commit-assistant
   ```

## Troubleshooting

### "Workflow not running"

- Check that the workflow file exists: `.github/workflows/publish-pypi.yml`
- Verify you've set up the trusted publisher on PyPI
- Check workflow permissions in repository settings

### "Publisher not verified"

- Make sure you've added the trusted publisher on PyPI
- Wait for the first workflow run to complete
- Check that all form values match exactly

### "Package already exists"

- Version 1.1.1 might already be on PyPI
- Update version to 1.1.2 and create a new release
- Or delete the existing package on PyPI (if you have access)

---

**Ready to create the release! 🚀**

Go to: https://github.com/Kevrollin/gitpilot.io/releases/new?tag=v1.1.1

