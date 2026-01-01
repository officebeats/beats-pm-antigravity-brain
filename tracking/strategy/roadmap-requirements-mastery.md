# 🗺️ Strategic Roadmap & Requirements Mastery (Q1 2026)

> **Synthesis Key**: Joined Strategic Priorities (`Route Prioritization.xlsx`) with Detailed Requirements (`Linear CSV`).

---

## ⚡ PHASE 1: THE "NOW" (High Urgency | Activation)

_Focus: Stabilizing the core Marketplace experience and fixing registration friction._

### 1. Workforce Definition: W2 vs 1099 (ROUTE-588 / ROUTE-553)

- **Strategic Goal**: Fix legal/compliance blockers for primes vetting subs.
- **Requirements**:
  - Add distinct fields: **Total Workforce**, **W-2 Employees**, **1099 Independent Contractors**.
  - Metrics: Calculate % of work subcontracted vs self-performed.
  - **Acceptance Criteria**: Separation of headcount in company profiles; clear labeling in communication to help contractors maintain their legal classification.

### 2. Chat Functionality Feedback (ROUTE-557)

- **Strategic Goal**: Reduce user friction and improve marketplace density.
- **Requirements**:
  - Unread message alerts (Connections (2)).
  - Persistent Date/Time stamps on messages.
  - Mandatory "Reason for Decline" comment field for applicants.
  - **Acceptance Criteria**: Both Prime and Sub views must show unread counts; daily 3 PM email digest for missed messages.

### 3. 24-Hour Bidding Tool (ROUTE-550)

- **Strategic Goal**: Empower primes with "emergency" labor needs.
- **Requirements**:
  - Quick-action "24-Hour" icon on opportunity creation.
  - **Acceptance Criteria**: Clicking button auto-sets bid deadline to +24hrs; overrides manual date but allows subsequent adjustment.

---

## 🚀 PHASE 2: THE "NEXT" (Medium Urgency | Expansion & Auto)

_Focus: Using AI to scale operations and expanding the network beyond cleaning._

### 4. AI Call Bots - autogenz.ai (ROUTE-618)

- **Strategic Goal**: Prevent missed revenue from unanswered lead calls.
- **Requirements**:
  - Integration with `autogenz.ai` voice assistant.
  - **Acceptance Criteria**: Lead capture and automated scheduling for service providers.

### 5. COI AI Text Scanning MVP (ROUTE-607 / ROUTE-601)

- **Strategic Goal**: Automate the vetting bottleneck.
- **Requirements**:
  - AI-driven scan of uploaded Certificate of Insurance.
  - Validate **Expiration Date** and **Company Name** against profile.
  - **Acceptance Criteria**: System shows Pass/Fail status instantly; automated alerts at 90/60/30 days for contractors.

### 6. Email Flow Automation (ROUTE-564)

- **Strategic Goal**: Professionalize the award/loss process.
- **Requirements**:
  - Centralized summary page for awarded opportunities.
  - Automated "Awarded", "Lost", and "Not Approved" emails.
  - **Acceptance Criteria**: Emails must include primary contact's **Cell Phone** for immediate project coordination.

---

## 📋 PHASE 3: THE "LATER" (Strategic Backlog)

_Focus: Long-tail value drivers and platform polish._

- **Pitch Field (ROUTE-591)**: Allow subs to add a custom comment to their bid to move past just "lowest price".
- **Ratings & Reviews (ROUTE-579)**: Establish trust via 1-5 star ratings with 1/2 star increments; transparent counter-responses between Prime and Sub.
- **Branch Copying (ROUTE-595)**: Allow national accounts (Jan-Pro) to copy master profiles to 100+ locations effortlessly.

---

## 🛠️ The "Never" List (Strategic Alignment)

_Items identified as "Remove/Never" to preserve resource bandwidth:_

- **Bulk Import (General)**: Simplified to focused CSV templates for now.
- **Residential Filtering**: Restricted to Commercial only to preserve brand positioning.
- **Unmanaged Integrations**: Avoid VendorPM/MyCOI integrations temporarily in favor of local AI scanning (ROUTE-607).

---

## 📍 Next Action for Ernesto

1. **Validate "Workforce Definition" Specs**: Check if Mitesh is ready to implement the W-2/1099 separation fields.
2. **Review Chat Alerts**: Schedule a 15m review with Dom to confirm the 3 PM email digest logic.
