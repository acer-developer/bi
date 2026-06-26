# IND-RA NCD INC — Standalone Deep-Dive
**Date:** 2026-06-26 | **Session:** 30
**Data Sources:** d365_data.xlsx (49,943 records) + infomerics.json.xlsx (8,438 records)

---

## Summary

IND-RA is the **largest NCD INC agency** in the dataset with 663 unique companies
(53.5% INC rate on Non-government debt instruments). This is the first time
IND-RA's NCD INC book has been profiled as a standalone.

| Metric | Value |
|--------|-------|
| Total IND-RA NCD records | 1,260 |
| IND-RA NCD INC records | 674 |
| IND-RA NCD INC unique companies | **663** |
| NCD INC rate | **53.5%** — highest of any agency-instrument pair |
| Total identified NCD amount | ₹40,918 Cr |
| Average per record | ₹60.7 Cr |
| Callable now (ULTRA HOT + HOT) | **373 unique companies** |

---

## Urgency Breakdown

| Urgency | Companies | % |
|---------|-----------|---|
| ULTRA HOT (365+ days) | 4 | 0.6% |
| HOT (180–364 days) | 369 | 55.7% |
| MEDIUM (90–179 days) | 171 | 25.8% |
| LOW (< 90 days) | 119 | 17.9% |

**373 companies are callable immediately (ULTRA HOT + HOT).**

Note: ULTRA HOT count is low (only 4) because most IND-RA NCD INC records
are concentrated in 2025 H2 / early 2026 — they entered HOT status recently.
The HOT cohort of 369 companies is extremely large and actionable NOW.

---

## Top Sectors

| Sector | Companies | ULTRA HOT | HOT | Total Amount (₹ Cr) |
|--------|-----------|-----------|-----|---------------------|
| Other (unclassified) | 218 | 0 | 126 | 16,483 |
| Construction | 93 | 1 | 59 | 7,569 |
| Steel & Metals | 45 | 0 | 29 | 1,503 |
| Manufacturing | 42 | 0 | 26 | 1,548 |
| Agro/Food | 39 | 1 | 20 | 2,910 |
| Chemicals/Pharma | 39 | 0 | 20 | 1,105 |
| IT/Technology | 31 | 1 | 15 | 1,278 |
| Textiles | 29 | 0 | 17 | 1,585 |
| Energy | 25 | 0 | 12 | 3,206 |
| Automobiles | 22 | 0 | 8 | 626 |

---

## Largest Targets by NCD Amount

| Rank | Company | Amount (₹ Cr) | Urgency | Sector |
|------|---------|---------------|---------|--------|
| 1 | P E C Ltd. | 3,432 | MEDIUM | Other |
| 2 | Rolta India Ltd. | 2,783 | MEDIUM | Other |
| 3 | Ushdev International Ltd. | 2,550 | MEDIUM | Other |
| 4 | Supreme Infrastructure India Ltd. | 1,894 | HOT | Construction |
| 5 | S R S Ltd. | 835 | MEDIUM | Other |
| 6 | A G S Transact Technologies Ltd. | 761 | MEDIUM | IT/Technology |
| 7 | Patil Construction & Infrastructure Ltd. | 728 | MEDIUM | Construction |
| 8 | John Energy Ltd. | 650 | HOT | Energy |
| 9 | Shri Ambalika Sugar Pvt. Ltd. | 550 | HOT | Agro/Food |
| 10 | Pratibha Syntex Ltd. | 549 | HOT | Other |

---

## Key Intelligence

1. **53.5% INC rate** — more than half of all IND-RA NCD-rated companies are non-cooperating.
   This is the highest NCD INC rate of any agency.

2. **369 HOT companies** — these entered 6–12 months ago (mid-2025 to late-2025).
   Most are approaching the 12-month ULTRA HOT threshold in Q3 2026. Optimal
   calling window: NOW through September 2026.

3. **Construction is the #1 classified sector** (93 companies, ₹7,569 Cr) — consistent
   with IND-RA's known strength in infrastructure/project finance.

4. **SEBI CRA license required** before pitching NCD instruments to any of these companies.
   Without it: only informational outreach possible.

5. **NCD INC ranking confirmed:**
   - IND-RA: 663 companies | ₹40,918 Cr (HIGHEST)
   - CARE: 454 companies | ₹56,923 Cr (HIGHEST amount)
   - ICRA: 282 companies | ₹24,330 Cr
   - BRICKWORK: 82 companies | ₹3,001 Cr
   - CRISIL: 3 companies | ₹3,418 Cr
   - ACUITE: 0 companies (confirmed)

---

## Files
- `csv/indra_ncd_inc_standalone_20260626.csv` — 674 records (663 unique companies), full detail
- `csv/indra_ncd_inc_sector_summary_20260626.csv` — 20 sectors, amounts and urgency counts
