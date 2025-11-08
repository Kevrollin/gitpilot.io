# Updating dev.mk - User Guide

## How Updates Work

### If Installed with pipx

**Users who installed with:**
```bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
```

**Need to update manually with pipx:**

```bash
# Update to latest version
pipx upgrade auto-commit-assistant

# Or reinstall from git (gets latest)
pipx reinstall git+https://github.com/Kevrollin/gitpilot.io.git
```

**The `autocommit --update` command may not work with pipx installations** because pipx manages its own virtual environments.

### If Installed with pip

**Users who installed with:**
```bash
pip install --user git+https://github.com/Kevrollin/gitpilot.io.git
```

**Can update using:**
```bash
# Option 1: Use autocommit --update (if it works)
autocommit --update

# Option 2: Update manually with pip
pip install --user --upgrade git+https://github.com/Kevrollin/gitpilot.io.git

# Option 3: Reinstall
pip install --user --upgrade --force-reinstall git+https://github.com/Kevrollin/gitpilot.io.git
```

## Updating to Specific Version

**To update to a specific release:**
```bash
# Using pipx
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3

# Using pip
pip install --user --upgrade git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3
```

## Do Users Need to Reinstall?

### Answer: **Yes, they need to update/reinstall to get new changes**

**Why:**
- pipx/pip installs a specific version of the code
- New updates are in the repository, not in their installed version
- They need to fetch and install the new version

**When updates are available:**
1. **You push new code** to the repository
2. **You create a new release** (e.g., v0.1.3)
3. **Users need to update** their installation to get the new version

### How Users Know to Update

**Option 1: Check for updates:**
```bash
autocommit --check-updates
```

**Option 2: Manual check:**
- Users check GitHub releases page
- Users see announcement
- Users notice new features

### Updating Process for Users

**For pipx users:**
```bash
# Check current version
autocommit --version

# Update to latest
pipx upgrade auto-commit-assistant

# Or reinstall from git
pipx reinstall git+https://github.com/Kevrollin/gitpilot.io.git
```

**For pip users:**
```bash
# Check current version
autocommit --version

# Update to latest
pip install --user --upgrade git+https://github.com/Kevrollin/gitpilot.io.git

# Or use autocommit --update (if it works)
autocommit --update
```

## After Updating

**Users should:**
1. Verify new version: `autocommit --version`
2. Test it works: `autocommit --help`
3. Use new features

## Important Notes

- **Just running `autocommit`** will use the currently installed version
- **To get updates**, users must update/reinstall
- **Updates don't happen automatically** - users need to update manually
- **New releases** require users to update their installation

## Making Updates Easier

### Option 1: Improve --update command

Update the `--update` command to detect pipx installations and use `pipx upgrade`:

```python
# In updater.py, detect installation method
# If pipx: use pipx upgrade
# If pip: use pip install --upgrade
```

### Option 2: Add update notification

Show a message when updates are available:
```python
# Check for updates on startup
# If new version available, notify user
# Prompt to update
```

### Option 3: Auto-update (advanced)

Create a background service that checks for updates and notifies users.

## Current Behavior

**What happens now:**
1. User installs: `pipx install git+https://github.com/Kevrollin/gitpilot.io.git`
2. Gets version 0.1.2 (or whatever is latest)
3. You release v0.1.3 with new features
4. User runs `autocommit` → **still uses v0.1.2** (old version)
5. User needs to run: `pipx upgrade auto-commit-assistant` → **gets v0.1.3**

**The `autocommit --update` command:**
- May work for pip installations
- May not work properly for pipx installations
- Should be improved to handle both cases

## Recommendations

1. **Document update process** clearly in README
2. **Improve --update command** to handle pipx
3. **Add version check** on startup (optional)
4. **Notify users** when updates are available

---

## Quick Answer

**Q: Do users need to reinstall for updates?**  
**A: Yes, they need to update/reinstall. Just running `autocommit` uses the currently installed version.**

**Q: How do they update?**  
**A: `pipx upgrade auto-commit-assistant` (for pipx) or `autocommit --update` (for pip)**

