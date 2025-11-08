# Website for dev.mk Downloads

This directory contains a simple static website for hosting dev.mk downloads.

## Setup

1. **Build the package:**
   ```bash
   ./scripts/build_package.sh
   ```

2. **Copy built files to website directory:**
   ```bash
   cp dist/* website/dist/
   ```

3. **Update version in index.html:**
   - Update the version number in the HTML file
   - Update download links to match the new version

## Hosting Options

### Option 1: GitHub Pages (Free, Easy)

1. **Create a `gh-pages` branch:**
   ```bash
   git checkout -b gh-pages
   git add website/
   git commit -m "Add website"
   git push origin gh-pages
   ```

2. **Enable GitHub Pages:**
   - Go to repository settings → Pages
   - Select `gh-pages` branch
   - Select `/website` as root directory
   - Your site will be at: `https://yourusername.github.io/gitpilot.io`

3. **Update package files:**
   - After each build, copy files to `website/dist/`
   - Commit and push to `gh-pages` branch

### Option 2: Netlify (Free, Easy)

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
   - Go to netlify.com
   - Connect your GitHub repository
   - Set build directory to `website`
   - Deploy

### Option 3: Vercel (Free, Easy)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd website
   vercel --prod
   ```

### Option 4: Simple HTTP Server

1. **Serve locally:**
   ```bash
   cd website
   python3 -m http.server 8000
   ```

2. **For production, use:**
   - Nginx
   - Apache
   - Any static file server

### Option 5: Cloud Storage (S3, etc.)

1. **Upload to S3:**
   ```bash
   aws s3 sync website/ s3://your-bucket-name/
   ```

2. **Enable static website hosting:**
   - Configure S3 bucket for static website hosting
   - Set index.html as index document

## Automated Deployment

### GitHub Actions (Recommended)

Create `.github/workflows/deploy-website.yml`:

```yaml
name: Deploy Website

on:
  push:
    branches: [ master ]
    paths:
      - 'website/**'
      - 'auto_commit/**'
      - 'setup.py'
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build wheel
      
      - name: Build package
        run: |
          python -m build
          mkdir -p website/dist
          cp dist/* website/dist/
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./website
```

## Custom Domain

1. **Get a domain** (e.g., from Namecheap, GoDaddy)
2. **Configure DNS:**
   - For GitHub Pages: Add CNAME record pointing to `yourusername.github.io`
   - For Netlify/Vercel: Follow their domain setup instructions
3. **Update website:**
   - Add CNAME file in website directory (for GitHub Pages)
   - Configure custom domain in hosting platform

## Updating Downloads

1. **Build new version:**
   ```bash
   ./scripts/build_package.sh
   ```

2. **Copy to website:**
   ```bash
   cp dist/* website/dist/
   ```

3. **Update HTML:**
   - Update version number
   - Update download links

4. **Commit and deploy:**
   ```bash
   git add website/
   git commit -m "Update to v1.1.1"
   git push
   ```

## File Structure

```
website/
├── index.html          # Main download page
├── dist/              # Package files (wheel, tar.gz)
│   ├── *.whl
│   └── *.tar.gz
└── README.md          # This file
```

## Notes

- Keep package files in `website/dist/` directory
- Update version numbers in HTML when releasing new versions
- Test download links after deployment
- Consider adding analytics (Google Analytics, etc.)

