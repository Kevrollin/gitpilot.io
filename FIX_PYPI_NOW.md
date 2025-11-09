# Fix PyPI Publishing - Quick Steps

The package isn't on PyPI because the workflow hasn't run yet. Here's how to fix it:

## Step 1: Push Workflow File to GitHub

The workflow file exists locally but needs to be on GitHub:

```bash
# Add and commit the workflow file
git add .github/workflows/publish-pypi.yml
git commit -m "Add PyPI publishing workflow"
git push
```

## Step 2: Set Up Trusted Publisher on PyPI

1. **Go to PyPI:**
   - Visit: https://pypi.org/manage/account/publishing/
   - Log in

2. **Click "Add a new pending publisher"**

3. **Fill in the form with these EXACT values:**

   ```
   PyPI Project Name: auto-commit-assistant
   Owner: Kevrollin
   Repository name: gitpilot.io
   Workflow name: publish-pypi.yml
   Environment name: pypi
   ```

4. **Click "Add"**

## Step 3: Create GitHub Environment (Optional but Recommended)

1. **Go to:**
   - https://github.com/Kevrollin/gitpilot.io/settings/environments

2. **Click "New environment"**

3. **Name it:** `pypi`

4. **Click "Configure environment" → "Save protection rules"**

## Step 4: Trigger the Workflow

### Option A: Re-publish the Release

1. **Go to your release:**
   - https://github.com/Kevrollin/gitpilot.io/releases/tag/v1.1.1

2. **Click the pencil icon (Edit)**

3. **Uncheck "Set as the latest release"** (if checked)

4. **Click "Update release"**

5. **Then click "Publish release" again**

This will trigger the workflow.

### Option B: Manually Trigger Workflow

1. **Go to Actions tab:**
   - https://github.com/Kevrollin/gitpilot.io/actions

2. **Click "Publish to PyPI" workflow**

3. **Click "Run workflow"**

4. **Select branch:** `master` (or your default branch)

5. **Click "Run workflow"**

## Step 5: Watch It Work

1. **Go to Actions tab:**
   - https://github.com/Kevrollin/gitpilot.io/actions

2. **Click on the running workflow**

3. **Watch the steps:**
   - "Build package" should succeed
   - "Publish to PyPI" should succeed

4. **Wait 2-5 minutes** for PyPI to update

5. **Check PyPI:**
   - https://pypi.org/project/auto-commit-assistant/

## Quick Command Summary

```bash
# 1. Push workflow file
git add .github/workflows/publish-pypi.yml
git commit -m "Add PyPI publishing workflow"
git push

# 2. Then go to PyPI and set up trusted publisher
# 3. Then manually trigger workflow or re-publish release
```

## If It Still Doesn't Work

### Check Workflow Logs

1. Go to Actions tab
2. Click on the workflow run
3. Check for errors in the logs
4. Common issues:
   - "Publisher not verified" → Trusted publisher not set up
   - "Environment not found" → Create the `pypi` environment
   - "Workflow file not found" → Make sure it's pushed to GitHub

### Manual Publishing (Backup)

If GitHub Actions isn't working, publish manually:

```bash
./scripts/publish_pypi.sh
```

This will ask for PyPI credentials and upload directly.

---

**Most Important:** Make sure the workflow file is pushed to GitHub and the trusted publisher is set up on PyPI!

