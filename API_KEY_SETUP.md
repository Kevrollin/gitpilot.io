# API Key Setup Guide

## 🔐 Adding Your Gemini API Key

To include your API key so users don't need to set it themselves:

### Step 1: Get Your API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

### Step 2: Set the Key (Choose One Method)

#### Method A: Environment Variable During Build (Recommended)

```bash
# Set the key as environment variable
export DEV_MK_GEMINI_API_KEY="your-actual-api-key-here"

# Build the package (key will be embedded)
python3 -m pip install --upgrade build
python3 -m build

# The key is now in the built package
```

#### Method B: Direct Code Update (For Testing)

**⚠️ WARNING: Only do this if the repository is private or you're okay with the key being public!**

1. Edit `auto_commit/ai.py`
2. Find the line: `DEFAULT_API_KEY = os.getenv("DEV_MK_GEMINI_API_KEY", "")`
3. Replace with: `DEFAULT_API_KEY = "your-actual-api-key-here"`
4. Build and release

#### Method C: Use the Setup Script

```bash
./scripts/set_api_key.sh your-api-key-here
```

This will:
- Update the code with your key
- Prepare for building
- You can then build and release

### Step 3: Build and Release

```bash
# Build the package
python3 -m build

# Create release
./scripts/release.sh
# Enter new version
# Create release manually if needed
```

### Step 4: Test Installation

```bash
# Install the new release
pipx install git+https://github.com/Kevrollin/gitpilot.io.git@v0.1.3

# Test it works without setting API key
autocommit --version
```

## 🔒 Security Considerations

### If Repository is Public:

**DO NOT** hardcode the API key in the source code! Instead:

1. **Use GitHub Secrets** (for GitHub Actions):
   - Add `DEV_MK_GEMINI_API_KEY` as repository secret
   - Use it in workflow during build
   - Key is never in source code

2. **Use Environment Variable During Build**:
   - Set key as environment variable
   - Build locally with key
   - Key is in built package but not in source
   - Don't commit the key

3. **Create a Separate Config Package**:
   - Key in separate private package
   - Main package depends on it
   - More complex but more secure

### If Repository is Private:

You can safely include the key in the code, but still consider:
- Rate limits on shared keys
- Usage monitoring
- Key rotation
- User override option (current implementation)

## 📝 Current Implementation

The code supports:
- ✅ Default shared key (via `DEV_MK_GEMINI_API_KEY`)
- ✅ User override (via `GEMINI_API_KEY`)
- ✅ Clear warnings when using default key
- ✅ Fallback to user's key if default fails

## 🎯 Recommended Approach

1. **For Public Repos**: Use environment variable during build
2. **For Private Repos**: Can include in code with warnings
3. **Best Practice**: Always allow users to override with their own key

## ✅ After Setting Key

1. Test the installation
2. Verify it works without user setting key
3. Create release
4. Update documentation
5. Monitor usage and rate limits

---

**Remember**: Always allow users to use their own key for unlimited usage!

