# ACER Intelligence — Master Task List
Last Updated: 2026-06-12
Status: Session 2 complete. Session 3 starting next run.

---

## P1 — Do This Session (Tonight)

- [ ] Cross-filter: INC companies also in d365 (doubly hot leads)
      → Fuzzy match INC Infomerics names with d365 INC names
      → Output: csv/INC_cross_matched_[YYYYMMDD].csv
      → Columns: Company | Infomerics Rating | d365 Agency | d365 Rating | Both INC?

- [ ] Sector × INC breakdown — which sectors have highest INC rates?
      → Cross-filter leads_ALL by Sector + Lead Segment
      → Output: csv/sector_INC_breakdown_[YYYYMMDD].csv
      → Find if Textiles/Steel/Agro cluster at INC

- [ ] BSE SME company fetch (if network available)
      → URL: https://www.bseindia.com/corporates/List_Scrips.aspx
      → Filter: Segment = SME, Status = Active
      → Save raw: csv/raw/bse_sme_raw_[YYYYMMDD].csv
      → Cross match with ratings data
      → Output: csv/bse_sme_matched_[YYYYMMDD].csv

- [ ] BFSI sector brief
      → Banks, NBFCs, housing finance — major rating category
      → Output: sector_BFSI_[YYYYMMDD].md

- [ ] Chemicals/Pharma sector brief
      → Output: sector_Chemicals_[YYYYMMDD].md

---

## P2 — Next Sessions

- [ ] Fetch BSE SME listed companies
      → URL: https://www.bseindia.com/corporates/List_Scrips.aspx
      → Filter: Segment = SME, Status = Active
      → Save raw: csv/raw/bse_sme_raw_[YYYYMMDD].csv
      → Cross match with ratings data
      → Output: csv/bse_sme_matched_[YYYYMMDD].csv
      → Columns: Company | BSE Code | Sector | State | Currently Rated | Rater

- [ ] Fetch NSE Emerge listed companies
      → URL: https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv
      → Save raw: csv/raw/nse_equity_raw_[YYYYMMDD].csv
      → Cross match with ratings data
      → Output: csv/nse_matched_[YYYYMMDD].csv

- [ ] Enrich company list with director/CEO/CFO names
      → Source: https://www.zaubacorp.com
      → Source: https://www.mca.gov.in
      → Add to existing CSV: Director Name | Designation | Email if available
      → Output: csv/leads_enriched_[YYYYMMDD].csv

- [ ] Regional Territory Maps
      → Currently BLOCKED — no State column in either file
      → Unblock by: deriving state from company name / MCA enrichment
      → Once unblocked: region_North.md / region_South.md / region_West.md / region_East.md

---

## P3 — Exploratory

- [ ] Seasonal pattern analysis
      → Which months have highest new instrument issuances?
      → Output: csv/seasonal_pattern_[YYYYMMDD].csv

- [ ] Master company database
      → Unified deduped list across both files
      → Output: csv/master_company_database_[YYYYMMDD].csv
      → Columns: Company | All Raters | All Instruments | Sectors | State | Urgency Score

- [ ] ACER whitespace map
      → Region x Sector gap table
      → Output: region_whitespace_map_[YYYYMMDD].md

- [ ] Instrument family grouping
      → Short Term / Long Term / Structured Finance buckets

---

## STANDING RULE — EVERY SESSION
Every finding must have a file. No exceptions.
If Claude says "X companies qualify" → that list must exist as CSV.
All CSVs go to: intelligence_outputs/session_[YYYYMMDD]/csv/
All MDs go to: intelligence_outputs/session_[YYYYMMDD]/

---

## Completed

- [x] Repo structure created — 2026-06-11
- [x] INSTRUCTIONS.md added to repo — 2026-06-11
- [x] TODO.md initialized — 2026-06-11
- [x] Full data profiling — both files — 2026-06-11 (Session 1)
- [x] Recency scoring — both files — 2026-06-11 (Session 1)
- [x] Competitor concentration analysis — 2026-06-11 (Session 1)
- [x] Top 50 sales lead list generated — 2026-06-11 (Session 1)
- [x] Infrastructure sector brief — 2026-06-11 (Session 1)
- [x] Company overlap check — 2026-06-11 (Session 1)
- [x] INC companies extracted — 996 companies — 2026-06-12 (Session 2)
- [x] HIGH urgency leads — both files — 3,535 companies — 2026-06-12 (Session 2)
- [x] Multi-agency companies — full CSV — 3,623 companies — 2026-06-12 (Session 2)
- [x] Downgraded companies — both files — full CSVs — 2026-06-12 (Session 2)
- [x] Fuzzy company matching Infomerics ↔ d365 — 1,827 matches — 2026-06-12 (Session 2)
- [x] Sector briefs: Agro/Food, Steel & Metals, Textiles — 2026-06-12 (Session 2)
- [x] Master lead database — 10,768 leads — leads_ALL_20260612.csv — 2026-06-12 (Session 2)
