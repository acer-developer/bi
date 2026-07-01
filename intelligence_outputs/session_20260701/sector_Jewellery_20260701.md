# Jewellery Sector Mini-Brief (Forward Pipeline) — ACER Intelligence
Date: 2026-07-01 | Session 40
Data Sources: d365_data.xlsx (49,945 records) + infomerics.json.xlsx (8,438 records), via
`csv/acer_revenue_model_20260630.csv` (10,093-row forward pipeline, built from both files)
Confidence: MEDIUM (keyword sector classification; see Data Quality Note below)

---

## Why this brief exists

TODO flagged Jewellery (merged label) as having the 2nd-highest NCD rate of any sector
(22.0%, after Education) with no dedicated brief since the Session 12 split-label version
(183 companies, pre-merge, full historical population — see
`intelligence_outputs/session_20260617/sector_Jewellery_Gems_20260617.md` for geography/
seasonality, which still applies). This mini-brief scopes narrower: the **forward 9-month
calling pipeline only** (Oct 2026 – Jun 2027), i.e. companies ACER should be calling now.

**Label fix applied:** the raw pipeline carried two labels for the same sector —
"Jewellery" and "Jewellery/Gems" — a Q1-2027-source-file vs Q2-2027-source-file naming
split (same root cause Session 39 found for Energy). Merged here; matches the
`sector_revenue_density_20260630.csv` Session 39 figure (53 companies, HIGH reliability).

---

## Sector Overview (Forward Pipeline)

| Metric | Value |
|---|---|
| Unique companies | 53 |
| Total records (company × instrument) | 82 |
| Total identified amount | ₹2,238.5 Cr |
| Total avg revenue potential | ₹637.0 Lakhs (₹6.37 Cr) |
| Revenue Density Score (Session 39 methodology) | 38.6 — Rank 5 of 23 sectors |
| NCD/Bond records | 18 of 82 (22.0%) — 2nd highest sector NCD rate after Education |
| HOT urgency | 8 companies (callable now) |
| MEDIUM urgency | 14 companies |
| LOW / LOW-MEDIUM urgency | 31 companies (October 2026 / Q1 2027 windows) |

## Agency Concentration (Forward Pipeline)

| Agency | Unique Companies | Records |
|---|---|---|
| CRISIL | 20 | 28 |
| CARE | 10 | 18 |
| BRICKWORK | 6 | 8 |
| ACUITE | 5 | 8 |
| IND-RA | 5 | 5 |
| ICRA | 4 | 8 |
| Infomerics | 3 | 7 |

CRISIL holds the largest single share (38% of unique companies) but no agency is dominant —
consistent with the fragmented landscape Session 12's full-population brief found (no agency
above 27% historically). This remains a low-competitor-density sector for ACER entry.

## Instrument Mix

| Instrument | Records |
|---|---|
| Term Loan | 29 |
| NCD/Bond | 18 |
| Bank Guarantee | 9 |
| Fund-Based | 7 |
| Non-Fund-Based | 7 |
| Letter of Credit | 5 |
| Short Term Bank Facilities | 4 |
| Long Term Bank Facilities | 3 |

**NCD angle:** 18 of 82 records (22.0%) are SEBI-license-gated NCD/Bond instruments — this
is ACER's highest-value pitch in this sector once the Oct 8 SEBI CRA license lands (see
`csv/ncd_rm_plan_gap_all_agencies_20260701.csv` — 2 of the 7 Jewellery-tagged NCD company-
agency pairs from Session 38's revenue model are CARE relationships not yet in the Aug RM
deployment plan).

## Top 10 Targets by Amount

1. Shanti Gold International Limited — ₹195.4 Cr (Infomerics, Q1 2027, LOW/MEDIUM)
2. Karuna Management Services Ltd. — ₹155.0 Cr (CRISIL, Oct 2026, LOW)
3. Goldenglobe Hotels Pvt. Ltd. — ₹125.0 Cr (ACUITE, Oct 2026, LOW)
4. K T M Jewellery Ltd. — ₹115.0 Cr (CARE, NCD, Q1 2027, LOW/MEDIUM)
5. Mohit Diamonds Pvt. Ltd. — ₹108.8 Cr (CRISIL, Oct 2026, MEDIUM)
6. Ranka Jewellers Private Limited — ₹98.0 Cr (Infomerics, Oct 2026, MEDIUM)
7. Diamond Beverages Pvt. Ltd. — ₹92.2 Cr (CARE, Oct 2026, LOW) — **see data quality note**
8. Manohar Lal Sarraf & Sons Jewellers Pvt. Ltd. — ₹83.0 Cr (CARE, NCD, Q1 2027, HOT)
9. Silvertoan Papers Ltd. — ₹62.7 Cr (CARE, Oct 2026, MEDIUM) — **see data quality note**
10. Samarth Diamond — ₹56.0 Cr (Infomerics, Oct 2026, LOW)

Full list: `csv/leads_Jewellery_20260701.csv` (53 rows, all forward-pipeline Jewellery companies)

---

## ACER Pitch Angle

> "Your current rating is approaching renewal. ACER rates jewellery, gems, and diamond
> processing SMEs faster than legacy agencies, with analysts who understand the export
> cycle. Get ahead of the Q4/Q1 renewal rush — call now."

**NCD-specific script (7 companies, pending Oct 8 SEBI license):**
> "Your NCD/Bond facility needs a valid SEBI-registered rating. ACER's debt rating license
> is confirmed for October — we want to start the relationship now so you're first in line
> when we can rate you, not competing with the post-license rush."

Refer to Session 12's brief for city-cluster geography (Surat diamond processing, Mumbai
gem trade, Jaipur gem cutting) and seasonal timing (Feb–Apr ideal, pre-Diwali secondary
window) — those structural patterns are unaffected by this pipeline-scoping exercise.

---

## Data Quality Note

At least 2 of the 53 companies in this list appear **name-keyword misclassified** into
Jewellery: "Diamond Beverages Pvt. Ltd." (beverages company, not diamonds) and "Silvertoan
Papers Ltd." (paper/packaging, "silver" keyword false match). "Goldenglobe Hotels Pvt. Ltd."
is also likely a hospitality company caught by the "gold" keyword. Sector classification
uses name-based keyword matching (~85% precision per Session 12); these should be manually
verified before RM outreach, but are left in the CSV per the no-truncation rule — flagged
here instead. This reinforces the MCA CIN/NIC enrichment case (Q5, carried forward) as the
fix for keyword-classification false positives across all sectors, not just "Other."

---

## Files
- `csv/leads_Jewellery_20260701.csv` — 53 rows (forward pipeline, deduped one row/company)
- This brief: `sector_Jewellery_20260701.md`
