# Branding and API Key Setup

## ⚠️ Important Security Warning

**DO NOT hardcode your API key directly in the source code if the repository is public!**

If you hardcode an API key in public code:
- Anyone can see and use your key
- You'll be charged for all usage
- Your key could be rate-limited or banned
- Security risk

## ✅ Recommended Approach

### Option 1: Use Environment Variable During Build (Safest)

Set the API key as an environment variable during the release process, not in the code:

1. **Create a secure config file** (not in git):
   ```bash
   # .env.release (not committed to git)
   DEV_MK_GEMINI_API_KEY=your-actual-key-here
   ```

2. **Set it as build-time environment variable**:
   ```bash
   export DEV_MK_GEMINI_API_KEY=your-key
   python3 -m build
   ```

3. **Or use GitHub Secrets** (for GitHub Actions):
   - Add `DEV_MK_GEMINI_API_KEY` as a repository secret
   - Use it in the workflow during build

### Option 2: Default Key with Clear Warnings (Current Implementation)

The code now supports:
- Default shared key via `DEV_MK_GEMINI_API_KEY` environment variable
- Users can override with their own `GEMINI_API_KEY`
- Clear warnings when using default key
- Rate limiting and usage monitoring

### Option 3: Create a Service/Proxy

For better security:
- Create an API proxy service
- Users authenticate with your service
- Your service manages API keys
- More complex but more secure

## 🔐 How to Add Your API Key Safely

### For Local Testing:
```bash
# Set as environment variable (not in code)
export DEV_MK_GEMINI_API_KEY=your-key-here
```

### For Releases:
1. **Use GitHub Secrets** (recommended):
   - Go to repository settings → Secrets
   - Add `DEV_MK_GEMINI_API_KEY`
   - Update GitHub Actions workflow to use it

2. **Or set during build**:
   ```bash
   DEV_MK_GEMINI_API_KEY=your-key python3 -m build
   ```

3. **Or inject during installation**:
   - Create a separate config package
   - Users install with key provided separately

## 📝 Next Steps

1. **Set your API key as environment variable**:
   ```bash
   export DEV_MK_GEMINI_API_KEY=your-actual-gemini-api-key
   ```

2. **Update branding** (see branding changes below)

3. **Test the installation**:
   ```bash
   pipx install git+https://github.com/Kevrollin/gitpilot.io.git
   ```

4. **Verify it works without requiring user's key**

## 🎨 Branding Updates Needed

Update these files with "dev.mk" and "Kelvin Mukaria":
- `setup.py` - Author and package info
- `README.md` - Title and author
- `cli.py` - Description
- `ui.py` - Banner
- `LICENSE` - Copyright
- All documentation files

