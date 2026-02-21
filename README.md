# Chronoplan

Chronoplan is a Streamlit application for planning and project control workflows.  
It combines portfolio views, WBS exploration, schedule/progress tracking, and subscription-aware access control in one product.

## What this repository contains
- Main app with routed pages for Home, Projects, Dashboard, WBS, S-curve, Billing, Checkout, and Admin tools.
- Excel-driven project ingestion and KPI visualization.
- Authentication flow (OIDC) with protected pages.
- Billing lifecycle integration (Paddle checkout + webhook sync).
- Optional Cloudflare R2 backups for operational artifacts.

## Tech stack
- Python 3.12
- Streamlit
- Pandas + OpenPyXL/Calamine
- Plotly
- SQLite
- Optional Cloudflare Worker for webhook handling

## Local setup
1. Create and activate a virtual environment.
2. Install dependencies.
3. Start the app.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Optional utilities:
- WBS utility app: `streamlit run wbs_app/wbs_app.py`
- Lightweight local webhook receiver: `python scripts/paddle_webhook_server.py`

## Configuration

### Authentication (OIDC)
Set Streamlit secrets:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "set-a-long-random-string"
client_id = "..."
client_secret = "..."
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

### Billing/runtime keys
Set as environment variables or Streamlit secrets:
- `BILLING_API_URL`
- `BILLING_API_TOKEN`
- `APP_URL`

If checkout is enabled in production:
- `PADDLE_ENV=production`
- `PADDLE_WEBHOOK_SECRET`
- `PADDLE_CLIENT_TOKEN`

### Backups (optional)
To enable Cloudflare R2 backups:
- `ENABLE_R2_BACKUPS=1`
- `R2_ACCOUNT_ID`
- `R2_ACCESS_KEY_ID`
- `R2_SECRET_ACCESS_KEY`
- `R2_BUCKET`
- Optional: `R2_ENDPOINT`, `R2_BACKUP_KEEP`

## Project layout
- `main.py`: app entrypoint (routes to `pages/0_Router.py`)
- `pages/`: Streamlit pages (projects, dashboard, WBS, S-curve, billing, checkout, legal)
- `projects_page/`: UI components/styles/helpers for project views
- `scripts/`: local operational scripts (including Paddle webhook server)
- `workers/`: Cloudflare Worker webhook implementation
- `artifacts/`: generated operational data and templates

## Deployment notes
- Works locally and on Streamlit Cloud.
- Use HTTPS `APP_URL` in production.
- Keep secrets out of git (`.streamlit/*` is ignored except page config).
