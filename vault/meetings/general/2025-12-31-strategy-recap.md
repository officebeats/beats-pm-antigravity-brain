# 🎙️ Meeting Recap: Strategy & Roadmap Kick-off
**Date**: December 31, 2025  
**Stakeholders**: Ernesto, Ricardo, Jack, Dom, Bill, Agnielly

## 🎯 Executive Summary
The team pivoted the 120-day focus exclusively to **Pre-Award (Up to Award)** features. The primary goals are to drive liquidity (2,000 contractors, 40 primes) and establish predictable revenue paths through lead flipping and subscriptions.

---

## ⚡ Key Strategic Pillars & Feature Requests

## ⚡ Key Strategic Pillars & Feature Requests

### 1. The Leads Module ("Flipping Leads")
*   **The Concept**: Enabling Primes to post leads they don't want (too small, wrong market) for Subcontractors to purchase.
*   **Requirements**:
    *   **Tiered Distribution**: Standard leads are 1-to-1 (exclusive); Large contracts (>$5k/mo) are 1-to-3 (shared bidding).
    *   **Dynamic Pricing**: Pricing model with a "timer" logic where lead price drops as it ages.
    *   **Verification Guarantee**: Verified phone numbers; restricted refund policy to "Credit-only" for invalid data.
    *   **Integrity Automation**: A "Breakaway/Handoff" script/email sent to clients introducing the Sub once the lead is flipped.
    *   **Data Mapping**: System-to-system ingest (API) or standardized intake form to map diverse Prime data fields to Route DB.
*   **User Journey**:
    1.  **Prime** receives an unserviceable inbound lead (too small or out of area).
    2.  **Prime** uploads details (manual or via API); lead is rebranded as a "Route Opportunity."
    3.  **Subcontractor** sees opportunity card on map, identifies as "Leads" category.
    4.  **Subcontractor** pays via Stripe (seeing transparency on "1 of 3 applicants" if applicable).
    5.  **Subcontractor** receives instant contact info; **Client** receives handoff intro.
*   **Open Questions**:
    *   What is the specific % revenue share for the Prime?
    *   Do we provide the email script or does the Prime provide it?
*   **Follow-ups/Tasks**:
    *   **Jack**: Draft the lead handoff email script.
    *   **Mitesh**: Map incoming data fields from CSV to lead object.

### 2. Contractor Network MVP
*   **The Concept**: A centralized tool for Primes to manage their own private "bench" of subcontractors instead of using spreadsheets.
*   **Requirements**:
    *   **Private Database**: Secure, per-prime workspace for managing existing vendors.
    *   **Status Management**: Kanban or List view with statuses: Active, Onboarding, Under Review, Approved, On Hold, Blacklisted (Do Not Use).
    *   **Bulk Infrastructure**: Hub for bulk-inviting subs via CSV template (Name/Email) to claim their Route profiles.
    *   **Compliance Vault**: Central repository for W-9, COI, and Business Licenses per sub.
    *   **Filtering**: Ability to filter the private network by liability amount, service type, or compliance status.
*   **User Journey**:
    1.  **Prime** enters "My Network" and uploads an Excel list of 60+ current subs.
    2.  **System** blasts invites; **Subs** claim profiles and upload missing documents.
    3.  **Prime** views dashboard to see who is "Active" vs "Expired COI."
    4.  **Prime** posts a job and selects "Invite My Network" to skip public search and target their trusted bench immediately.
*   **Open Questions**:
    *   Will subs have a separate login or use the existing one?
    *   How do we handle subs who are already on the platform?
*   **Follow-ups/Tasks**:
    *   **Dom**: Design the "Network Sidebar" and private list view.
    *   **Mitesh**: Build the bulk CSV invite parser.

### 3. Property Manager / Prospect Search
*   **The Concept**: A "Google Places" style search within Route to find commercial prospects (medical, restaurants, PMs).
*   **Requirements**:
    *   **Integrated Map Search**: Pulling Google API data (Phone, Email, Web) directly into the Exchange interface.
    *   **ICP Targeting**: Search filters for specific market segments (e.g., "Medical Clinics," "Real Estate Brokers").
    *   **AI Enrichment**: "ZenWiz" style logic to verify/find emails for the search results (Phase 2).
    *   **Campaign Tool**: Bulk "Prospect List" generation with outreach status tracking (Sent vs. Responded).
    *   **Email Templates**: Integration of Bill/Ricardo’s proven scripts for cold outreach within the platform.
*   **User Journey**:
    1.  **Subcontractor** wakes up to no active local opportunities.
    2.  **Subcontractor** searches "Property Managers" in their ZIP code.
    3.  **Subcontractor** builds a "Prospect List" of 50 local offices.
    4.  **Subcontractor** selects an email template and hits "Send" (throttled to avoid spam).
    5.  **Subcontractor** manages replies directly within the Route Communications hub.
*   **Open Questions**:
    *   Google Places API cost at scale?
    *   ZenWiz API partnership terms?
*   **Follow-ups/Tasks**:
    *   **Ricardo**: Email Matt R. Santos (ZenWiz) for pricing.
    *   **Dom**: Verify Google Places data accuracy for "Janitorial Services."

### 4. Profile 2.0 (Deep Vetting Fields)
*   **Requirements**:
    *   **Technical Identifiers**: New fields for NAICS codes, SAM.gov registration, and Federal Security Clearance status.
    *   **Safety Metrics**: Dedicated field for EMR (Safety) ratings.
    *   **W2 vs 1099**: Headcount breakdown fields for workforce transparency.
    *   **Video Integration**: Native 30-second "Video Pitch" upload (Premium feature).
    *   **Lead Magnet UI**: "Empty Space" labels (e.g., "No Video Present") to nudge contractors toward completions/upsells.
*   **User Journey**:
    1.  **Subcontractor** updates profile to include their SAM.gov code and 30s video intro.
    2.  **Prime** performs an "Advanced Search" for subs with security clearance in Grand Rapids.
    3.  **Prime** watches the 30s video to verify "Brand Integrity" before inviting to bid.
*   **Open Questions**:
    *   Storage limits for video uploads?
    *   Is SAM.gov data available via API (lookup)?
*   **Follow-ups/Tasks**:
    *   **Mitesh**: Add NAICS, SAM, and Security Clearance fields to the DB.
    *   **Dom**: Add "Video Placeholder" for profiles without videos to nudge them.

### 5. "Bid" Integration & Promo
*   **Requirements**:
    *   **Cross-Product Modal**: Pop-up banner or sidebar link within Exchange for the "Bid" toolkit.
    *   **Coupon Logic**: Single-use token logic for $49.99/yr special pricing for Exchange subscribers.
    *   **Onboarding Portal**: Dedicated Circle space for "Bid Pros" led by Alejandro Flores.
    *   **Live Training**: Scheduled 1-hour weekly live coaching sessions (marketing focus).
*   **User Journey**:
    1.  **User** sees a "Power Up Your Bidding" call-out on the dashboard.
    2.  **User** clicks, pays $49.99, and is redirected to their login for Bid.
    3.  **User** receives invite to weekly Alejandro Flores coaching sessions.
*   **Open Questions**:
    *   How to handle existing Bid users?
    *   Discount code duration (annual vs lifetime)?
*   **Follow-ups/Tasks**:
    *   **Bill**: Create the $49.99 coupon in Stripe.
    *   **Ricardo**: Confirm Alejandro Flores's 1-hour/weekly commitment.

### 6. Resource Library Market
*   **Requirements**:
    *   **Marketplace Sidebar**: Sidebar link for one-time purchases (Templates, Ebooks).
    *   **Pop-up Checkout**: In-app purchase flow without full site redirect.
    *   **Asset Integration**: Purchased contracts must auto-populate the user’s "Document Hub."
*   **User Journey**:
    1.  **User** needs a "Master Subcontractor Agreement."
    2.  **User** goes to Resource Library, views the $99 template, and buys via Stripe.
    3.  **System** drops the PDF template into their Chat Document Hub for immediate use.
*   **Open Questions**:
    *   Which TJS assets are high-priority for launch?
*   **Follow-ups/Tasks**:
    *   **Bill**: Inventory the best-selling TJS templates for flip-to-Exchange.

### 7. Chat Document Hub & Message Templates
*   **Requirements**:
    *   **Company Folder System**: Multi-folder hierarchy (e.g., Prime Folder vs. Sub Folder).
    *   **Vetting Subfolders**: Pre-defined slots for "Vetting Questions" and "Vetting Answers."
    *   **Attach-from-Cloud**: Ability to attach files directly from the Hub in any chat thread.
    *   **Templated Messages**: "Copy/Paste" library of saved phrases/questions for high-frequency hiring.
*   **User Journey**:
    1.  **Prime** opens 10 chats for one cleaning job.
    2.  Instead of re-uploading the same PDF 10 times, the **Prime** clicks "Add from Hub" and selects their "Vetting Template."
    3.  **Sub** responds with "Saved Response #1" to common questions.
*   **Open Questions**:
    *   Can users create subfolders?
    *   Permission levels for "Company" folders vs "Personal" templates?
*   **Follow-ups/Tasks**:
    *   **Dom**: Map out the Doc Hub folder hierarchy (Prime vs Sub).

### 8. HubSpot Sync & Segmentation
*   **Requirements**:
    *   **Cron Job Logic**: Twice-daily data sync of all new users/activities.
    *   **Segmentation Logic**: Tagging accounts as "Subscriber," "Purchaser," "Bid User," or "TJS Lead."
    *   **Activity Triggers**: Automated email sequences triggered by "Inactivity" (e.g., haven't searched in 7 days).
*   **User Journey**:
    1.  **User** purchases a Lead.
    2.  **HubSpot** syncs the event; User is moved to the "Lead Nurture" email campaign automatically to ensure they close the deal.
*   **Open Questions**:
    *   Do we sync individual "Opportunity Views"?
*   **Follow-ups/Tasks**:
    *   **Mitesh**: Setup twice-daily cron for user segment sync.

---

## 📅 Immediate Action Items (Today/Tomorrow)

| Stakeholder | Task | Priority |
| :--- | :--- | :--- |
| **Ernesto/Dom** | Prioritize 2-3 items per "Bucket" (Search, Profile, Chat) | 🔥 High |
| **Jack** | Schedule monthly check-ins with all founding primes | ⚡ Med |
| **Ricardo** | Outreach to Matt R. Santos (ZenWiz) for partnership demo | ⚡ Med |
| **Matesh/Dom** | Implement Multi-location select in Matching Algorithm | ⚙️ Dev |
| **Ernesto** | Execute Q1 Financial Data Pull (BR-103) | 🔥 High |

---

## 📋 Roadmap Adjustments (Next 90 Days)
- [ ] **Bid Pro Program**: Alejandro Flores to lead 1hr/wk demos.
- [ ] **Bid Promo**: $49.99/yr offer inside Exchange via coupon code.
- [ ] **Profile 2.0**: Add NAICS, SAM.gov, and 30-sec Video Intro.
- [ ] **Resource Library**: TJS one-time purchase integration in sidebar.

---

## 💡 Notable Quotes
*   *Jack*: "90 days from now, we've got to be looking at... a predictable path to profitability."
*   *Ricardo*: "I'd rather have a janky ladder that lets me get up to my floor instead of a perfect two-step ladder."
*   *Dom*: "If our platform needs pop-ups and a wizard... that means it's not built right."
