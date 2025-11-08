# Troubleshooting Installation Issues

## Repository Access Issues

### Error: "could not read Username for 'https://github.com'"

This error occurs when:
1. The repository is **private**
2. Authentication is required
3. Repository doesn't exist at the URL

### Solution 1: Make Repository Public (Recommended)

The easiest solution is to make your repository public:

1. Go to: https://github.com/Kevrollin/gitpilot.io/settings
2. Scroll down to "Danger Zone"
3. Click "Change repository visibility"
4. Select "Make public"
5. Confirm

Then users can install with:
```bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
```

### Solution 2: Use SSH (For Private Repos)

If you want to keep the repository private, users need to use SSH:

1. **Set up SSH keys** (if not already):
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ssh-add ~/.ssh/id_ed25519
   ```

2. **Add SSH key to GitHub**:
   - Copy public key: `cat ~/.ssh/id_ed25519.pub`
   - Go to: https://github.com/settings/keys
   - Add new SSH key

3. **Change remote URL to SSH**:
   ```bash
   git remote set-url origin git@github.com:Kevrollin/gitpilot.io.git
   ```

4. **Users install with SSH**:
   ```bash
   pipx install git+ssh://git@github.com/Kevrollin/gitpilot.io.git
   ```

### Solution 3: Use Personal Access Token (For Private Repos)

Users can use a Personal Access Token:

1. **Create a token**:
   - Go to: https://github.com/settings/tokens
   - Generate new token (classic)
   - Select `repo` scope
   - Copy the token

2. **Install with token**:
   ```bash
   pipx install git+https://<TOKEN>@github.com/Kevrollin/gitpilot.io.git
   ```

   Or set it as environment variable:
   ```bash
   export GITHUB_TOKEN=your_token_here
   pipx install git+https://${GITHUB_TOKEN}@github.com/Kevrollin/gitpilot.io.git
   ```

### Solution 4: Verify Repository URL

Make sure the repository URL is correct:

1. Check the actual repository URL:
   ```bash
   git remote -v
   ```

2. Verify it exists:
   ```bash
   curl -I https://github.com/Kevrollin/gitpilot.io
   ```

3. If 404, check:
   - Repository name is correct
   - Username is correct
   - Repository exists
   - Repository is accessible

## Recommended Solution

**For an open-source tool like Gitpilot, make the repository public:**

1. It's easier for users to install
2. No authentication required
3. More discoverable
4. Better for open-source projects

### Steps to Make Repository Public

1. Go to repository settings
2. Scroll to "Danger Zone"
3. Click "Change repository visibility"
4. Select "Make public"
5. Type repository name to confirm
6. Done!

After making it public, users can install with:
```bash
pipx install git+https://github.com/Kevrollin/gitpilot.io.git
```

## Alternative: Install from Release

If the repository must stay private, users can download and install from releases:

1. **Download release files** from: https://github.com/Kevrollin/gitpilot.io/releases
2. **Install locally**:
   ```bash
   # Download wheel file
   wget https://github.com/Kevrollin/gitpilot.io/releases/download/v0.1.2/auto_commit_assistant-0.1.2-py3-none-any.whl
   
   # Install
   pipx install auto_commit_assistant-0.1.2-py3-none-any.whl
   ```

## Update Documentation

After fixing the repository visibility, update your documentation to reflect the correct installation method.

