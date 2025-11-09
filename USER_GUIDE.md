# User Guide - Step-by-Step Installation & Usage

Welcome! This guide will walk you through installing and using dev.mk Auto Commit Assistant step by step.

## 📋 Prerequisites

Before you start, make sure you have:
- ✅ A computer running Linux or macOS
- ✅ Python 3.8 or higher installed
- ✅ Git installed (usually comes with most systems)
- ✅ Internet connection

### Check if you have Python

Open your terminal and run:
```bash
python3 --version
```

You should see something like: `Python 3.8.x` or higher.

If you don't have Python, install it:
- **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install python3 python3-pip`
- **macOS:** `brew install python3`

### Check if you have Git

Run:
```bash
git --version
```

You should see something like: `git version 2.x.x`

If you don't have Git, install it:
- **Linux (Ubuntu/Debian):** `sudo apt install git`
- **macOS:** `brew install git`

---

## 🚀 Step 1: Install dev.mk

### Option A: Easy One-Command Installation (Recommended)

Open your terminal and run this single command:

```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

**What this does:**
- Downloads the installation script
- Downloads the package from Google Drive
- Installs it automatically
- Sets everything up for you

**What you'll see:**
```
╔═══════════════════════════════════════════════════════╗
║  dev.mk - Auto Commit Assistant                      ║
║  By Kelvin Mukaria                                   ║
║  Installing from Google Drive                        ║
╚═══════════════════════════════════════════════════════╝

✓ Python 3.x.x found

Downloading package from Google Drive...
Downloading: auto_commit_assistant-1.1.1-py3-none-any.whl
✓ Download completed

Installing auto-commit-assistant...
✓ Installation completed successfully!
```

**This may take 1-2 minutes depending on your internet speed.**

---

### Option B: Manual Installation

If the one-command installation doesn't work, follow these steps:

#### Step 1.1: Download the Package

```bash
curl -L "https://drive.google.com/uc?export=download&id=1A1fNt_FyfvHcjtN18v5NzBYMEVy7L6Lg" -o package.whl
```

**What you'll see:**
- A progress bar showing the download
- File saved as `package.whl` in your current directory

#### Step 1.2: Install the Package

**If you have pipx (recommended for CLI tools):**
```bash
pipx install package.whl
```

**Or if you have pip:**
```bash
pip install --user package.whl
```

**What you'll see:**
```
Installing collected packages: auto-commit-assistant
Successfully installed auto-commit-assistant-1.1.1
```

#### Step 1.3: Clean Up (Optional)

Remove the downloaded file:
```bash
rm package.whl
```

---

## ✅ Step 2: Verify Installation

After installation, verify it works:

```bash
    autocommit --version
```

**You should see:**
```
dev.mk 1.1.1
```

**If you see "command not found":**

This means the installation directory is not in your PATH. Fix it by running:

```bash
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Make it permanent (add to your shell config)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Reload your shell configuration
source ~/.bashrc
```

**Then try again:**
```bash
autocommit --version
```

---

## 🔧 Step 3: Set Up Your API Key (Optional)

dev.mk works out of the box with a built-in API key, but you can set your own for unlimited usage.

### Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Set the API Key

**Option 1: For a single session (temporary)**
```bash
export GEMINI_API_KEY='your-api-key-here'
```

**Option 2: Permanent (recommended)**
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Option 3: For a specific project**
Create a `.env` file in your project directory:
```bash
echo 'GEMINI_API_KEY=your-api-key-here' > .env
```

---

## 📖 Step 4: Using dev.mk

### Basic Usage

#### Step 4.1: Navigate to Your Project

```bash
cd /path/to/your/project
```

**Example:**
```bash
cd ~/Documents/my-project
```

#### Step 4.2: Make Some Changes

Edit some files in your project, or create new files. For example:
```bash
echo "Hello, World!" > test.txt
```

#### Step 4.3: Run dev.mk

```bash
autocommit
```

**What you'll see:**
```
╔═══════════════════════════════════════════════════════╗
║  dev.mk - Auto Commit Assistant                      ║
║  By Kelvin Mukaria                                   ║
║  [Timestamp]                                         ║
╚═══════════════════════════════════════════════════════╝

[1/5] Checking git repository... ✓
[2/5] Staging changes... ✓
[3/5] Analyzing changes... ⏳
[4/5] Generating commit message... ⏳
[5/5] Commit message generated!

┌─────────────────────────────────────────────────────┐
│ Generated Commit Message:                           │
│                                                     │
│ Add test.txt file with Hello World message         │
│                                                     │
└─────────────────────────────────────────────────────┘

What would you like to do?
1. Accept and continue
2. Edit message inline
3. Edit in editor
4. Enter manual message
5. Cancel

Enter choice [1-5]: 
```

#### Step 4.4: Choose an Option

- **Option 1:** Press `1` and Enter to accept the AI-generated message
- **Option 2:** Press `2` to edit the message directly
- **Option 3:** Press `3` to open in your text editor
- **Option 4:** Press `4` to write your own message
- **Option 5:** Press `5` to cancel

#### Step 4.5: Commit and Push

After accepting, dev.mk will:
- Commit your changes
- Push to the remote repository

**You'll see:**
```
[6/6] Committing changes... ✓
[7/7] Pushing to remote... ✓

✅ Success! Changes committed and pushed.
```

---

## 🎯 Common Use Cases

### Use Case 1: Quick Commit with Auto-Accept

If you trust the AI-generated messages, use the `--yes` flag:

```bash
autocommit --yes
```

This automatically accepts the AI message without showing the preview.

### Use Case 2: See What Would Happen (Dry Run)

Test what dev.mk would do without actually committing:

```bash
autocommit --dry-run
```

### Use Case 3: Skip AI and Enter Manual Message

If you prefer to write your own commit message:

```bash
autocommit --skip-ai
```

### Use Case 4: Commit to a Specific Branch

Commit to a different branch:

```bash
autocommit --branch feature/new-feature
```

This will create the branch if it doesn't exist.

### Use Case 5: Quiet Mode (for Scripts)

Suppress output for automation:

```bash
autocommit --quiet
```

---

## 🆘 Troubleshooting

### Problem: "command not found: autocommit"

**Solution:**
```bash
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Problem: "Not a git repository"

**Solution:**
Initialize a git repository first:
```bash
git init
git remote add origin https://github.com/yourusername/yourrepo.git
```

Or navigate to an existing git repository.

### Problem: "No changes to commit"

**Solution:**
This is normal! It means all your changes are already committed. Make some changes to files, then run `autocommit` again.

### Problem: "GEMINI_API_KEY not found"

**Solution:**
dev.mk works without an API key (uses built-in key), but if you see this error:
1. Set your API key (see Step 3 above)
2. Or the built-in key may have reached its limit - set your own key

### Problem: "Permission denied"

**Solution:**
Make sure you have write permissions to the repository:
```bash
# Check permissions
ls -la

# Fix if needed
chmod -R u+w .
```

### Problem: "Failed to push"

**Solution:**
1. Check your git remote is set:
   ```bash
   git remote -v
   ```

2. Make sure you have push access to the repository

3. Set upstream branch:
   ```bash
   git push -u origin main
   ```

---

## 📚 Advanced Usage

### View All Options

```bash
autocommit --help
```

### Change Theme

```bash
autocommit --theme minimal
autocommit --theme developer
```

### Enable Logging

```bash
autocommit --log autocommit.log
```

This creates a log file with all operations.

### Combine Flags

```bash
autocommit --yes --branch feature/new --log commits.log --theme minimal
```

---

## 🎉 Congratulations!

You've successfully installed and used dev.mk Auto Commit Assistant!

### Next Steps

1. **Try it in your projects:** Use `autocommit` in any git repository
2. **Set up your API key:** For unlimited usage
3. **Explore features:** Try different flags and options
4. **Read the docs:** Check `README.md` for more information

### Getting Help

- **Documentation:** See `README.md` and `INSTALL.md`
- **Issues:** Report problems on GitHub
- **FAQ:** Check `FAQ.md` for common questions

---

## 📝 Quick Reference

### Installation
```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

### Basic Usage
```bash
cd /path/to/your/project
autocommit
```

### Common Commands
```bash
autocommit --yes              # Auto-accept AI message
autocommit --dry-run          # Test without committing
autocommit --skip-ai          # Manual commit message
autocommit --branch <name>    # Commit to specific branch
autocommit --help             # Show help
autocommit --version          # Show version
```

### Update dev.mk
```bash
autocommit --update
```

---

**Happy committing! 🚀**

For more information, visit: https://github.com/Kevrollin/gitpilot.io

