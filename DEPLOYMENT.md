# Deployment Guide

This guide shows 3 ways to deploy your heart disease prediction dashboard.

## Quick Comparison

| Method | Cost | Setup Time | Ease | Auto-Deploy | Best For |
|--------|------|------------|------|-------------|----------|
| **Netlify** ⭐ | Free | 5 min | Easy | Yes | Quick portfolio showcase |
| **GitHub Pages** | Free | 2 min | Very Easy | Yes | Minimal setup |
| **Azure ACI** | $1.87/day | 15 min | Moderate | Manual | Full pipeline reproduction |

---

## Option 1: Netlify (Recommended) ⭐⭐⭐⭐⭐

### Step 1: Create GitHub Repository
1. Go to **github.com/new**
2. Create repo `ds710-heart-disease`
3. Push your files:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/ds710-heart-disease.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Netlify
1. Go to **netlify.com**
2. Click **"Sign up"** → Connect GitHub account
3. Click **"New site from Git"**
4. Select **`ds710-heart-disease`** repository
5. **Build settings**:
   - Build command: (leave blank)
   - Publish directory: `.` (current directory)
6. Click **"Deploy site"**
7. Wait 30 seconds → Your site is live!

### Step 3: Custom Domain (Optional)
1. In Netlify dashboard, go to **Site settings**
2. Under **Domain management**, add custom domain
3. Points to `[random].netlify.app` by default
4. Can add custom domain (requires DNS change)

### Auto-Deploy on Future Updates
Every time you `git push`, Netlify automatically rebuilds and deploys! ✅

**Estimated time**: 5 minutes
**Cost**: Free (generous free tier)

---

## Option 2: GitHub Pages

### Step 1: Prepare Files
Make sure you have:
- `dashboard.html` (main file)
- `README.md`
- `LICENSE`
- `.gitignore`

### Step 2: Enable GitHub Pages
1. Go to your repo on **github.com**
2. Click **Settings** → **Pages**
3. Under "Source", select **main** branch
4. Save
5. Wait 1 minute → Site is live!

**URL format**: `https://USERNAME.github.io/ds710-heart-disease/`

**Estimated time**: 2 minutes
**Cost**: Free

---

## Option 3: Azure Container Instances (Current Setup)

### Prerequisites
- Azure account (free tier available)
- Azure CLI installed
- Docker images pushed to Docker Hub

### Step 1: Create Resource Group
```bash
az group create --name ETL_DS710_RG --location eastus2
```

### Step 2: Create Storage Account
```bash
az storage account create \
  --name ds710storage11154 \
  --resource-group ETL_DS710_RG \
  --location eastus2 \
  --sku Standard_LRS \
  --kind StorageV2
```

### Step 3: Create File Share
```bash
az storage share create \
  --account-name ds710storage11154 \
  --name ds710share \
  --quota 100
```

### Step 4: Deploy Dashboard Container
```bash
az container create \
  --resource-group ETL_DS710_RG \
  --name ds710-dashboard \
  --image mbubulka/ds710-dashboard:latest \
  --cpu 1 \
  --memory 1.5 \
  --ports 8501 \
  --protocol TCP \
  --azure-file-volume-account-name ds710storage11154 \
  --azure-file-volume-account-key $(az storage account keys list \
    --resource-group ETL_DS710_RG \
    --account-name ds710storage11154 \
    --query [0].value -o tsv) \
  --azure-file-volume-share-name ds710share \
  --azure-file-volume-mount-path /data
```

### Step 5: Get Public IP
```bash
az container show \
  --resource-group ETL_DS710_RG \
  --name ds710-dashboard \
  --query ipAddress.ip -o tsv
```

**Access at**: `http://[IP_ADDRESS]:8501/dashboard.html`

**Estimated time**: 15 minutes
**Cost**: ~$1.87/day (all containers), $0.31/day (dashboard only)

---

## Local Development

### Option A: Just View Dashboard
1. Download `dashboard.html`
2. Double-click to open in browser
3. No installation needed!

### Option B: Reproduce Full Pipeline
1. **Install Docker**:
   ```bash
   # Windows/Mac: Download from https://www.docker.com/products/docker-desktop
   # Linux:
   sudo apt-get install docker.io docker-compose
   ```

2. **Create docker-compose.yml**:
   ```yaml
   version: '3.8'
   services:
     etl:
       image: mbubulka/ds710-etl:latest
       volumes:
         - ./data:/data
     eda:
       image: mbubulka/ds710-eda:latest
       depends_on:
         - etl
       volumes:
         - ./data:/data
     model:
       image: mbubulka/ds710-model:latest
       depends_on:
         - eda
       volumes:
         - ./data:/data
     fairness:
       image: mbubulka/ds710-fairness:latest
       depends_on:
         - model
       volumes:
         - ./data:/data
     dashboard:
       image: mbubulka/ds710-dashboard:latest
       depends_on:
         - fairness
       volumes:
         - ./data:/data
       ports:
         - "8501:8501"
   ```

3. **Run**:
   ```bash
   mkdir data
   docker-compose up
   ```

4. **Access**:
   ```
   http://localhost:8501/dashboard.html
   ```

---

## Troubleshooting

### Netlify Deploy Failed
- Check that you pushed to GitHub (`git push`)
- Verify `dashboard.html` exists in repo root
- Check Netlify deploy logs (Deploys tab)

### GitHub Pages Not Showing
- Wait 1 minute after enabling
- Check URL format: `username.github.io/repo-name`
- Ensure `.nojekyll` file exists (Netlify adds automatically)

### Azure Container Won't Start
- Check Azure CLI is authenticated: `az account show`
- Verify Docker image exists: `docker pull mbubulka/ds710-dashboard:latest`
- Check storage account keys: `az storage account keys list`

### Dashboard Shows Blank
- Open browser DevTools (F12)
- Check Console for JavaScript errors
- Verify all files (HTML, CSS, JS) are in same directory

---

## Cost Analysis

### Netlify Free Tier
- **Storage**: Up to 100 GB
- **Bandwidth**: 100 GB/month
- **Build minutes**: 300/month
- **Cost**: **$0/month** (free)

### GitHub Pages
- **Storage**: Unlimited (reasonable limits)
- **Bandwidth**: Unlimited
- **Cost**: **$0/month** (free)

### Azure ACI (Current)
- **Dashboard only**: $0.31/day = **$9.30/month**
- **Full pipeline (5 containers)**: $1.87/day = **$56/month**
- **Storage (Azure Files)**: $0.06/month
- **Total**: $9.36-56/month depending on containers

---

## Recommendation

🎯 **Use Netlify** because:
1. **Simplest setup** (5 minutes)
2. **Zero cost** (free tier)
3. **Auto-deploy** on git push
4. **Professional appearance** (custom domain available)
5. **No maintenance** needed

---

## Next Steps

1. Create GitHub repo: `github.com/USERNAME/ds710-heart-disease`
2. Push files to GitHub
3. Deploy to Netlify (5 minutes)
4. Share link on portfolio/LinkedIn

**That's it!** Your dashboard is now live on the internet. 🚀
