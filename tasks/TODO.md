# ACER Intelligence — Master Task List
Last Updated: 2026-06-12
Status: Session 1 complete. Session 2 starting tonight.

---

## P1 — Do This Session (Tonight)

- [ ] Extract ALL INC companies from infomerics data
      → Companies with "(INC)" in rating = walked out on Infomerics
      → These are hottest possible leads — need new agency immediately
      → Output: csv/INC_companies_[YYYYMMDD].csv
      → Columns: Company | Instrument | Rating | Date | Urgency | Pitch Angle

- [ ] Extract ALL HIGH urgency companies from both files
      → Rating date older than 12 months = overdue for renewal
      → Output: csv/high_urgency_leads_[YYYYMMDD].csv
      → Columns: Company | Rater | Instrument | Rating | Date | Days Overdue

- [ ] Extract ALL multi-agency companies from d365
      → 3,623 companies use 2+ agencies — full list needed not just count
      → Output: csv/multi_agency_companies_[YYYYMMDD].csv
      → Columns: Company | Agencies Used | Agency Count | Last Rating Date

- [ ] Extract ALL downgraded companies from both files
      → 1,380 from Infomerics + 5,608 from d365 = full lists needed
      → Output: csv/downgraded_infomerics_[YYYYMMDD].csv
      → Output: csv/downgraded_d365_[YYYYMMDD].csv
      → Columns: Company | Previous Rating | Current Rating | Date | Rater

- [ ] Fuzzy match Infomerics companies with d365 companies
      → Use rapidfuzz library
      → True overlap likely 200-500 companies
      → Output: csv/matched_companies_[YYYYMMDD].csv
      → Columns: Infomerics Name | d365 Name | Match Score | Combined Data

- [ ] Sector briefs for remaining sectors
      → Agro/Food → sector_AgroFood_[YYYYMMDD].md
      → Steel & Metals → sector_SteelMetals_[YYYYMMDD].md
      → Textiles → sector_Textiles_[YYYYMMDD].md

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
