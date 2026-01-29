from __future__ import annotations

from datetime import date
from pathlib import Path

import streamlit as st

from projects_page.styles import inject_base_css

_icon_path = Path(__file__).resolve().parents[1] / "Chronoplan_ico.png"
st.set_page_config(
    page_title="ChronoPlan Privacy",
    page_icon=str(_icon_path) if _icon_path.exists() else "CP",
    layout="wide",
)
inject_base_css()

EFFECTIVE_DATE = date(2026, 1, 29)
SUPPORT_EMAIL = "chronoplan.app@gmail.com"
OPERATOR_NAME = "Ali EL Bied"
OPERATOR_LOCATION = "Brussels, Belgium"

st.markdown(
    f"""
# Privacy Policy

**Effective date:** {EFFECTIVE_DATE.isoformat()}

This Privacy Policy explains how ChronoPlan (the “Service”) collects, uses, and shares information.

## 1) Who we are

ChronoPlan is operated by **{OPERATOR_NAME}**, **{OPERATOR_LOCATION}**.

Contact: **{SUPPORT_EMAIL}**

## 2) Data we collect

Depending on how you use the Service, we may collect:

- **Account data**: your name, email address, and profile picture (via Google sign-in).
- **Uploaded content**: files you upload (e.g., Excel files) and the derived project data needed to generate dashboards.
- **Usage/technical data**: basic logs needed for security and debugging (for example, error logs).
- **Billing identifiers**: subscription/customer identifiers received from Paddle webhooks and billing sync (where configured).

## 3) How we use data

We use your data to:
- authenticate you and maintain your session,
- provide dashboards and project features,
- provide billing/subscription access control,
- prevent abuse and improve reliability,
- respond to support requests.

## 4) Where data is stored (high level)

The Service stores project and billing state on the server running the app (for example under an `artifacts/` directory, including a local SQLite database).
If enabled by the operator, backups may be stored with **Cloudflare R2**.
If configured, billing status may be stored in **Cloudflare Workers KV** via a billing webhook worker.

## 5) Payments and Paddle

Payments are handled by **Paddle.com**. Paddle may act as the **Merchant of Record** and will process your payment information.
We do not store full card details on our servers.

## 6) Sharing and subprocessors

We may share data with service providers strictly to operate the Service, such as:
- **Google** (authentication),
- **Streamlit hosting** (app hosting),
- **Paddle.com** (payment processing / merchant of record),
- **Cloudflare** (Workers/KV and/or R2 if enabled).

## 7) Retention

We keep data as long as needed to provide the Service, comply with legal obligations, resolve disputes, and enforce agreements.
You can request deletion (see below). Some records may be retained where required for legal, security, or accounting reasons.

## 8) Your rights

You may request access, correction, or deletion of your personal data by contacting us at **{SUPPORT_EMAIL}**.
If you are in the EEA/UK, you may have additional rights under GDPR (for example: objection, restriction, portability).

## 9) Security

We take reasonable measures to protect data, but no system is 100% secure.

## 10) International users

Your data may be processed in countries where our providers operate their infrastructure.

## 11) Changes

We may update this policy from time to time. We will update the effective date above when we do.

## 12) Contact

Privacy questions: **{SUPPORT_EMAIL}**
""".strip(),
    unsafe_allow_html=False,
)

st.divider()
col_left, col_right = st.columns(2)
with col_left:
    st.page_link("pages/90_Terms.py", label="Terms of Service")
with col_right:
    st.page_link("pages/92_Refunds.py", label="Refund & Cancellation Policy")
