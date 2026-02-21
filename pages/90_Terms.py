from __future__ import annotations

from datetime import date
from pathlib import Path

import streamlit as st

from projects_page.styles import inject_base_css, inject_legal_css

_icon_path = Path(__file__).resolve().parents[1] / "Chronoplan_ico.png"
st.set_page_config(
    page_title="ChronoPlan Terms",
    page_icon=str(_icon_path) if _icon_path.exists() else "CP",
    layout="wide",
)
inject_base_css()
inject_legal_css()

EFFECTIVE_DATE = date(2026, 1, 29)
SUPPORT_EMAIL = "chronoplan.app@gmail.com"
OPERATOR_NAME = "Ali EL Bied"
OPERATOR_LOCATION = "Brussels, Belgium"

legal = st.container(key="legal_page")
with legal.container(key="legal_back_btn"):
    st.page_link("pages/4_Billing.py", label="Back to billing")

legal.markdown(
    f"""
# Terms of Service

**Effective date:** {EFFECTIVE_DATE.isoformat()}

These Terms of Service (the “Terms”) govern your use of ChronoPlan (the “Service”).
By using the Service, you agree to these Terms.

## 1) Who operates the Service

ChronoPlan is operated by **{OPERATOR_NAME}** (“we”, “us”, “our”), located in **{OPERATOR_LOCATION}**.

Contact: **{SUPPORT_EMAIL}**

## 2) Eligibility and accounts

You must provide accurate account information and keep your account secure. You are responsible for activity under your account.

## 3) Subscriptions, payments, and Merchant of Record

Paid access may be offered via subscription.

**Payments are processed by Paddle.com** (Paddle) as our payment provider. In many cases, Paddle acts as the **Merchant of Record**, meaning Paddle is the seller of record for the transaction and may handle taxes, invoicing, and payment processing.
Your payment receipt will include the merchant details.

## 4) Trials and access

We may offer trial access. Trial terms can change, and trial access may end automatically.

## 5) Cancellation and renewals

Unless stated otherwise, subscriptions renew automatically until cancelled. You can cancel to stop future renewals. Access generally remains available until the end of the current paid billing period.

## 6) Refunds

Refunds and eligibility are described in our **Refund & Cancellation Policy** (see the “Refunds” page in the app).
Mandatory consumer protection laws in your country may provide additional rights, and those rights override this section.

## 7) Acceptable use

You agree not to:
- misuse the Service (including attempts to disrupt, reverse engineer, or bypass access controls),
- upload content you do not have rights to use,
- use the Service for unlawful purposes.

We may suspend or terminate access if we believe your use is harmful, unlawful, or violates these Terms.

## 8) Your content

You retain rights to your content. You grant us permission to process your content to provide the Service (for example: storing files you upload, generating dashboards, and creating exports).

## 9) Availability and changes

The Service may change over time, and we do not guarantee uninterrupted availability. We may modify or discontinue features at any time.

## 10) Disclaimers

The Service is provided “as is” and “as available”. To the maximum extent permitted by law, we disclaim warranties of merchantability, fitness for a particular purpose, and non-infringement.

## 11) Limitation of liability

To the maximum extent permitted by law, we are not liable for indirect, incidental, special, consequential, or punitive damages, or any loss of profits, data, or goodwill.
Our total liability for any claim relating to the Service is limited to the amount you paid for the Service in the **3 months** prior to the event giving rise to the claim.

## 12) Governing law

These Terms are governed by the laws of **Belgium**, without regard to conflict-of-law principles, subject to any mandatory consumer protection laws that apply to you.

## 13) Changes to these Terms

We may update these Terms from time to time. We will update the effective date above when we do.

## 14) Contact

Questions about these Terms: **{SUPPORT_EMAIL}**
""".strip(),
    unsafe_allow_html=False,
)

footer = legal.container(key="legal_footer")
footer.divider()
col_left, col_right = footer.columns(2)
with col_left:
    st.page_link("pages/91_Privacy.py", label="Privacy Policy")
with col_right:
    st.page_link("pages/92_Refunds.py", label="Refund & Cancellation Policy")
