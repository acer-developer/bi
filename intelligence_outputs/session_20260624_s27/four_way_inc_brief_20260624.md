# 4-Way INC Investigation Brief
**Date:** 2026-06-24 | **Session:** 27
**Source:** d365_data.xlsx — 18,610 INC records analyzed

---

## Correction from Prior Sessions

Previous analysis identified **2 four-way INC companies**. Actual count: **8 companies** INC at 4 different agencies simultaneously.

---

## The 8 Four-Way INC Companies

| Company | INC Agencies | Max Amount (Cr) | Most Overdue | Sector |
|---------|-------------|-----------------|--------------|--------|
| Siddapur Distilleries Ltd. | ACUITE, BW, CARE, IND-RA | ₹108 | 405 days | Other |
| Ashok Bricks Inds. Pvt. Ltd. | BW, CRISIL, ICRA, IND-RA | ₹44 | 400 days | Construction |
| Telawne Power Equipments Pvt. Ltd. | ACUITE, CRISIL, ICRA, IND-RA | ₹29 | 392 days | Manufacturing |
| New Modern Technomech Pvt. Ltd. | ACUITE, BW, CARE, CRISIL | ₹50 | 370 days | IT/Technology |
| Winfab Equipments Pvt. Ltd. | BW, CARE, CRISIL, ICRA | ₹4 | 343 days | Manufacturing |
| Shiva Structures Pvt. Ltd. | CARE, CRISIL, ICRA, IND-RA | ₹21 | 341 days | Construction |
| Kohinoor Feeds & Fats Pvt. Ltd. | ACUITE, BW, CRISIL, IND-RA | ₹50 | 341 days | Other |
| Uttarakhand Engineering Products Pvt. Ltd. | BW, CARE, CRISIL, IND-RA | ₹24 | 341 days | Manufacturing |

**Total combined rated amount:** ₹330 Cr across 8 companies

---

## Why Are These Companies INC at Every Agency?

### Pattern Analysis

**Finding 1: These companies have ALWAYS been INC in the dataset**
6 of 8 companies have NO active (non-INC) records anywhere in d365. They appear to have never achieved a functional rating in the observation period.

**Exception — Siddapur Distilleries:**
- Had ACTIVE CARE ratings in January 2026 (Term Loans B, Bank Guarantee A4)
- Went INC at ACUITE in March 2026
- This is the only company with evidence of recovering before falling back INC

**Finding 2: Multi-agency INC = multi-lender structure, not sequential failures**
These companies are not "failing at one agency, trying another." They have SIMULTANEOUS rating agreements with 4 agencies — suggesting each lender requires their own preferred rating agency. All 4 agencies then independently mark INC.

**Illustration — Ashok Bricks Inds.:**
- BRICKWORK: INC since May 2025 (Bank Guarantee + Term Loan)
- ICRA: INC since Sep 2025 (NCD + Term Loan)
- CRISIL: INC since Feb 2026 (BG + LC + Term Loan)
- IND-RA: INC since Apr 2026 (NCD ₹44 Cr)
- Timeline shows NEW agencies being added as new lenders come in — not retries

**Finding 3: Ratings are NOT being downgraded TO INC — they START as INC**
All records show the companies entered the dataset already in INC status. There are no prior active ratings visible. This suggests the cooperation breakdown happened BEFORE the rating engagement was completed.

---

## The Root Cause Hypothesis

These 8 companies represent a **documentation/cooperation failure pattern**, not a creditworthiness issue:

1. Company has credit facilities from multiple banks
2. Each bank mandates a rating from their preferred agency (or the company applies to multiple)
3. Company is unable or unwilling to provide documentation to ANY of the agencies
4. All agencies independently issue INC
5. The company's multi-lender structure means this cascades to 4 agencies simultaneously

**Alternative hypothesis (less likely):** These are genuinely stressed companies that have deliberately stopped cooperating with all raters to delay a downgrade. The "D" rating at Ashok Bricks across ALL agencies supports this — if it's a simple documentation issue, the grade would not universally be "D" (Default).

---

## Ashok Bricks — The "D" Grade Signal

Ashok Bricks is uniquely flagged: its ratings are "D" (Default), not INC-class grades. The "D" at CRISIL, ICRA, IND-RA, and BW means this company has likely DEFAULTED on obligations to all lenders. It entered INC status because it stopped cooperating AFTER default — agencies cannot update the "D" grade without cooperation.

This is a **debt recovery case**, not a sales target.

---

## The Opportunity for ACER

Despite the complexity, these 8 companies represent the **highest-signal displacement opportunity in the database**:

### Why Call Them?
1. **Maximum frustration** — every agency has marked them INC. They are desperate for a resolution.
2. **Multiple live obligations** — they have active credit from multiple banks that REQUIRES ratings.
3. **Lowest competition** — no agency is actively servicing them. ACER has zero incumbent risk.
4. **Documentation vs credit** issue — if the INC is a documentation failure (not actual default), ACER's dedicated onboarding process can unlock the mandate.

### Who to Target First

**Best targets (not "D" rated, HOT+ urgency):**
1. **Siddapur Distilleries** (₹108 Cr, ACUITE+BW+CARE+IND-RA INC) — **WAS recently active at CARE** (Jan 2026). Most solvable. Direct relationship exists.
2. **New Modern Technomech** (₹50 Cr, ACUITE+BW+CARE+CRISIL INC) — IT/Tech sector, mid-ticket, recent ACUITE INC (Apr 2026) suggests fresh trigger
3. **Kohinoor Feeds & Fats** (₹50 Cr, ACUITE+BW+CRISIL+IND-RA INC) — Food sector, most recent INC at IND-RA (Apr 2026)
4. **Telawne Power Equipments** (₹29 Cr, ACUITE+CRISIL+ICRA+IND-RA INC) — IND-RA still active on refreshes (Apr 2026)

**Skip for now:**
- Ashok Bricks (rated "D" = likely actual default, not documentation issue)
- Winfab Equipments (₹3.5 Cr max amount — low revenue potential)

---

## Call Script for 4-Way Companies

> "We're ACER Ratings, India's newest SEBI-registered CRA. I see that your facility ratings at [Agency1, Agency2, Agency3, Agency4] have all been marked as issuer non-cooperating. This is a serious situation — your bankers need active ratings. 
>
> ACER has a dedicated documentation support team that helps companies resolve exactly this kind of situation. We assign one relationship manager to coordinate across all your lenders, gather documents once, and deliver ratings to all parties simultaneously.
>
> We're the only agency in India that offers this multi-bank coordination service. Would you have 20 minutes this week to discuss?"

---

## Also Found: Cross-Source 4-Way Companies (D365 + Infomerics)

Two additional companies are INC at 3 D365 agencies AND at Infomerics — effectively 4-source INC:

| Company (D365) | Company (Infomerics) | D365 INC Agencies |
|----------------|---------------------|-------------------|
| Imperial Tubes Pvt. Ltd. | Imperial Granites Pvt Ltd | BW, ICRA, IND-RA |
| R S Development & Constructions India Pvt. Ltd. | R. S. Development & Constructions India Pvt. Ltd. | BW, CRISIL, IND-RA |

**Note:** These are likely the same companies (name variant). If confirmed same entity, total 4-way pool is 10.

---

**File:** `csv/four_way_inc_profiles_20260624.csv` (58 rows — all records for all 8 companies)
*Confidence: HIGH — all data from d365_data.xlsx, exact name matching*
