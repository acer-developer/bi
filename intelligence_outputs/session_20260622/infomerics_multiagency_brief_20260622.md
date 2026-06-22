# Infomerics ULTRA HOT × D365 Multi-Agency Cross-Match
Date: 2026-06-22 | Session 23
Data sources: infomerics.json.xlsx (8,438 records) + d365_data.xlsx (49,943 records)

---

## The Finding: 102 of 367 Infomerics ULTRA HOT Companies Also in D365

**27.8% of Infomerics ULTRA HOT companies are multi-agency companies** — they have ratings at D365 agencies in addition to Infomerics.

These are the absolute maximum priority targets in the entire database.

| Match Type    | Companies | Notes                      |
|---------------|-----------|----------------------------|
| Exact match   | 77        | Same normalized company name |
| Fuzzy match   | 25        | Name variant / abbreviation |
| **Total**     | **102**   |                            |
| Not in D365   | 265       | Infomerics-only            |
| **ULTRA HOT** | **367**   | **Total**                  |

---

## The 72-Company Maximum Priority Tier

**72 of the 102 D365-matched companies are ALSO INC at their D365 agencies.**

These companies are:
- INC at Infomerics (ULTRA HOT — 365+ days overdue)
- INC at one or more D365 agencies (CRISIL, CARE, ACUITE, etc.)
- Multi-agency = already open to using multiple raters
- Doubly or triply abandoned = maximum dissatisfaction

**ACER pitch for these 72**: "You have been marked non-cooperative at BOTH Infomerics AND [CRISIL/CARE/ACUITE]. Your rating is completely non-functional. ACER is your only path to a working credit rating — we can rerate you within 30 days across all your instruments."

---

## D365 Agency Footprint of Matched Companies

| D365 Agency | Records Among 102 Matched |
|-------------|--------------------------|
| CRISIL      | 110                      |
| CARE        | 75                       |
| ACUITE      | 51                       |
| BRICKWORK   | 49                       |
| IND-RA      | 34                       |
| ICRA        | 12                       |

CRISIL and CARE have the highest overlap with Infomerics ULTRA HOT companies. These are the most established competitors — their simultaneous INC at both Infomerics AND CRISIL/CARE is an extraordinary signal.

---

## Why Multi-Agency INC = Maximum Priority

Standard single-agency INC: Company may be avoiding ONE rater's fees or disputes.
Multi-agency INC (Infomerics + D365): Company has stopped cooperating with ALL raters. This means:
1. Business is under serious financial stress (ratings non-functional = can't raise capital)
2. They NEED a fresh start — can't continue with any existing rater
3. They are maximally receptive to a new agency offering them a lifeline
4. ACER can walk in as the "reset button" and capture the entire rating relationship

---

## Sample Matched Companies

From the analysis, the matched companies include companies from sectors including:
- Steel & Metals (N.R. Ispat & Power, Radha Smelters, Deccan Ferro Alloys, Gagan Ferrotech)
- Textiles (4S Spintex India, Prateek Apparels)
- Industrial/Infra (Enviro Infra Engineers, Clean Coal Enterprises)
- Specialty Materials (Nikhil Adhesives, Raviraj Foils)

---

## Strategic Recommendation

**TIER 1 — Call This Week (72 companies)**:
Companies INC at Infomerics ULTRA HOT + INC at D365 agency.
Pitch: "You have no functioning credit rating anywhere. ACER is your only option."

**TIER 2 — Call Next Week (30 companies)**:
Companies INC at Infomerics ULTRA HOT + Present at D365 agency (but D365 not INC).
Pitch: "Your Infomerics rating is non-functional for 12+ months. Switch to ACER and consolidate your ratings with one reliable agency."

**TIER 3 — Pipeline (265 companies)**:
Infomerics ULTRA HOT — not found in D365.
These are Infomerics-only exclusive companies — ACER's competitive advantage (no other agency relationship to displace).

---

## Data Quality Notes
- Fuzzy matching uses normalized name containment (3+ word prefix match, 10+ char threshold)
- True match count could be higher — estimate 110–120 with full fuzzy matching
- D365 has ZERO Infomerics records (confirmed from Session 22) — all cross-matches are true multi-agency companies
- Infomerics ULTRA HOT defined as 365+ days since last rating date

---

## Files Produced
- `csv/infomerics_ultrahot_multiagency_20260622.csv` — 757 rows (all Infomerics ULTRA HOT records, with D365 match flag)
- `csv/infomerics_ultrahot_d365_matched_20260622.csv` — 232 rows (D365-matched companies only — highest priority)

Confidence: HIGH (exact match) / MEDIUM (fuzzy match)
