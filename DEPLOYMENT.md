# Deployment Guide

## Option 1: Streamlit Cloud (Recommended)

### Prerequisites
- GitHub repository with your code
- Anthropic API key

### Steps
1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Add Streamlit web interface"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file: `streamlit_app.py`
   - Add secrets:
     ```
     ANTHROPIC_API_KEY=your_key_here
     MODEL=claude-3-5-sonnet-20240620
     ```
   - Click "Deploy"

3. **Access your app**:
   - Get URL like: `https://your-app-name.streamlit.app`
   - Automatic updates on GitHub pushes

## Option 2: GitHub Codespaces

### Steps
1. **Enable Codespaces**:
   - Go to your GitHub repo
   - Click "Code" → "Codespaces"
   - Click "Create codespace"

2. **Run in Codespace**:
   ```bash
   uv sync
   streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
   ```

3. **Access via Port Forwarding**:
   - Codespaces automatically forwards port 8501
   - Get public URL in "Ports" tab
   - Share with anyone

## Option 3: Railway (More Control)

### Steps
1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Deploy**:
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Set Environment Variables**:
   - Go to Railway dashboard
   - Add: `ANTHROPIC_API_KEY` and `MODEL`

## Local Testing

Before deploying, test locally:

```bash
# Install dependencies
uv sync

# Run Streamlit app
streamlit run streamlit_app.py
```

Visit `http://localhost:8501` to test.
