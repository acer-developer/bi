# ACER Intelligence Session Summary — Session 17
**Date:** 2026-06-19 | **Run time:** ~21:00 IST

---

## What Was Done This Session

### 1. ACUITE Displacement Playbook (P1 — COMPLETE)
- Full ACUITE INC analysis from d365_data.xlsx
- **911 unique ACUITE INC companies** (41.6% INC rate)
- 89 ULTRA HOT + 454 HOT + 368 WARM
- Highest INC instruments: LC (52.2%), Fund-based (50.0%), Term loans (43.6%), BG (43.4%)
- Pitch scripts written for each instrument type
- Files: `csv/acuite_displacement_master_20260619.csv` (1,926 rows) + `csv/acuite_ULTRA_HOT_only_20260619.csv` (164 rows)
- Brief: `acuite_displacement_brief_20260619.md`

### 2. CARE Vulnerability Analysis (P2 — COMPLETE)
- Full CARE INC analysis
- **1,722 unique CARE INC companies** (27.4% INC rate)
- 271 ULTRA HOT + 787 HOT + 664 WARM
- Highest INC: LC (46.1%), BG (41.5%), Fund-based (37.5%)
- Strategic note: CARE = largest absolute INC pool (1,722 vs 911 for ACUITE) but lower INC rate
- Files: `csv/care_displacement_master_20260619.csv` (3,020 rows) + `csv/care_ULTRA_HOT_only_20260619.csv` (471 rows)
- Brief: `care_vulnerability_brief_20260619.md`

### 3. IND-RA Displacement Master (P2 — COMPLETE)
- **1,412 unique IND-RA INC companies** (33.0% INC rate)
- 42 ULTRA HOT + 955 HOT
- KEY FINDING: IND-RA Non-government Debt 53.5% INC — highest NCD INC rate in dataset
- Caveat: NCD/bond segment requires ACER SEBI license
- File: `csv/indra_displacement_master_20260619.csv` (1,706 rows)

### 4. Full Competitor Vulnerability Matrix (P2 — COMPLETE)
- All 6 agencies scored and ranked
- Attack sequencing: Phase 1 (BW+ACUITE), Phase 2 (CRISIL+CARE), Phase 3 (IND-RA+ICRA)
- **Total displacement pool: 10,338 INC companies | 1,429 ULTRA HOT | 5,489 HOT**
- Files: `csv/competitor_vulnerability_summary_20260619.csv`
- Brief: `competitor_master_brief_20260619.md`

### 5. Regional City Cluster Analysis (H2 — PARTIAL)
- City name inference from 49,945 D365 company names
- 409 companies geolocated (1.7% coverage)
- 79 city clusters mapped; 163 unique INC companies geolocated
- **Anand (Gujarat): 60% INC, 10 ULTRA HOT — highest priority field visit**
- **Indore (MP): 69.2% INC rate — Tier 2 Central India whitespace**
- Files: `csv/geographic_clusters_20260619.csv` + `csv/city_cluster_summary_20260619.csv`
- Brief: `regional_clusters_brief_20260619.md`

---

## Key Findings

1. **ACUITE is the immediate P1 target after Brickwork.** 41.6% INC rate, 89 ULTRA HOT companies needing same-week call. LC (52.2% INC) and Fund-based (50.0% INC) are the entry instruments.

2. **CARE's absolute INC pool is the largest in the dataset: 1,722 companies.** Higher CARE brand loyalty means lower close rate, but 271 ULTRA HOT are in active compliance crisis — these will listen.

3. **IND-RA has a hidden NCD/Bond opportunity: 53.5% NCD INC rate.** If ACER secures SEBI bond rating license, 674 IND-RA NCD records become immediately actionable. This single unlock could be worth ₹100+ Cr AUM.

4. **The total ACER displacement pipeline across all 6 agencies: 10,338 companies.** Of these, 6,918 are HOT or ULTRA HOT — callable now. This is the market waiting for ACER.

5. **Anand (Gujarat) is the single best city cluster to target.** 40 companies, 60% INC rate, 10 ULTRA HOT. Dairy/food processing sector. A single day-trip produces 24+ potential clients. No competitor has a local presence.

---

## Hypotheses for Session 18

- H1: **CRISIL INC master** — 3,429 companies (36.6% INC); build CSV for Q3 targeting; strategy note: approach CRISIL INC companies that also have Brickwork/ACUITE INC (already using multiple raters)
- H2: **Infomerics-only whitespace** — 8,438 Infomerics records; which sectors/companies appear ONLY in Infomerics (no D365 equivalent) — these are companies rated by a small agency only, perfect for ACER pitch
- H3: **July renewal calendar precision** — From the 527 ULTRA HOT in outreach dashboard, build a daily calling schedule for July 2026 (which companies hit 12 months on which date in July)
- H4: **SEBI license gap analysis** — Map ACER's current product capability vs all INC instruments; calculate how many leads are currently inaccessible (NCD, Bond segments require SEBI registration)
- H5: **"Dead company" audit** — Some INC companies may be defunct (liquidated, dissolved). Cross-check ULTRA HOT list against known signals (company name patterns, rating grades like "D" before INC).

---

## Data Quality Notes
- d365_data.xlsx: 49,945 records confirmed. All 6 agencies present.
- INC flag: 'Y' / 'N' (one header row artifact excluded)
- Date parsing: All dates in DD-MM-YYYY format parsed successfully
- City inference: 1.7% coverage — useful directionally, not statistically significant
- CRISIL has "Medium-term loan" (6 records, 66.7% INC) — very small sample, not representative

---

## Open Questions
- Q1: BSE SME / NSE Emerge data — blocked 17 sessions; team MUST manually download
- Q2: ACER BG rating product capability — does ACER have SEBI registration for Bank Guarantees?
- Q3: ACER NCD/bond license — unlocks IND-RA + CRISIL NCD segment (1,000+ companies)
- Q4: MCA CIN data — upload would unlock full regional map (currently 1.7% coverage → 100%)
- Q5: ACUITE playbook — should field team start with ULTRA HOT 89 companies this week?

---

## Files Created This Session

```
intelligence_outputs/session_20260619/
  csv/
    acuite_displacement_master_20260619.csv       1,926 rows
    acuite_ULTRA_HOT_only_20260619.csv              164 rows
    care_displacement_master_20260619.csv          3,020 rows
    care_ULTRA_HOT_only_20260619.csv                471 rows
    indra_displacement_master_20260619.csv         1,706 rows
    competitor_vulnerability_summary_20260619.csv     6 rows (agency summary)
    geographic_clusters_20260619.csv                409 rows
    city_cluster_summary_20260619.csv                79 rows
  acuite_displacement_brief_20260619.md
  care_vulnerability_brief_20260619.md
  competitor_master_brief_20260619.md
  regional_clusters_brief_20260619.md
  summary_session17_20260619.md  (this file)

session_logs/session_20260619_2100.md
```
