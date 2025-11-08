# Website Deployment Guide for dev.mk

This guide explains how to deploy a website for hosting dev.mk downloads.

## Quick Start

### 1. Build and Deploy Locally

```bash
# Build the package
./scripts/build_package.sh

# Deploy website (copies files and updates HTML)
./scripts/deploy_website.sh
```

### 2. Choose Hosting Option

## Hosting Options

### Option 1: GitHub Pages (Recommended - Free & Easy)

**Pros:**
- Free
- Automatic HTTPS
- Custom domain support
- Integrated with GitHub
- Automatic deployment via GitHub Actions

**Setup:**

1. **Enable GitHub Pages:**
   ```bash
   # Create gh-pages branch
   git checkout -b gh-pages
   git add website/
   git commit -m "Add website"
   git push origin gh-pages
   ```

2. **Configure in GitHub:**
   - Go to repository → Settings → Pages
   - Select `gh-pages` branch
   - Select `/website` as root directory
   - Save

3. **Your site will be live at:**
   - `https://yourusername.github.io/gitpilot.io`
   - Or custom domain if configured

4. **Automatic Deployment:**
   - The GitHub Actions workflow will automatically deploy on pushes
   - Just push to `master` branch and website updates

### Option 2: Netlify (Free & Easy)

**Pros:**
- Free tier available
- Automatic HTTPS
- Custom domain support
- Easy deployment
- Preview deployments

**Setup:**

1. **Install Netlify CLI:**
   ```bash
   npm install -g netlify-cli
   ```

2. **Deploy:**
   ```bash
   cd website
   netlify deploy --prod
   ```

3. **Or connect via GitHub:**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub repository
   - Set build directory to `website`
   - Deploy

4. **Your site will be at:**
   - `https://your-site-name.netlify.app`
   - Or custom domain

### Option 3: Vercel (Free & Easy)

**Pros:**
- Free tier available
- Automatic HTTPS
- Custom domain support
- Fast CDN
- Easy deployment

**Setup:**

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd website
   vercel --prod
   ```

3. **Or connect via GitHub:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Connect your GitHub repository
   - Set root directory to `website`
   - Deploy

### Option 4: Cloudflare Pages (Free)

**Pros:**
- Free
- Fast CDN
- Automatic HTTPS
- Custom domain support

**Setup:**

1. Go to [Cloudflare Pages](https://pages.cloudflare.com)
2. Connect your GitHub repository
3. Set build directory to `website`
4. Deploy

### Option 5: Simple HTTP Server

**For local testing or small deployments:**

```bash
cd website
python3 -m http.server 8000
# Visit http://localhost:8000
```

**For production:**
- Use Nginx, Apache, or any static file server
- Upload `website/` directory to your server
- Configure web server to serve files

## Automated Deployment

### GitHub Actions (Already Configured)

The repository includes `.github/workflows/deploy-website.yml` that:
- Builds the package automatically
- Copies files to website directory
- Updates version in HTML
- Deploys to GitHub Pages

**To use:**
1. Enable GitHub Pages in repository settings
2. Push changes to `master` branch
3. Website updates automatically

### Manual Deployment Workflow

1. **Build package:**
   ```bash
   ./scripts/build_package.sh
   ```

2. **Deploy website:**
   ```bash
   ./scripts/deploy_website.sh
   ```

3. **Push to hosting platform:**
   - GitHub Pages: Push to `gh-pages` branch
   - Netlify/Vercel: Push to `master` (auto-deploy)
   - Or upload manually

## Custom Domain Setup

### For GitHub Pages:

1. **Add CNAME file:**
   ```bash
   echo "dev.mk" > website/CNAME
   git add website/CNAME
   git commit -m "Add custom domain"
   git push
   ```

2. **Configure DNS:**
   - Add CNAME record: `dev.mk` → `yourusername.github.io`
   - Or A records: `dev.mk` → GitHub Pages IPs

3. **Enable in GitHub:**
   - Repository → Settings → Pages
   - Add custom domain: `dev.mk`
   - Enable "Enforce HTTPS"

### For Netlify:

1. **Add domain in Netlify dashboard:**
   - Site settings → Domain management
   - Add custom domain
   - Follow DNS setup instructions

### For Vercel:

1. **Add domain in Vercel dashboard:**
   - Project settings → Domains
   - Add custom domain
   - Follow DNS setup instructions

## Updating Downloads

### When releasing a new version:

1. **Update version in code:**
   ```bash
   # Edit auto_commit/__init__.py
   __version__ = "1.1.2"
   ```

2. **Build and deploy:**
   ```bash
   ./scripts/deploy_website.sh
   ```

3. **Or let GitHub Actions handle it:**
   - Just push to master
   - GitHub Actions builds and deploys automatically

### Manual update:

1. **Build package:**
   ```bash
   ./scripts/build_package.sh
   ```

2. **Copy to website:**
   ```bash
   cp dist/* website/dist/
   ```

3. **Update HTML:**
   - Edit `website/index.html`
   - Update version numbers
   - Update download links

4. **Deploy:**
   - Push to GitHub (for GitHub Pages)
   - Or deploy via Netlify/Vercel CLI

## File Structure

```
website/
├── index.html          # Main download page
├── dist/              # Package files (wheel, tar.gz)
│   ├── *.whl
│   └── *.tar.gz
├── CNAME              # Custom domain (optional)
└── README.md          # Website documentation
```

## Testing

### Test locally:

```bash
cd website
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Test downloads:

1. Click download links
2. Verify files download correctly
3. Test installation:
   ```bash
   pip install downloaded-file.whl
   ```

## Troubleshooting

### Files not updating:

- Clear browser cache
- Check file paths in HTML
- Verify files are in `website/dist/`

### GitHub Pages not updating:

- Check GitHub Actions workflow status
- Verify `gh-pages` branch exists
- Check repository settings → Pages

### Download links not working:

- Verify file names match HTML links
- Check file paths are correct
- Ensure files are in `website/dist/`

## Best Practices

1. **Version control:**
   - Keep website files in git
   - Tag releases
   - Document changes

2. **Automation:**
   - Use GitHub Actions for automatic deployment
   - Automate version updates
   - Test before deploying

3. **Monitoring:**
   - Check download analytics
   - Monitor website uptime
   - Track errors

4. **Security:**
   - Use HTTPS
   - Keep dependencies updated
   - Scan for vulnerabilities

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Netlify Documentation](https://docs.netlify.com)
- [Vercel Documentation](https://vercel.com/docs)
- [Cloudflare Pages Documentation](https://developers.cloudflare.com/pages)

---

**Ready to deploy! 🚀**

For questions or issues, open an issue on GitHub.

