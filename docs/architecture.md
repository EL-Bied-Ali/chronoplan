# Architecture Overview

## Application model
ChronoPlan is a Streamlit multi-page app with a service-layer style Python module layout.

High-level flow:
1. User authenticates with Google OAuth.
2. User selects or creates a project workspace.
3. User uploads an Excel planning file.
4. App extracts/matches required columns and stores project mapping.
5. Dashboard, S-curve, and WBS views render from cached parsed data.
6. Billing state gates access to upload/analytics capabilities.

## Key modules
- `auth_google.py`
  - Google OAuth, session cookie handling, login/logout helpers.
- `projects.py`
  - Project CRUD, owner scoping, file persistence, and mapping association.
- `shared_excel.py`
  - Shared workbook state restore/persist across pages.
- `wbs_app/extract_wbs_json.py`
  - Workbook parsing, schedule lookup, preview rows, and mapping suggestions.
- `services_kpis.py` / `services_dates.py`
  - KPI and date math logic used by charts and cards.
- `billing_store.py`
  - Local account/billing storage and plan status access controls.

## UI pages
- `pages/0_Projects.py`: project home and management.
- `app.py`: project progress dashboard + S-curve experience.
- `pages/2_WBS.py`: WBS rendering entry.
- `pages/4_Billing.py`: billing and subscription status.
- `pages/5_Checkout.py`: checkout tooling and diagnostics.
- `pages/99_Admin.py`: admin-level controls and metrics.

## Billing integration options
- Local webhook service:
  - `scripts/paddle_webhook_server.py`
- Edge worker option:
  - `workers/paddle_webhook_worker.js`

Both paths update plan state (`trialing` / `active`) and subscription metadata used by access gates.
