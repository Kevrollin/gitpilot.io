# Troubleshooting PyPI Publishing

The package isn't on PyPI yet. Let's check what's happening:

## Step 1: Check GitHub Actions Workflow

1. **Go to Actions tab:**
   - Visit: https://github.com/Kevrollin/gitpilot.io/actions

2. **Look for "Publish to PyPI" workflow:**
   - Did it run when you created the release?
   - What's the status? (green checkmark, red X, or yellow circle)

3. **Check the workflow run:**
   - Click on the workflow run
   - Check the logs for errors

## Common Issues

### Issue 1: Workflow Didn't Run

**Symptoms:**
- No workflow run appears in Actions tab
- Release was created but nothing happened

**Solutions:**

1. **Check workflow file exists:**
   ```bash
   ls -la .github/workflows/publish-pypi.yml
   ```

2. **Verify it's committed and pushed:**
   ```bash
   git add .github/workflows/publish-pypi.yml
   git commit -m "Add PyPI publishing workflow"
   git push
   ```

3. **Manually trigger the workflow:**
   - Go to: Actions tab → "Publish to PyPI" → "Run workflow"
   - Select branch: `master` or `main`
   - Click "Run workflow"

### Issue 2: Workflow Failed - "Publisher not verified"

**Symptoms:**
- Workflow runs but fails
- Error: "Publisher not verified" or authentication error

**Solutions:**

1. **Check trusted publisher setup:**
   - Go to: https://pypi.org/manage/account/publishing/
   - Verify the publisher is added
   - Check all values match exactly:
     - Project: `auto-commit-assistant`
     - Owner: `Kevrollin`
     - Repository: `gitpilot.io`
     - Workflow: `publish-pypi.yml`
     - Environment: `pypi` (or leave empty)

2. **Create GitHub environment (if using):**
   - Go to: Settings → Environments
   - Create environment: `pypi`
   - Save

3. **Re-run the workflow:**
   - After fixing, re-run the workflow
   - The publisher should verify after first successful run

### Issue 3: Workflow Failed - "Package name mismatch"

**Symptoms:**
- Error about package name
- Build succeeds but publish fails

**Solutions:**

1. **Check package name in setup.py:**
   ```bash
   grep "name=" setup.py
   # Should show: name="auto-commit-assistant"
   ```

2. **Verify PyPI project name matches:**
   - In trusted publisher form, use: `auto-commit-assistant`
   - Must match exactly (case-sensitive, hyphens matter)

### Issue 4: Workflow Succeeded But Package Not on PyPI

**Symptoms:**
- Workflow shows green checkmark
- But package not found on PyPI

**Solutions:**

1. **Wait a few minutes:**
   - PyPI can take 2-5 minutes to update
   - Refresh the page

2. **Check PyPI directly:**
   - Visit: https://pypi.org/project/auto-commit-assistant/
   - Try searching: https://pypi.org/search/?q=auto-commit-assistant

3. **Check workflow logs:**
   - Look for "Successfully published" message
   - Check for any warnings

4. **Verify package name:**
   - Make sure you're searching for: `auto-commit-assistant`
   - Not: `auto_commit_assistant` or `auto-commit-assistant-1.1.1`

## Quick Fix: Manual Publishing

If GitHub Actions isn't working, publish manually:

1. **Build the package:**
   ```bash
   ./scripts/build_package.sh
   ```

2. **Publish manually:**
   ```bash
   ./scripts/publish_pypi.sh
   ```

   This will:
   - Ask for PyPI credentials
   - Upload the package
   - Make it available on PyPI

## Verify Setup

Run this checklist:

- [ ] Workflow file exists: `.github/workflows/publish-pypi.yml`
- [ ] Workflow is committed and pushed to GitHub
- [ ] Trusted publisher added on PyPI
- [ ] GitHub environment `pypi` created (if using)
- [ ] Package name matches: `auto-commit-assistant`
- [ ] Release was created on GitHub
- [ ] Workflow ran (check Actions tab)

## Next Steps

1. **Check Actions tab first:**
   - https://github.com/Kevrollin/gitpilot.io/actions
   - See if workflow ran and what happened

2. **If workflow didn't run:**
   - Make sure workflow file is pushed
   - Manually trigger it

3. **If workflow failed:**
   - Check the error message
   - Fix the issue
   - Re-run the workflow

4. **If workflow succeeded but no package:**
   - Wait a few minutes
   - Check PyPI again
   - Verify package name

## Still Having Issues?

1. **Check workflow logs:**
   - Actions tab → Click on workflow run → Check all steps

2. **Verify trusted publisher:**
   - https://pypi.org/manage/account/publishing/
   - Make sure it's added and verified

3. **Try manual publishing:**
   - Use `./scripts/publish_pypi.sh` as a backup

---

**Most likely issue:** The workflow file might not be pushed to GitHub yet, or the trusted publisher isn't set up.

