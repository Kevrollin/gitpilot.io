# Fixing Invalid API Key Issue

## Problem

The API key in the code is invalid or expired. Users get this error:
```
API key not valid. Please pass a valid API key.
```

## Solutions

### Option 1: Update with Valid API Key (Recommended)

**Step 1: Get a valid API key**

1. Go to: https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

**Step 2: Update the code**

Edit `auto_commit/ai.py`:
```python
DEFAULT_API_KEY = os.getenv("DEV_MK_GEMINI_API_KEY", "YOUR_VALID_API_KEY_HERE")
```

**Step 3: Test the key**

```bash
python3 -c "import google.generativeai as genai; genai.configure(api_key='YOUR_KEY'); models = genai.list_models(); print('Valid!' if list(models) else 'Invalid')"
```

**Step 4: Build and release**

```bash
# Update version
# Edit auto_commit/__init__.py to 0.1.4

# Build
source venv/bin/activate
python -m build

# Commit and push
git add .
git commit -m "fix: Update API key"
git tag -a v0.1.4 -m "Release v0.1.4 - Fix API key"
git push origin master
git push origin v0.1.4

# Create release on GitHub
```

### Option 2: Remove Default Key, Require User Key

**Better approach for public repos:**

1. Remove the hardcoded key
2. Make it clear users need to set their own key
3. Provide clear setup instructions

**Update `auto_commit/ai.py`:**
```python
# Remove default key - users must set their own
DEFAULT_API_KEY = os.getenv("DEV_MK_GEMINI_API_KEY", "")
```

### Option 3: Use Environment Variable Only

**Most secure approach:**

1. Don't hardcode any key
2. Users must set `GEMINI_API_KEY` environment variable
3. Provide clear error messages and setup instructions

## Quick Fix for Users

**Tell users to set their own API key:**

```bash
# Users can set their own key
export GEMINI_API_KEY='their-valid-api-key'

# Or in .env file
echo 'GEMINI_API_KEY=their-valid-api-key' > .env
```

## Testing API Key

**Test if a key is valid:**

```bash
python3 << EOF
import google.generativeai as genai
api_key = "YOUR_API_KEY_HERE"
try:
    genai.configure(api_key=api_key)
    models = list(genai.list_models())
    print(f"✅ Key is valid! Found {len(models)} models")
except Exception as e:
    print(f"❌ Key is invalid: {e}")
EOF
```

## Recommended Solution

**For a public repository, the best approach is:**

1. **Remove the hardcoded key** (security risk)
2. **Make it optional** - tool works if user sets key
3. **Provide clear instructions** on how to get and set a key
4. **Or create a service/proxy** that manages keys securely

## Next Steps

1. **Test your API key** to verify it works
2. **Update the code** with a valid key (or remove it)
3. **Build new version** (0.1.4)
4. **Create new release**
5. **Update documentation** with API key setup instructions

## For Users (Temporary Fix)

**Until a new release is available, users can:**

```bash
# Set their own API key
export GEMINI_API_KEY='their-api-key-here'

# Or create .env file in project directory
echo 'GEMINI_API_KEY=their-api-key-here' > .env

# Then run autocommit
autocommit
```

---

**The API key in v0.1.3 is invalid. Update it and create v0.1.4!**

