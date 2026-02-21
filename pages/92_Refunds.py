from __future__ import annotations

from datetime import date
from pathlib import Path

import streamlit as st

from projects_page.styles import inject_base_css, inject_legal_css

_icon_path = Path(__file__).resolve().parents[1] / "Chronoplan_ico.png"
st.set_page_config(
    page_title="ChronoPlan Refunds",
    page_icon=str(_icon_path) if _icon_path.exists() else "CP",
    layout="wide",
)
inject_base_css()
inject_legal_css()

EFFECTIVE_DATE = date(2026, 1, 29)
SUPPORT_EMAIL = "chronoplan.app@gmail.com"
OPERATOR_NAME = "Ali EL Bied"

legal = st.container(key="legal_page")
with legal.container(key="legal_back_btn"):
    st.page_link("pages/4_Billing.py", label="Back to billing")

legal.markdown(
    f"""
# Refund & Cancellation Policy

**Effective date:** {EFFECTIVE_DATE.isoformat()}

This policy explains how cancellations and refunds work for ChronoPlan.

## 1) Cancellation

- You can cancel at any time to stop **future renewals**.
- After cancellation, access typically remains available until the end of the current paid billing period.
- We do **not** offer prorated refunds for partial periods (unless required by law).

## 2) 14‑day first‑payment refund (goodwill)

If this is your **first paid subscription payment**, you can request a refund within **14 days** of the charge date if you have not “meaningfully used” the Service.

For this policy, “meaningful usage” generally means any of the following:
- more than 1 project created, or
- more than 1 file uploaded, or
- repeated/ongoing use of premium features.

If you are unsure, contact us and we’ll review fairly.

## 3) How to request a refund

Email **{SUPPORT_EMAIL}** with:
- the email used for your ChronoPlan account, and
- your Paddle receipt or transaction details (if available), and
- a short reason for the request.

## 4) Payments via Paddle (Merchant of Record)

Payments are processed by **Paddle.com** and Paddle may be the **Merchant of Record**. In some cases, refunds may be issued through Paddle’s systems and timelines.

## 5) Legal rights

This policy does not limit rights you may have under mandatory consumer protection laws in your country (including the EU/EEA/UK where applicable).

## 6) Abuse

We may deny refund requests that we reasonably believe involve fraud, abuse, or policy manipulation.

## 7) Contact

Refund/cancellation questions: **{SUPPORT_EMAIL}** (Operator: {OPERATOR_NAME})
""".strip(),
    unsafe_allow_html=False,
)

footer = legal.container(key="legal_footer")
footer.divider()
col_left, col_right = footer.columns(2)
with col_left:
    st.page_link("pages/90_Terms.py", label="Terms of Service")
with col_right:
    st.page_link("pages/91_Privacy.py", label="Privacy Policy")
