# 🚀 AgriSaarthi Deployment Guide (Vercel & Render)

This guide provides step-by-step instructions for deploying the **AgriSaarthi** platform to **Vercel** and **Render**.

---

## 🏗️ Architecture Overview

The AgriSaarthi ecosystem consists of three decoupled components:
1. **Frontend**: React 19 + Vite + Tailwind CSS Single-Page Application (SPA).
2. **Backend**: ASP.NET Core 10 Web API & Razor Command Center with Entity Framework Core.
3. **AI Microservice**: Python FastAPI serving the Scikit-Learn crop recommendation model (`crop_rf_model.joblib`) and MobileNetV2 leaf disease pathology sentry.

---

## ⚡ Option 1: Deploy Frontend on Vercel (Fastest & Recommended for Web UI)

Vercel provides edge CDN hosting, automated CI/CD from GitHub, and free SSL certificates.

### Step 1: Sign in to Vercel
1. Navigate to **[vercel.com](https://vercel.com)** and sign in using your GitHub account (`Tamanpreet84`).

### Step 2: Import the GitHub Repository
1. In the Vercel Dashboard, click **"Add New..."** → **"Project"**.
2. Select your repository: **`Tamanpreet84/AgriSaarthi`**.

### Step 3: Configure Project Settings
* **Project Name**: `agrisaarthi` (or any custom name)
* **Framework Preset**: `Vite` (Vercel detects this automatically from `vercel.json`)
* **Root Directory**: `frontend` *(If prompted, select `frontend`; otherwise the root `vercel.json` will build it automatically)*
* **Build Command**: `npm run build`
* **Output Directory**: `dist`

### Step 4: (Optional) Environment Variables
Under the **Environment Variables** section, add:
* **Key**: `VITE_API_URL`
* **Value**: `https://your-backend-service.onrender.com` *(Point this to your Render backend or leave default for testing)*

### Step 5: Deploy
Click **"Deploy"**. Vercel will install dependencies and compile the production build in ~60 seconds, assigning a live URL like:
```text
https://agrisaarthi.vercel.app
```

---

## 🐳 Option 2: Full-Stack Deployment on Render (1-Click Blueprint)

Render can deploy the **entire stack** (Python FastAPI AI Microservice, ASP.NET Core 10 Backend, and Frontend) using the pre-configured `render.yaml` Blueprint.

### Step 1: Sign in to Render
1. Navigate to **[dashboard.render.com](https://dashboard.render.com)** and sign in with GitHub.

### Step 2: Deploy with Blueprint
1. Click the **"New"** button in the top-right corner.
2. Select **"Blueprint"**.
3. Choose the repository: **`Tamanpreet84/AgriSaarthi`** (branch: `main`).

### Step 3: Automatic Service Discovery
Render will parse `render.yaml` and automatically detect the 3 services:
1. **`agrisaarthi-ai-service`** (Web Service · Docker):
   * Builds using `./ai-service/Dockerfile`.
   * Serves crop recommendation and leaf pathology on port `8000`.
2. **`agrisaarthi-backend`** (Web Service · Docker):
   * Builds using `./backend/AgriSaarthi.Api/Dockerfile`.
   * Serves ASP.NET Core 10 Web API and Razor Views.
   * Automatically discovers the AI microservice URL internally.
3. **`agrisaarthi-frontend`** (Static Site):
   * Builds using `cd frontend && npm install && npm run build`.
   * Publishes `frontend/dist` with SPA route rewrites.

### Step 4: Set Database Connection String
For `agrisaarthi-backend`, Render will prompt for:
* **`ConnectionStrings__DefaultConnection`**:
  * Provide your cloud SQL Server connection string (e.g. Free Tier Azure SQL Database, AWS RDS, or Render PostgreSQL).
  * Example Azure SQL format:
    ```text
    Server=tcp:agrisaarthi-server.database.windows.net,1433;Initial Catalog=AgriSaarthiDb;Persist Security Info=False;User ID=cloudadmin;Password=YourSecurePassword123!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
    ```

### Step 5: Click "Apply"
Render will provision and launch all three services. Each service receives its own public HTTPS URL:
* Frontend: `https://agrisaarthi-frontend.onrender.com`
* Backend API: `https://agrisaarthi-backend.onrender.com`
* AI Service: `https://agrisaarthi-ai-service.onrender.com`

---

## 📋 Pre-Configured Deployment Configuration Files

All configuration files are already set up in the repository:
1. [vercel.json](file:///C:/Users/taman/OneDrive/Desktop/agrisaarthi/vercel.json) — Vercel root build & SPA rewrites.
2. [frontend/vercel.json](file:///C:/Users/taman/OneDrive/Desktop/agrisaarthi/frontend/vercel.json) — Vercel frontend-specific configuration.
3. [render.yaml](file:///C:/Users/taman/OneDrive/Desktop/agrisaarthi/render.yaml) — Render Infrastructure as Code Blueprint.
4. [backend/AgriSaarthi.Api/Dockerfile](file:///C:/Users/taman/OneDrive/Desktop/agrisaarthi/backend/AgriSaarthi.Api/Dockerfile) — Multi-stage ASP.NET Core 10 production container.
5. [ai-service/Dockerfile](file:///C:/Users/taman/OneDrive/Desktop/agrisaarthi/ai-service/Dockerfile) — FastAPI & ML model container.
