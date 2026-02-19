# ChronoPlan AN
ChronoPlan AN is a Streamlit-based project controls platform for planning and progress tracking teams.

It combines:
- project-level workspace management
- Excel-driven WBS extraction and mapping
- KPI dashboards and S-curves
- Google OAuth authentication
- billing and subscription workflows (Paddle checkout + webhook sync)

## Why this project
This project was built to make planning analytics usable by non-technical teams: upload a scheduling workbook, map fields once, then get clean progress views and portfolio-level project organization.

## Core capabilities
- Multi-project workspace with per-project file storage and mapping persistence
- Interactive KPI dashboard (planned vs actual, delay, SPI/SV, weekly momentum)
- S-curve page with planned, actual, and forecast progression
- WBS visualization and extraction pipeline from real Excel planning exports
- Google login, session handling, and protected routes
- Trial/subscription access control and billing status pages
- Admin interface for account plan operations and billing audit events

## Tech stack
- Python 3.11
- Streamlit
- Pandas + OpenPyXL
- Plotly
- Authlib / Google OAuth
- SQLite (local billing + account store)
- Paddle API / webhooks
- Optional Cloudflare Worker integration for webhook handling

## Repository structure
```text
.
|-- app.py                      # Main dashboard app entry
|-- pages/                      # Multi-page Streamlit routes
|-- wbs_app/                    # Standalone WBS extraction UI
|-- auth_google.py              # OAuth + session logic
|-- billing_store.py            # Billing/account persistence and helpers
|-- projects.py                 # Project CRUD + per-project file state
|-- scripts/
|   `-- paddle_webhook_server.py
|-- workers/                    # Optional Cloudflare worker for webhooks
|-- artifacts/                  # Local runtime files + template
`-- .streamlit/                 # Streamlit config and local secrets
```

Additional docs:
- `docs/architecture.md`
- `docs/linkedin-summary.md`

## Run locally
1. Create and activate a virtual environment.
2. Install dependencies.
3. Add required secrets.
4. Run the app.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Optional routes:
- `streamlit run pages/0_Projects.py`
- `streamlit run wbs_app/wbs_app.py`

## Required configuration
Set these via environment variables or `.streamlit/secrets.toml`.

```toml
GOOGLE_CLIENT_ID = "..."
GOOGLE_CLIENT_SECRET = "..."
AUTH_COOKIE_SECRET = "long-random-secret"
AUTH_REDIRECT_URI = "http://localhost:8501"
AUTH_COOKIE_TTL_DAYS = "7"

PADDLE_CLIENT_TOKEN = "..."
PADDLE_ENV = "sandbox" # or "production"
PADDLE_PRICE_EUR_SANDBOX = "..."
PADDLE_PRICE_EUR = "..."
PADDLE_WEBHOOK_SECRET = "..."
PADDLE_WEBHOOK_PORT = "8001"
PADDLE_WEBHOOK_PATH = "/webhook/paddle"
```

## Billing webhook sync
To keep account plans in sync after checkout:

```bash
python scripts/paddle_webhook_server.py
```

Then configure Paddle webhook URL:

```text
http://YOUR_HOST:8001/webhook/paddle
```

## Portfolio highlights (LinkedIn-friendly)
- Built an end-to-end planning analytics product, not just isolated charts
- Implemented authentication, access control, billing status, and subscription hooks
- Designed Excel ingestion and mapping flows that support imperfect real-world source files
- Structured the app as reusable service modules (`projects`, `billing`, `auth`, `wbs`)
