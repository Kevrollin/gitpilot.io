# PyPI Trusted Publisher Form - Quick Reference

Use these exact values when filling out the PyPI trusted publisher form:

## Form Values

**PyPI Project Name:**
```
auto-commit-assistant
```
*(Must match the `name` field in `setup.py`)*

**Owner:**
```
Kevrollin
```
*(Your GitHub username - check your repository URL)*

**Repository name:**
```
gitpilot.io
```
*(Your repository name - check your repository URL)*

**Workflow name:**
```
publish-pypi.yml
```
*(The filename in `.github/workflows/publish-pypi.yml`)*

**Environment name:**
```
pypi
```
*(Optional - the GitHub environment name, or leave empty)*

## Quick Steps

1. Go to: https://pypi.org/manage/account/publishing/
2. Click: `Add a new pending publisher`
3. Fill in the values above
4. Click: `Add`
5. Done! ✅

## Verify Your Values

**Check repository name:**
```bash
git remote -v
# Should show: github.com/Kevrollin/gitpilot.io
```

**Check package name:**
```bash
grep "name=" setup.py
# Should show: name="auto-commit-assistant"
```

**Check workflow file:**
```bash
ls -la .github/workflows/publish-pypi.yml
# File should exist
```

## After Adding

1. The publisher will show as "pending"
2. Create a GitHub release to trigger the workflow
3. After first successful run, it becomes "verified"
4. Future releases will auto-publish! 🚀

