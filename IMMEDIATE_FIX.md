# Immediate Fix - Install dev.mk Now

## 🚀 Quick Fix (You Already Have package.whl)

Since you already downloaded `package.whl`, here's the fastest way to install it:

### Option 1: Rename and Install (Fastest)

```bash
# Rename to correct filename
mv package.whl auto_commit_assistant-1.1.1-py3-none-any.whl

# Install with pipx (if available)
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl

# OR if pipx not available, use pip --user
pip install --user auto_commit_assistant-1.1.1-py3-none-any.whl

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify
autocommit --version
```

### Option 2: Use the Quick Fix Script

```bash
# Download the quick fix script
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/QUICK_FIX.sh -o quick_fix.sh
chmod +x quick_fix.sh
./quick_fix.sh
```

### Option 3: Manual Step-by-Step

```bash
# Step 1: Rename the file
mv package.whl auto_commit_assistant-1.1.1-py3-none-any.whl

# Step 2: Try pipx first (recommended)
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl

# Step 3: If pipx fails, use pip --user
pip install --user auto_commit_assistant-1.1.1-py3-none-any.whl

# Step 4: If --user fails due to externally-managed-environment, use --break-system-packages
pip install --break-system-packages auto_commit_assistant-1.1.1-py3-none-any.whl

# Step 5: Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Step 6: Verify
autocommit --version
```

## ✅ Expected Results

After running the commands above, you should see:

```
✓ Installation successful!
```

Then when you run:
```bash
autocommit --version
```

You should see:
```
dev.mk 1.1.1
```

## 🔧 Troubleshooting

### If pipx says "Invalid wheel filename"

Make sure you renamed the file:
```bash
mv package.whl auto_commit_assistant-1.1.1-py3-none-any.whl
pipx install auto_commit_assistant-1.1.1-py3-none-any.whl
```

### If you get "externally-managed-environment"

Use one of these options:

1. **Use pipx** (best option):
   ```bash
   pipx install auto_commit_assistant-1.1.1-py3-none-any.whl
   ```

2. **Use --user flag**:
   ```bash
   pip install --user auto_commit_assistant-1.1.1-py3-none-any.whl
   ```

3. **Use --break-system-packages** (last resort):
   ```bash
   pip install --break-system-packages auto_commit_assistant-1.1.1-py3-none-any.whl
   ```

### If "command not found: autocommit"

Add to PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Then verify:
```bash
autocommit --version
```

## 🎯 Complete Working Command Sequence

Copy and paste this entire block:

```bash
# Rename file
mv package.whl auto_commit_assistant-1.1.1-py3-none-any.whl

# Install (tries pipx first, then pip --user, then --break-system-packages)
if command -v pipx &> /dev/null; then
    pipx install auto_commit_assistant-1.1.1-py3-none-any.whl --force
elif pip install --user auto_commit_assistant-1.1.1-py3-none-any.whl 2>/dev/null; then
    echo "Installed with pip --user"
else
    pip install --break-system-packages auto_commit_assistant-1.1.1-py3-none-any.whl
fi

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify
autocommit --version

# Clean up
rm -f auto_commit_assistant-1.1.1-py3-none-any.whl
```

## 📝 What Each Command Does

1. **`mv package.whl auto_commit_assistant-1.1.1-py3-none-any.whl`**
   - Renames the file to the correct wheel filename
   - pipx needs the actual package name in the filename

2. **`pipx install ...`**
   - Installs in an isolated environment (recommended)
   - Avoids externally-managed-environment issues

3. **`pip install --user ...`**
   - Installs to user directory
   - Avoids system-wide installation issues

4. **`pip install --break-system-packages ...`**
   - Last resort option
   - Only use if other methods fail

5. **`export PATH=...`**
   - Adds installation directory to PATH
   - Makes `autocommit` command available

6. **`autocommit --version`**
   - Verifies installation worked
   - Should show version number

## 🎉 Success!

Once you see `dev.mk 1.1.1` from `autocommit --version`, you're ready to use dev.mk!

### Next Steps

1. **Navigate to a project:**
   ```bash
   cd /path/to/your/project
   ```

2. **Use dev.mk:**
   ```bash
   autocommit
   ```

3. **Learn more:**
   ```bash
   autocommit --help
   ```

---

**Need more help?** See [INSTALL_FIX.md](INSTALL_FIX.md) or [USER_GUIDE.md](USER_GUIDE.md)

