# Gitpilot - Auto Commit Assistant

A powerful, interactive Python CLI tool that automatically stages all changes in a Git repository, analyzes the diffs using Google's Gemini API, generates clean and professional commit messages, commits the changes, and pushes them to the remote repository. Features a hacker/dev-inspired Rich terminal UI with spinners, progress bars, and interactive commit message preview.

## ✨ Features

- 🎨 **Rich Interactive Terminal UI**: Beautiful hacker/dev-inspired interface with spinners, progress bars, panels, and banners
- 🤖 **AI-Powered Commit Messages**: Uses Google Gemini API to generate intelligent, context-aware commit messages
- 📦 **Automatic Staging**: Automatically stages all changes in the repository
- 🔍 **Smart Analysis**: Analyzes git diffs to understand what changed
- 💾 **Interactive Preview**: Preview, edit, or manually enter commit messages before committing
- 🚀 **Auto Commit & Push**: Commits and pushes changes automatically
- ✅ **Graceful Handling**: Exits cleanly if there are no changes to commit
- 🎯 **CLI Flags**: Full automation support with `--yes`, `--dry-run`, `--skip-ai`, `--branch`, `--quiet`, `--log`
- 📝 **File Logging**: Optional logging to file for debugging and audit trails
- 🎨 **Multiple Themes**: Choose from `hacker`, `minimal`, or `developer` themes
- 🐧 **Cross-Platform**: Compatible with Linux and macOS

## 📸 Screenshots

The tool features a beautiful terminal interface with:
- ASCII banner with timestamp
- Step-by-step progress indicators
- Spinners during network operations
- Rich panels for commit message preview
- Interactive prompts for editing messages
- Summary tables showing workflow status

## 🚀 Installation

### Quick Install (Recommended)

**Install directly from the Git repository** (recommended for easy updates):

```bash
pip install git+https://github.com/Kevrollin/gitpilot.io.git
```

Or use the install script:

```bash
curl -fsSL https://raw.githubusercontent.com/Kevrollin/gitpilot.io/main/install.sh | bash
```

### Alternative: Local Development Installation

If you want to develop or customize Gitpilot:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kevrollin/gitpilot.io.git
   cd gitpilot.io
   ```

2. **Install in development mode:**
   ```bash
   pip install -e .
   ```

### Set Up Your Gemini API Key

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey) or [Google Cloud Console](https://console.cloud.google.com/).

**Option 1: Using a .env file (Recommended for projects):**
```bash
echo 'GEMINI_API_KEY=your-api-key-here' > .env
```

**Option 2: Environment variable:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Option 3: Persistent environment variable:**
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

The tool will automatically load from a `.env` file if it exists in your project directory, or from environment variables.

## 🔄 Updating Gitpilot

### Automatic Update

Update to the latest version:

```bash
autocommit --update
```

### Check for Updates

Check if updates are available:

```bash
autocommit --check-updates
```

### Manual Update

If you installed from git, update manually:

```bash
pip install --upgrade --force-reinstall git+https://github.com/Kevrollin/gitpilot.io.git
```

**Note:** After updating, restart your terminal or run `hash -r` to refresh command cache.

### Configure Repository URL

If you're using a custom or private repository, set the repository URL:

```bash
export GITPILOT_REPO_URL="https://github.com/Kevrollin/gitpilot.io.git"
```

Add this to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.) to make it permanent.

## 📖 Usage

### Basic Usage

1. **Navigate to your project directory:**
   ```bash
   cd /path/to/your/project
   ```

2. **Run the autocommit command:**
   ```bash
   autocommit
   ```

That's it! The tool will:
- Display a beautiful banner
- Show step-by-step progress
- Stage all your changes
- Analyze the diffs
- Generate a commit message using AI
- Show an interactive preview where you can accept, edit, or replace the message
- Commit the changes
- Push to the remote repository

### Interactive Commit Message Preview

After AI generates a commit message, you'll see an interactive preview with options:

1. **Accept and continue** - Use the AI-generated message as-is
2. **Edit message inline** - Modify the message directly in the terminal
3. **Edit in editor** - Open your `$EDITOR` (default: nano) to edit the message
4. **Enter manual message** - Replace with your own commit message
5. **Cancel** - Exit without committing

### CLI Flags

The tool supports various CLI flags for automation and customization:

#### `--yes` / `-y`
Auto-accept AI-generated commit messages without preview:
```bash
autocommit --yes
```

#### `--dry-run` / `-d`
Simulate all operations without committing or pushing:
```bash
autocommit --dry-run
```

#### `--skip-ai` / `-s`
Skip AI generation and prompt for manual commit message:
```bash
autocommit --skip-ai
```

#### `--branch` / `-b <name>`
Commit to a specific branch (will create if it doesn't exist):
```bash
autocommit --branch feature/new-feature
```

#### `--quiet` / `-q`
Suppress non-essential output (useful for scripting):
```bash
autocommit --quiet
```

#### `--log` / `-l <file>`
Log all operations to a specified file:
```bash
autocommit --log autocommit.log
```

#### `--theme` / `-t <theme>`
Choose UI theme: `hacker` (default), `minimal`, or `developer`:
```bash
autocommit --theme minimal
autocommit --theme developer
```

#### `--version` / `-v`
Show version information:
```bash
autocommit --version
```

#### `--update` / `-u`
Update Gitpilot to the latest version:
```bash
autocommit --update
```

#### `--check-updates`
Check if updates are available:
```bash
autocommit --check-updates
```

### Usage Examples

**Interactive mode with AI:**
```bash
autocommit
```

**Auto-accept AI messages:**
```bash
autocommit --yes
```

**Dry run to see what would happen:**
```bash
autocommit --dry-run
```

**Skip AI and enter manual message:**
```bash
autocommit --skip-ai
```

**Commit to specific branch:**
```bash
autocommit --branch feature/add-login
```

**Quiet mode with logging:**
```bash
autocommit --quiet --log commits.log
```

**Use minimal theme:**
```bash
autocommit --theme minimal
```

**Combine flags:**
```bash
autocommit --yes --branch main --log commits.log --theme developer
```

### First-Time Setup

If the directory is **not** a Git repository, the tool will:
- ⚠️ Detect that no git repo exists
- 📝 Prompt you to enter a Git repository URL
- 🔧 Initialize a new git repository
- 🔗 Add the remote URL as `origin` (if provided)
- 📦 Stage all files in the directory
- 🤖 Generate an AI-powered commit message based on all files
- 💾 Create an initial commit with the AI-generated message
- 🚀 Push to the remote repository (if URL was provided)

**You can:**
- Enter a full URL: `https://github.com/username/repo.git`
- Enter a simplified URL: `github.com/username/repo` (will be converted to https)
- Press Enter to skip and initialize without a remote (you can add it later)

**Note:** For new repositories, the tool will create an initial commit with an AI-generated message based on all your files. It won't check for "changes" since everything is new.

## 🏗️ Project Structure

```
auto_commit_assistant/
│
├── auto_commit/
│   ├── __init__.py
│   ├── main.py          # Main orchestration logic with Rich UI
│   ├── git_ops.py       # Git operations (refactored, no prints)
│   ├── ai.py            # AI commit message generation (refactored)
│   ├── ui.py            # Rich terminal UI components
│   ├── logger.py        # Logging module
│   └── git_handler.py   # Legacy (deprecated, use git_ops.py)
│
├── cli.py               # CLI entry point with argparse
├── setup.py             # Package configuration
├── requirements.txt     # Dependencies
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## 🔧 How It Works

### For New Repositories (First-Time Setup):
1. **Detect No Repo**: Detects that no git repository exists
2. **Prompt for URL**: Asks user for a git repository URL (optional)
3. **Initialize Repo**: Initializes git repository and adds remote if URL provided
4. **Stage All Files**: Stages all files in the directory (`git add .`)
5. **Generate AI Message**: Analyzes all files and generates an initial commit message using AI
6. **Initial Commit**: Creates the initial commit with the AI-generated message
7. **Push**: Pushes to remote repository (if URL was provided)

### For Existing Repositories:
1. **Check Git Repo**: Verifies git repository exists
2. **Stage Changes**: Runs `git add .` to stage all changes
3. **Get Diff**: Retrieves the staged diff using `git diff --cached`
4. **Check for Changes**: If no changes are found, exits gracefully
5. **Generate Message**: Sends the diff to Gemini API to generate a commit message
6. **Preview Message**: Shows interactive preview with edit options
7. **Commit**: Commits the changes with the final message
8. **Push**: Pushes the changes to the remote repository (sets upstream if needed)

## 📋 Requirements

- Python 3.8 or higher
- Git installed and configured
- Google Gemini API key
- `google-generativeai` library
- `python-dotenv` library
- `rich` library (for terminal UI)

## 🐛 Error Handling

The tool includes comprehensive error handling:
- Validates that `GEMINI_API_KEY` is set
- Checks if Git commands succeed
- Handles empty diffs gracefully
- Provides clear error messages with Rich formatting
- Logs all operations for debugging
- Graceful fallbacks if AI generation fails

## 🧪 Testing

To test the installation:

1. **Make sure you're in a Git repository:**
   ```bash
   cd /path/to/your/git/repo
   ```

2. **Activate your virtual environment (if using one):**
   ```bash
   source /path/to/auto_commit_assistant/venv/bin/activate
   ```

3. **Run the autocommit command:**
   ```bash
   autocommit
   ```

4. **Test with no changes:**
   - Run `autocommit` in a clean repo (no uncommitted changes)
   - It should exit gracefully with: "✅ No changes to commit."

5. **Test with changes:**
   - Make a small change to any file
   - Run `autocommit`
   - It should stage, show preview, commit, and push your changes

6. **Test dry run:**
   ```bash
   autocommit --dry-run
   ```
   - Should simulate all operations without actually committing/pushing

## 🐛 Troubleshooting

### "GEMINI_API_KEY not found"
Make sure you've set the API key using one of the methods in the Installation section above.

### "Git command failed"
- If you're not in a Git repository, the tool will automatically prompt you to set one up
- If you're already in a Git repository, ensure Git is properly configured
- Check that you have write permissions to the repository

### "No changes to commit"
This is normal! The tool detected that there are no changes to commit and exits gracefully.

### "command not found: autocommit"
Make sure:
- You've installed the package with `pip install -e .`
- Your virtual environment is activated (if using one)
- The virtual environment's `bin` directory is in your PATH

### "Failed to generate commit message"
- Check your internet connection
- Verify your API key is valid and has access to Gemini models
- Check the log file (if using `--log`) for detailed error messages
- Try using `--skip-ai` to enter a manual commit message

### Rich UI not displaying correctly
- Make sure your terminal supports ANSI colors
- Try using a different theme: `--theme minimal`
- Check terminal compatibility (works best with modern terminals like iTerm2, Terminator, etc.)

## 🎨 Themes

The tool supports three themes:

- **hacker** (default): Green/cyan colors, hacker/dev aesthetic
- **minimal**: Blue/white colors, clean and minimal
- **developer**: Cyan/magenta colors, modern developer style

Choose a theme with the `--theme` flag:
```bash
autocommit --theme minimal
```

## 📝 Logging

Enable file logging with the `--log` flag:
```bash
autocommit --log autocommit.log
```

The log file will contain:
- All git commands executed
- AI API requests and responses
- Workflow steps and status
- Error messages and stack traces
- Timestamps for all operations

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

MIT License

## 👤 Author

Gitpilot

---

**Note**: The tool will automatically detect if you're in a Git repository. If not, it will prompt you to set one up, so you can use `autocommit` in any directory!

**Happy committing! 🚀**
