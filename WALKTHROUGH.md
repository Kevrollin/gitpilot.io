# Interactive Walkthrough - Installing and Using dev.mk

This guide shows you exactly what you'll see at each step.

---

## 📦 Part 1: Installation

### Step 1: Open Your Terminal

Open your terminal application:
- **Linux:** Press `Ctrl+Alt+T` or search for "Terminal"
- **macOS:** Press `Cmd+Space`, type "Terminal", press Enter

### Step 2: Check Prerequisites

Run these commands to check if you have everything you need:

```bash
python3 --version
```

**Expected output:**
```
Python 3.8.10
```
(or any version 3.8 or higher)

```bash
git --version
```

**Expected output:**
```
git version 2.34.1
```
(or any version)

```bash
curl --version
```

**Expected output:**
```
curl 7.68.0
```
(or any version)

✅ **If all three commands work, you're ready to install!**

### Step 3: Install dev.mk

Run the installation command:

```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install-from-drive.sh | bash
```

**What you'll see:**

```
╔═══════════════════════════════════════════════════════╗
║  dev.mk - Auto Commit Assistant                      ║
║  By Kelvin Mukaria                                   ║
║  Installing from Google Drive                        ║
╚═══════════════════════════════════════════════════════╝

✓ Python 3.12.3 found

Downloading package from Google Drive...
Downloading: auto_commit_assistant-1.1.1-py3-none-any.whl
From: Google Drive

################################################## 100.0%
✓ Download completed

Installing auto-commit-assistant...
Using pipx (recommended for CLI tools)...
  installed package auto-commit-assistant 1.1.1, installed using Python 3.12.3
  These apps are now globally available
    - autocommit
✓ Installation completed successfully!

╔═══════════════════════════════════════════════════════╗
║  Installation Complete!                               ║
╚═══════════════════════════════════════════════════════╝

✓ autocommit command is available

Usage:
  autocommit              # Run in a git repository
  autocommit --help       # Show help
  autocommit --version    # Show version

Next steps:
1. Navigate to a git repository:
   cd /path/to/your/project

2. Run dev.mk:
   autocommit

3. (Optional) Set your own Gemini API key for unlimited usage:
   export GEMINI_API_KEY='your-api-key-here'
   echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc

Note: dev.mk works out of the box with a built-in API key.
Set your own key for unlimited usage and better performance.

Happy committing! 🚀
```

**Installation takes about 1-2 minutes.**

### Step 4: Verify Installation

Run:

```bash
autocommit --version
```

**Expected output:**
```
dev.mk 1.1.1
```

✅ **If you see the version number, installation was successful!**

**If you see "command not found":**

Run these commands:

```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Then try again:
```bash
autocommit --version
```

---

## 🎯 Part 2: Using dev.mk

### Step 1: Navigate to Your Project

```bash
cd /path/to/your/project
```

**Example:**
```bash
cd ~/Documents/my-project
cd ~/projects/website
cd /home/username/projects/app
```

### Step 2: Make Some Changes

Edit some files or create new files. For example:

```bash
# Create a new file
echo "Hello, World!" > test.txt

# Or edit an existing file
nano README.md
# (make some changes, save and exit)
```

### Step 3: Run dev.mk

```bash
autocommit
```

**What you'll see:**

```
╔═══════════════════════════════════════════════════════╗
║  dev.mk - Auto Commit Assistant                      ║
║  By Kelvin Mukaria                                   ║
║  2024-11-09 13:00:00                                 ║
╚═══════════════════════════════════════════════════════╝

[1/5] Checking git repository...        ✓
[2/5] Staging changes...                ✓
[3/5] Analyzing changes...              ⏳
[4/5] Generating commit message...      ⏳
[5/5] Commit message generated!         ✓

┌─────────────────────────────────────────────────────┐
│ Generated Commit Message:                           │
│                                                     │
│ Add test.txt file with Hello World message         │
│                                                     │
│ This commit adds a new test.txt file containing    │
│ a simple "Hello, World!" message for testing       │
│ purposes.                                           │
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

### Step 4: Choose an Option

**Option 1: Accept and Continue (Recommended for first time)**
- Type `1` and press Enter
- dev.mk will use the AI-generated message as-is

**Option 2: Edit Message Inline**
- Type `2` and press Enter
- You'll see: `Enter your commit message:`
- Type your message and press Enter

**Option 3: Edit in Editor**
- Type `3` and press Enter
- Your default editor (nano/vim) will open
- Edit the message, save and exit

**Option 4: Enter Manual Message**
- Type `4` and press Enter
- You'll see: `Enter your commit message:`
- Type your message and press Enter

**Option 5: Cancel**
- Type `5` and press Enter
- Installation will be cancelled
- No changes will be committed

### Step 5: See the Results

After you accept (Option 1), you'll see:

```
[6/6] Committing changes...             ✓
[7/7] Pushing to remote...              ✓

✅ Success! Changes committed and pushed.

Commit: abc123def456...
Branch: main
Message: Add test.txt file with Hello World message

Summary:
  Files changed: 1
  Insertions: 1
  Deletions: 0
```

✅ **Done! Your changes are now committed and pushed!**

---

## 🚀 Part 3: Advanced Usage

### Quick Commit (Auto-Accept)

If you trust the AI messages:

```bash
autocommit --yes
```

**What you'll see:**
```
╔═══════════════════════════════════════════════════════╗
║  dev.mk - Auto Commit Assistant                      ║
╚═══════════════════════════════════════════════════════╝

[1/5] Checking git repository...        ✓
[2/5] Staging changes...                ✓
[3/5] Analyzing changes...              ⏳
[4/5] Generating commit message...      ⏳
[5/5] Commit message generated!         ✓
[6/6] Committing changes...             ✓
[7/7] Pushing to remote...              ✓

✅ Success! Changes committed and pushed.
```

**No interaction needed!**

### Dry Run (Test Without Committing)

See what would happen without actually committing:

```bash
autocommit --dry-run
```

**What you'll see:**
```
╔═══════════════════════════════════════════════════════╗
║  dev.mk - Auto Commit Assistant (DRY RUN)            ║
╚═══════════════════════════════════════════════════════╝

[1/5] Checking git repository...        ✓
[2/5] Staging changes...                ✓
[3/5] Analyzing changes...              ⏳
[4/5] Generating commit message...      ⏳
[5/5] Commit message generated!         ✓

┌─────────────────────────────────────────────────────┐
│ Would commit with message:                          │
│                                                     │
│ Add test.txt file with Hello World message         │
│                                                     │
└─────────────────────────────────────────────────────┘

⚠️  DRY RUN: No changes were committed or pushed.
```

### Skip AI (Manual Message)

Write your own commit message:

```bash
autocommit --skip-ai
```

**What you'll see:**
```
╔═══════════════════════════════════════════════════════╗
║  dev.mk - Auto Commit Assistant                      ║
╚═══════════════════════════════════════════════════════╝

[1/5] Checking git repository...        ✓
[2/5] Staging changes...                ✓
[3/5] Skipping AI generation...         ✓

Enter your commit message:
```

Type your message and press Enter.

---

## 🎓 Part 4: Real-World Example

Let's walk through a complete example:

### Scenario: You've Added a New Feature

1. **You've created a new file:**
   ```bash
   echo "function calculateTotal() { return price * quantity; }" > calculator.js
   ```

2. **You've modified an existing file:**
   ```bash
   # Edit main.js to import the calculator
   nano main.js
   # Add: import { calculateTotal } from './calculator.js';
   ```

3. **Run dev.mk:**
   ```bash
   autocommit
   ```

4. **See the AI-generated message:**
   ```
   Add calculator function and integrate into main.js
   
   This commit adds a new calculateTotal function in calculator.js
   and integrates it into the main application by importing it in
   main.js. The function calculates the total price by multiplying
   price and quantity.
   ```

5. **Accept the message (Option 1):**
   - Type `1` and press Enter

6. **See success:**
   ```
   ✅ Success! Changes committed and pushed.
   
   Commit: def456ghi789...
   Branch: main
   Message: Add calculator function and integrate into main.js
   ```

✅ **Your feature is now committed and pushed!**

---

## 📚 What's Next?

### Learn More Commands

```bash
autocommit --help
```

**Shows:**
```
usage: autocommit [-h] [--yes] [--dry-run] [--skip-ai] [--branch BRANCH]
                  [--quiet] [--log LOG] [--theme THEME] [--version]
                  [--update] [--check-updates]

dev.mk - AI-Powered Auto Commit Assistant

options:
  -h, --help            show this help message and exit
  -y, --yes             Auto-accept AI-generated commit messages
  -d, --dry-run         Simulate all operations without committing
  -s, --skip-ai         Skip AI generation and prompt for manual message
  -b BRANCH, --branch BRANCH
                        Commit to a specific branch
  -q, --quiet           Suppress non-essential output
  -l LOG, --log LOG     Log all operations to a file
  -t THEME, --theme THEME
                        Choose UI theme (hacker, minimal, developer)
  -v, --version         Show version information
  -u, --update          Update to the latest version
  --check-updates       Check if updates are available
```

### Set Up Your API Key

For unlimited usage:

```bash
export GEMINI_API_KEY='your-api-key-here'
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

Get your key from: https://makersuite.google.com/app/apikey

### Try Different Themes

```bash
autocommit --theme minimal
autocommit --theme developer
```

---

## ✅ Checklist

Before you start using dev.mk:

- [ ] ✅ Installed dev.mk
- [ ] ✅ Verified installation (`autocommit --version`)
- [ ] ✅ Added to PATH (if needed)
- [ ] ✅ Set API key (optional, but recommended)
- [ ] ✅ Tested in a project
- [ ] ✅ Read the help (`autocommit --help`)
- [ ] ✅ Ready to use!

---

## 🆘 Need Help?

- **Full Guide:** See [USER_GUIDE.md](USER_GUIDE.md)
- **Quick Start:** See [QUICKSTART.md](QUICKSTART.md)
- **Installation:** See [INSTALL.md](INSTALL.md)
- **Troubleshooting:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

**Congratulations! You're ready to use dev.mk! 🎉**

Happy committing! 🚀

