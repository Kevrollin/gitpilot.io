# PyPI Publishing via GitHub Actions (OpenID Connect)

This guide explains how to set up automatic PyPI publishing using GitHub Actions with OpenID Connect (no API tokens needed!).

## Benefits

✅ **No API Tokens:** Uses OpenID Connect for secure authentication  
✅ **Automatic Publishing:** Publishes when you create a GitHub release  
✅ **Secure:** No secrets to manage or store  
✅ **Easy:** One-time setup, then automatic  

## Setup Steps

### Step 1: Create GitHub Actions Workflow

The workflow file is already created at:
```
.github/workflows/publish-pypi.yml
```

This workflow will:
- Trigger on GitHub releases
- Build the package
- Publish to PyPI automatically

### Step 2: Create GitHub Environment (Recommended)

1. **Go to your repository on GitHub:**
   - Navigate to: `Settings` → `Environments`

2. **Create new environment:**
   - Click `New environment`
   - Name: `pypi`
   - Click `Configure environment`

3. **Add protection rules (optional but recommended):**
   - Add required reviewers (if you have collaborators)
   - Set deployment branches (e.g., only `master` or `main`)

4. **Save the environment**

### Step 3: Configure Trusted Publisher on PyPI

1. **Go to PyPI:**
   - Visit: https://pypi.org/manage/account/publishing/
   - Log in to your PyPI account

2. **Add a new trusted publisher:**
   - Click `Add a new pending publisher`

3. **Fill in the form:**

   **PyPI Project Name:**
   ```
   auto-commit-assistant
   ```
   *(This must match the name in your `setup.py`)*

   **Owner:**
   ```
   Kevrollin
   ```
   *(Your GitHub username or organization name)*

   **Repository name:**
   ```
   gitpilot.io
   ```
   *(Your repository name)*

   **Workflow name:**
   ```
   publish-pypi.yml
   ```
   *(The filename in `.github/workflows/`)*

   **Environment name:**
   ```
   pypi
   ```
   *(The GitHub environment you created, or leave empty if not using environments)*

4. **Click `Add`**

5. **Verify:**
   - The publisher will show as "pending"
   - After the first successful workflow run, it will become "verified"

### Step 4: Test the Setup

#### Option A: Create a GitHub Release (Recommended)

1. **Create a release:**
   ```bash
   git tag v1.1.1
   git push origin v1.1.1
   ```
   Then go to GitHub → Releases → Draft a new release → Select the tag

2. **Or use the release script:**
   ```bash
   ./scripts/release.sh
   ```
   When prompted, choose to create a GitHub release

3. **Watch the workflow:**
   - Go to: `Actions` tab in your repository
   - You should see "Publish to PyPI" workflow running
   - It will automatically publish to PyPI when the release is published

#### Option B: Manual Trigger (Testing)

1. **Go to Actions tab:**
   - Click on `Publish to PyPI` workflow
   - Click `Run workflow`
   - Click `Run workflow` button

2. **Watch the workflow:**
   - It will build and attempt to publish
   - Check the logs for any errors

### Step 5: Verify Publication

1. **Check PyPI:**
   - Visit: https://pypi.org/project/auto-commit-assistant/
   - Your package should be listed

2. **Test installation:**
   ```bash
   pip install auto-commit-assistant
   ```

## Workflow Details

### When It Runs

The workflow triggers on:
- **GitHub Release:** When you publish a release
- **Manual:** Via `workflow_dispatch` (Actions tab → Run workflow)

### What It Does

1. Checks out your code
2. Sets up Python
3. Installs build tools
4. Builds the package (`.whl` and `.tar.gz`)
5. Publishes to PyPI using OpenID Connect

### Environment Variables

No environment variables needed! OpenID Connect handles authentication.

## Troubleshooting

### "Publisher not verified"

- Make sure you've added the trusted publisher on PyPI
- Check that all fields match exactly (case-sensitive)
- Wait for the first workflow run to complete

### "Workflow not triggering"

- Check that the workflow file is in `.github/workflows/`
- Verify the filename matches what you entered on PyPI
- Check GitHub Actions is enabled in repository settings

### "Build failed"

- Check Python version compatibility
- Verify `setup.py` is correct
- Check build logs for specific errors

### "Publish failed"

- Verify PyPI project name matches `setup.py`
- Check that version number is unique (not already published)
- Ensure you have permission to publish to the project

## Updating the Package

### For New Versions:

1. **Update version in code:**
   ```bash
   # Edit auto_commit/__init__.py
   __version__ = "1.1.2"
   ```

2. **Commit and push:**
   ```bash
   git add auto_commit/__init__.py
   git commit -m "Bump version to 1.1.2"
   git push
   ```

3. **Create a release:**
   ```bash
   git tag v1.1.2
   git push origin v1.1.2
   ```
   Then create a GitHub release for that tag

4. **Automatic publishing:**
   - GitHub Actions will automatically build and publish
   - No manual steps needed!

## Security Notes

- ✅ **No API tokens stored** - Uses OpenID Connect
- ✅ **Workflow runs in isolated environment**
- ✅ **Only publishes on releases** - Prevents accidental publishes
- ✅ **Environment protection** - Can require approvals

## Alternative: Manual Publishing

If you prefer manual control, you can still use:

```bash
./scripts/publish_pypi.sh
```

This uses API tokens instead of OpenID Connect.

## Next Steps

1. ✅ Workflow file created (`.github/workflows/publish-pypi.yml`)
2. ⏳ Create GitHub environment `pypi` (optional but recommended)
3. ⏳ Add trusted publisher on PyPI
4. ⏳ Create a test release to verify

---

**Ready to set up! Follow the steps above to enable automatic PyPI publishing.** 🚀

