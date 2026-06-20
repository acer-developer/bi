# Dead Company Audit — ULTRA HOT Risk Screening
**Session 19 | 2026-06-20**
**Data: D365 + Infomerics combined ULTRA HOT universe**

---

## Purpose
Before mobilizing the sales team on 1,647 ULTRA HOT companies, screen for entities
that may be defunct (dissolved, struck-off, in NCLT liquidation) to avoid wasted calls.

---

## Total ULTRA HOT Universe
**1,647 companies** (combining D365 + Infomerics, de-duplicated)
- D365 ULTRA HOT: 1,280 companies
- Infomerics ULTRA HOT: 367 companies (99.9% not in D365)

---

## MCA API Status: BLOCKED
Live MCA API access is blocked by firewall (403 Forbidden) — same limitation as BSE/NSE fetches.
Proxy signals were used instead:

---

## Proxy Risk Scoring Results

| Risk Category | Companies | Action |
|---------------|-----------|--------|
| HIGH RISK — Name contains "Wound Up/Struck Off/NCLT" | **0** | Verify before calling |
| MEDIUM RISK — 18+ months overdue (540+ days) | **62** | Google/MCA verify first |
| LOW-MEDIUM RISK — 15+ months overdue (450+ days) | **122** | Spot-check 20-30% |
| STANDARD — Call directly | **1,463** | Call now |

**File:** `csv/ultra_hot_dead_risk_audit_20260620.csv` (1,647 rows with risk flags)

---

## Key Finding: No Name-Flagged Defunct Companies
Zero companies in the ULTRA HOT list have keywords like "wound up", "struck off",
"dissolved", or "in liquidation" in their registered name. This is a positive signal —
the 1,647 ULTRA HOT companies appear to be active entities.

---

## The 62 MEDIUM RISK Companies
These are largely from the **Infomerics dataset** with very old rating dates:
- Some Infomerics INC dates are 3-5 years old (up to 1,724 days!)
- Infomerics rating data may contain older historical records
- Recommend: Google search the company name + "MCA" before calling
- Example: "Ashapura Options Private Limited" — 1,724 days overdue (last rated ~2021)

---

## Recommended Action Protocol

**For 1,463 STANDARD companies:** Call directly using super_targets file pitch scripts.

**For 62 MEDIUM RISK companies:**
Before calling, do a 2-minute check:
1. Google: [Company Name] + India + status
2. Check: [company name].mca.gov.in (if accessible)
3. If no red flags, proceed with call

**For permanent solution:**
- Team should manually download MCA company status data
- CIN enrichment would also classify ~8,356 "Other" unclassified companies
- Upload to data/ folder: this remains the single highest-value unblocked task

---

## Implication for July Blitz
**1,463 of 1,647 ULTRA HOT companies are clean to call immediately** — 88.8% are standard.
The July 14-18 peak window (216 companies/day peak) should proceed as planned.

---

*Note: This audit used proxy signals only. Full MCA verification would require manual data upload.*
*Confidence in risk scores: MEDIUM (proxy-based, not live MCA data)*
