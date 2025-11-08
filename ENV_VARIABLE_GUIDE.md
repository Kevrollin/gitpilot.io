# Environment Variable Management Guide

## How to Remove/Undo GEMINI_API_KEY

### If Set in Current Terminal Session

**To remove it from current session:**
```bash
unset GEMINI_API_KEY
```

**To verify it's removed:**
```bash
echo $GEMINI_API_KEY
# Should output nothing (empty)
```

### If Set in Shell Config File (Permanent)

**Check if it's in your config files:**
```bash
# Check ~/.bashrc
grep GEMINI_API_KEY ~/.bashrc

# Check ~/.zshrc (if using zsh)
grep GEMINI_API_KEY ~/.zshrc

# Check ~/.profile
grep GEMINI_API_KEY ~/.profile
```

**Remove it:**
```bash
# Edit the file
nano ~/.bashrc
# or
nano ~/.zshrc

# Find the line that says:
# export GEMINI_API_KEY="your-api-key-here"

# Delete that line, save and exit

# Reload the shell config
source ~/.bashrc
# or
source ~/.zshrc
```

**Or use sed to remove it automatically:**
```bash
# Remove from ~/.bashrc
sed -i '/GEMINI_API_KEY/d' ~/.bashrc
source ~/.bashrc

# Remove from ~/.zshrc
sed -i '/GEMINI_API_KEY/d' ~/.zshrc
source ~/.zshrc
```

### If Set in .env File (Project-Specific)

**Remove the .env file or edit it:**
```bash
# Delete the file
rm .env

# Or edit it to remove the line
nano .env
# Remove the line: GEMINI_API_KEY=your-api-key-here
```

### Complete Cleanup

**To completely remove it from all places:**
```bash
# 1. Unset in current session
unset GEMINI_API_KEY

# 2. Remove from shell config files
sed -i '/GEMINI_API_KEY/d' ~/.bashrc
sed -i '/GEMINI_API_KEY/d' ~/.zshrc
sed -i '/GEMINI_API_KEY/d' ~/.profile

# 3. Remove .env file if exists
rm -f .env

# 4. Start a new terminal session
# (Close and reopen terminal)
```

### Verify It's Removed

```bash
# Check if variable exists
env | grep GEMINI_API_KEY
# Should output nothing

# Check current value
echo $GEMINI_API_KEY
# Should output nothing
```

## Notes

- **dev.mk works without API key** - it has a built-in key
- **Setting your own key is optional** - only needed for unlimited usage
- **Removing the key** will make dev.mk use the built-in key
- **New terminal sessions** won't have the variable after removal

## Quick Reference

```bash
# Remove from current session
unset GEMINI_API_KEY

# Remove from ~/.bashrc permanently
sed -i '/GEMINI_API_KEY/d' ~/.bashrc && source ~/.bashrc

# Check if it exists
echo $GEMINI_API_KEY
```

