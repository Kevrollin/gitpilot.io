# What to Share With Developers

## ✅ You're All Set!

Your code is now ready for developers to install and use. Here's what to share:

## 📤 Share This Message With Your Team

### Option 1: Copy-Paste Email/Slack Message

```
Hey team! 👋

I've set up Gitpilot - an AI-powered auto-commit assistant that makes committing code super easy.

🚀 Quick Install (one-time):
pip install git+https://github.com/Kevrollin/gitpilot.io.git

🔑 Set your API key:
export GEMINI_API_KEY="your-api-key-here"
(Get your key from: https://makersuite.google.com/app/apikey)

💻 Use it in any project:
cd your-project
autocommit

That's it! Gitpilot will automatically stage, generate commit messages, commit, and push.

🔄 To update when I push new versions:
autocommit --update

Full docs: https://github.com/Kevrollin/gitpilot.io
```

### Option 2: Share the Quick Start Guide

Point developers to the `QUICKSTART.md` file in your repository:
- https://github.com/Kevrollin/gitpilot.io/blob/main/QUICKSTART.md

### Option 3: Share the Developer Guide

Point developers to the `DEVELOPER_GUIDE.md` file:
- https://github.com/Kevrollin/gitpilot.io/blob/main/DEVELOPER_GUIDE.md

## 📍 Where Developers Should Run Commands

### Installation (Run Once, Anywhere)
- Developers can run the install command from **any directory**
- It installs Gitpilot globally on their system
- Command: `pip install git+https://github.com/Kevrollin/gitpilot.io.git`

### Using Gitpilot (In Project Directories)
- Developers navigate to their **project directory** (where their git repo is)
- Then run: `autocommit`
- Gitpilot will automatically detect the git repository and work with it

### Setting API Key
- **System-wide**: Add to `~/.bashrc` or `~/.zshrc` (affects all projects)
- **Project-specific**: Create a `.env` file in the project directory (only affects that project)

## 🔄 How Updates Work

1. **You push updates** to the repository
2. **Developers run**: `autocommit --update`
3. **Gitpilot automatically** pulls the latest version and reinstalls

That's it! No manual steps needed.

## 📝 Files You Created

- ✅ `QUICKSTART.md` - Quick start guide for developers
- ✅ `DEVELOPER_GUIDE.md` - Copy-paste guide to share
- ✅ `INSTALL.md` - Detailed installation guide
- ✅ `install.sh` - One-click install script
- ✅ Updated `README.md` - Main documentation
- ✅ `auto_commit/updater.py` - Auto-update functionality

## 🎯 Next Steps

1. **Push all changes** to your repository
2. **Share the installation command** with your team
3. **When you make updates**, developers just run `autocommit --update`

## 💡 Tips

- Make sure the `install.sh` script is in the root of your repository
- The repository URL is already configured in the code
- Developers can check for updates anytime with `autocommit --check-updates`
- The tool works in any git repository once installed

## ❓ Common Questions

**Q: Where do developers install it?**
A: Anywhere - it installs globally. Then they use it in their project directories.

**Q: How do they update?**
A: Just run `autocommit --update` whenever you push new changes.

**Q: Do they need to reinstall?**
A: No! The `--update` command handles everything automatically.

**Q: What if the repository URL changes?**
A: Developers can set `GITPILOT_REPO_URL` environment variable to override the default.

---

**You're ready to go! 🚀**

Share the installation command and your team can start using Gitpilot immediately.

