# LinkedIn Summary (Copy/Paste)

## Project
ChronoPlan AN - Planning Analytics Platform

## One-liner
Built a full Streamlit product for project controls teams: secure login, project workspaces, Excel-to-WBS ingestion, KPI/S-curve dashboards, and subscription-ready billing flows.

## What I implemented
- Multi-project workspace management with persistent file/mapping state
- Excel ingestion pipeline for WBS and schedule-driven analytics
- Dashboard views for planned vs actual, delay, SPI/SV, and weekly momentum
- S-curve visualization with forecast logic and activity filtering
- Google OAuth authentication and session lifecycle
- Billing and access-control flows (trial/subscription) with webhook synchronization
- Admin tooling for account/plan operations

## Stack
Python, Streamlit, Pandas, Plotly, OpenPyXL, Authlib, SQLite, Paddle Webhooks

## Impact
- Reduced friction for non-technical users by turning raw planning workbooks into immediately usable analytics
- Created a production-style app architecture (auth, billing, data services, UI modules) suitable for real deployment
