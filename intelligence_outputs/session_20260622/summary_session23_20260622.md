# ACER Intelligence Session 23 — Summary
Date: 2026-06-22 | Session 23 of ongoing series

---

## Data Foundation
- D365: 49,943 valid records across 6 agencies (CRISIL, CARE, ICRA, IND-RA, ACUITE, BRICKWORK)
- Infomerics: 8,438 records, 999 INC companies, 367 ULTRA HOT
- Analysis date: 2026-06-22

---

## Task 1: ACUITE 2026 Acceleration — Geographic Breakdown ✓

**Finding: ACUITE April 2026 = 128 companies INC (57.4% INC rate) — mirrors CARE spike**

Both CARE and ACUITE hit their 2026 peaks in April simultaneously. This is a structural fiscal year-end phenomenon — companies whose ratings came up for March/April renewal are refusing to cooperate at record rates.

- ACUITE INC rate trend: 37.2% (May 2025) → 57.4% (Apr 2026)
- Callable now: 83 ULTRA HOT + 265 HOT = **348 companies**
- Geographic breakdown: 97% unknown (MCA CIN needed); Gujarat/Tamil Nadu/AP visible in top states
- Key insight: ACUITE's 57.4% INC rate means ACER has a compelling pitch — "your ACUITE rating is statistically likely to be non-cooperative"

Files:
- `csv/acuite_2026_acceleration_geo_20260622.csv` (1,926 rows)
- `csv/acuite_monthly_inc_trend_20260622.csv` (12 rows)
- `acuite_2026_geo_brief_20260622.md`

---

## Task 2: Feb 2026 CARE Cohort — Targeted Call List ✓

**Finding: 183 CARE INC companies from Feb 2026 — in maximum receptivity window NOW**

These companies are 115–140 days post-INC as of today. Urgency classification = LOW (not yet 6 months), but calling rationale = HIGH RECEPTIVITY (4–5 months post-INC is the ideal window: past initial shock, not yet resigned, still actively looking for alternatives).

- 317 records, 183 unique companies
- 85% in High Risk or Default grade — these companies NEED a working rating
- Top instruments: Term Loans (122), Bank Guarantee (68), NCD (39)
- CARE context: Feb 2026 was the 2nd highest INC month before April's peak

Important correction from TODO assumption: Feb 2026 companies are NOT yet in "HOT urgency" by our scoring system (< 180 days). However, they ARE in the maximum sales receptivity window.

Files:
- `csv/care_feb2026_cohort_20260622.csv` (317 rows)
- `care_feb2026_cohort_brief_20260622.md`

---

## Task 3: Infomerics ULTRA HOT × D365 Cross-Match ✓

**Finding: 102 of 367 Infomerics ULTRA HOT companies also in D365 — 72 are ALSO INC there**

The 72-company multi-agency doubly-INC tier is the single most actionable finding of this session. These companies are INC at Infomerics (365+ days overdue) AND INC at one or more D365 agencies. Their rating is completely non-functional across the industry.

- 27.8% of Infomerics ULTRA HOT companies have a D365 footprint
- 77 exact name matches + 25 fuzzy matches = 102 total
- D365 agency overlap: CRISIL (110 records) > CARE (75) > ACUITE (51) > BRICKWORK (49)
- 72 companies also INC at D365 — ACER is their ONLY viable option for a functioning rating
- 265 Infomerics ULTRA HOT are exclusive (not in D365) — ACER's differentiated pipeline

Files:
- `csv/infomerics_ultrahot_multiagency_20260622.csv` (757 rows)
- `csv/infomerics_ultrahot_d365_matched_20260622.csv` (232 rows — D365-matched only)
- `infomerics_multiagency_brief_20260622.md`

---

## Top 5 Intelligence Findings This Session

1. **ACUITE April 2026 spike mirrors CARE** — structural fiscal year-end phenomenon; both hit record INC rates simultaneously. July 2026 will likely spike again. ACER must begin calling ACUITE HOT companies NOW, before the July cycle.

2. **72 Infomerics ULTRA HOT companies are also INC at D365 agencies** — completely non-functional ratings across the entire industry. These are ACER's maximum-priority acquisition targets. Lead with: "You have no working rating anywhere."

3. **ACUITE INC rate is 57.4%** — more than half of all companies ACUITE rated in April 2026 are non-cooperative. This destroys the ACUITE value proposition and makes ACER's pitch almost write-able without research.

4. **Feb 2026 CARE cohort (183 companies) is in peak receptivity NOW** — 4–5 months post-INC is the ideal window. These companies haven't been called yet. Term Loans (122 records) and NCD (39 records) first.

5. **27.8% of Infomerics ULTRA HOT are multi-agency companies** — the Infomerics-only assumption (from Session 22) is partially wrong: more than 1 in 4 Infomerics ULTRA HOT companies also have ratings at CRISIL, CARE, or others. ACER can displace multiple raters in a single call.

---

## Open Questions Carried Forward
- Q1: BG and LC license status — 68+40 Feb 2026 CARE companies need this confirmed
- Q2: SEBI CRA license — NCD/debt instruments across all lists require this
- Q3: MCA CIN upload — geographic classification still blocked for 97%+ of companies
- Q4: BSE SME fetch — still blocked (403 firewall)

---

## Hypotheses for Session 24
- H1: IND-RA 2026 acceleration check — have they also spiked like CARE+ACUITE?
- H2: Steel sector multi-agency master — consolidate all steel leads from sessions 2/14/16/23
- H3: April 2026 cross-agency spike — how many companies went INC at MULTIPLE agencies in April simultaneously?
- H4: 83 ACUITE ULTRA HOT + 83 CRISIL ULTRA HOT overlap — are there companies that are ULTRA HOT at both?
- H5: Infomerics + ACUITE dual-INC — ACUITE is the closest analog to Infomerics; overlap?
