# Gitpilot - Auto Commit Assistant

A powerful Python CLI tool that automatically stages all changes in a Git repository, analyzes the diffs using Google's Gemini API, generates clean and professional commit messages, commits the changes, and pushes them to the remote repository. All with a single command: `autocommit`.

## Features

- 🤖 **AI-Powered Commit Messages**: Uses Google Gemini API to generate intelligent, context-aware commit messages
- 📦 **Automatic Staging**: Automatically stages all changes in the repository
- 🔍 **Smart Analysis**: Analyzes git diffs to understand what changed
- 💾 **Auto Commit & Push**: Commits and pushes changes automatically
- ✅ **Graceful Handling**: Exits cleanly if there are no changes to commit
- 🎨 **Clean CLI Output**: Beautiful output with emojis and helpful messages
- 🐧 **Cross-Platform**: Compatible with Linux and macOS

## Installation

### Recommended: Using a Virtual Environment

**Yes, using a virtual environment is strongly recommended!** This keeps the project dependencies isolated from your system Python packages and prevents conflicts.

1. **Navigate to the project directory:**
   ```bash
   cd auto_commit_assistant
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   
   **Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```
   
   You'll see `(venv)` in your terminal prompt when it's active.

4. **Install the package and dependencies:**
   ```bash
   pip install -e .
   ```
   
   This will automatically install all dependencies from `requirements.txt`.

5. **Set up your Gemini API key:**
   
   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey) or [Google Cloud Console](https://console.cloud.google.com/).
   
   You can set it up in one of these ways:
   
   **Option 1: Using a .env file (Recommended for projects):**
   ```bash
   echo 'GEMINI_API_KEY=your-api-key-here' > .env
   ```
   
   Create a `.env` file in your project directory with your API key. This file is already in `.gitignore`, so it won't be committed.
   
   **Option 2: Environment variable (Current session only):**
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
   
   **Option 3: Persistent environment variable:**
   ```bash
   echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
   source ~/.bashrc
   ```
   
   The tool will automatically load from a `.env` file if it exists in your project directory, or from environment variables.

6. **Deactivate the virtual environment when done (optional):**
   ```bash
   deactivate
   ```

**Note:** Remember to activate the virtual environment (`source venv/bin/activate`) each time you want to use the `autocommit` command, or the command won't be available.

### Alternative: Install Without Virtual Environment

If you prefer not to use a virtual environment (not recommended), you can install directly:

```bash
cd auto_commit_assistant
pip install -e .
```

**Warning:** This installs packages system-wide and may cause conflicts with other Python projects.

## Usage

**Important:** Make sure your virtual environment is activated (if you're using one):
```bash
source venv/bin/activate
```

1. **Navigate to your project directory:**
   ```bash
   cd /path/to/your/project
   ```

2. **Run the autocommit command:**
   ```bash
   autocommit
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

### Normal Usage

Once a git repository is set up, the tool will:
- Stage all your changes
- Analyze the diffs
- Generate a commit message using AI
- Commit the changes
- Push to the remote repository

If there are no changes, it will exit gracefully with a message.

## How It Works

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
6. **Commit**: Commits the changes with the generated message
7. **Push**: Pushes the changes to the remote repository (sets upstream if needed)

## Project Structure

```
auto_commit_assistant/
│
├── auto_commit/
│   ├── __init__.py
│   ├── main.py          # Main orchestration logic
│   ├── git_handler.py   # Git operations
│   └── ai_commit.py     # AI commit message generation
│
├── cli.py               # CLI entry point
├── setup.py             # Package configuration
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Requirements

- Python 3.8 or higher
- Git installed and configured
- Google Gemini API key
- `google-generativeai` library

## Error Handling

The tool includes comprehensive error handling:
- Validates that `GEMINI_API_KEY` is set
- Checks if Git commands succeed
- Handles empty diffs gracefully
- Provides clear error messages

## Testing

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
   - It should stage, commit, and push your changes

## Troubleshooting

### "GEMINI_API_KEY environment variable is not set"
Make sure you've exported the API key as an environment variable. See the Installation section above.

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

## License

MIT License

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Author

Gitpilot

---

**Note**: The tool will automatically detect if you're in a Git repository. If not, it will prompt you to set one up, so you can use `autocommit` in any directory!

