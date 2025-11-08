# Website Quick Start Guide

## 🚀 Get Your Download Site Live in 5 Minutes

### Step 1: Build the Package

```bash
./scripts/build_package.sh
```

This creates the `.whl` and `.tar.gz` files in the `dist/` directory.

### Step 2: Deploy Website

**Option A: GitHub Pages (Recommended)**

1. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Settings → Pages
   - Source: `Deploy from a branch`
   - Branch: `gh-pages` (create it if needed)
   - Folder: `/website`
   - Save

2. **Deploy:**
   ```bash
   ./scripts/deploy_website.sh
   git checkout -b gh-pages
   git add website/
   git commit -m "Deploy website"
   git push origin gh-pages
   ```

3. **Your site is live at:**
   - `https://yourusername.github.io/gitpilot.io`
   - Or your custom domain

**Option B: Netlify (Easiest)**

1. **Go to [netlify.com](https://netlify.com)**
2. **Click "New site from Git"**
3. **Connect GitHub repository**
4. **Settings:**
   - Build command: `./scripts/build_package.sh && cp dist/* website/dist/`
   - Publish directory: `website`
5. **Deploy!**

**Option C: Vercel**

1. **Go to [vercel.com](https://vercel.com)**
2. **Click "Import Project"**
3. **Connect GitHub repository**
4. **Settings:**
   - Root directory: `website`
5. **Deploy!**

## 📝 What You Get

- ✅ Beautiful download page
- ✅ Direct download links for `.whl` and `.tar.gz`
- ✅ Installation instructions
- ✅ Automatic version updates (with GitHub Actions)
- ✅ Mobile-responsive design

## 🔄 Updating

When you release a new version:

1. **Update version in code:**
   ```bash
   # Edit auto_commit/__init__.py
   __version__ = "1.1.2"
   ```

2. **Build and deploy:**
   ```bash
   ./scripts/deploy_website.sh
   # Then push to your hosting platform
   ```

Or let GitHub Actions handle it automatically!

## 🎨 Customization

Edit `website/index.html` to:
- Change colors
- Add your logo
- Update branding
- Add features
- Change layout

## 📦 File Structure

```
website/
├── index.html      # Main page
├── dist/          # Package files (auto-generated)
└── README.md      # Documentation
```

## ✅ Done!

Your download site is now live! Share the URL with users.

---

**Need help?** See `WEBSITE_DEPLOYMENT.md` for detailed instructions.

