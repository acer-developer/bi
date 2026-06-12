# ACER Intelligence — Master Task List
Last Updated: 2026-06-12
Status: Session 3 complete. Session 4 starting next run.

---

## P1 — Do This Session (Tonight)

- [ ] Sub-sector breakdown of 160 doubly-INC companies
      → Which sectors do these ultra-hot leads cluster in?
      → Output: csv/doubly_INC_sector_breakdown_[YYYYMMDD].csv
      → Also: are they mostly BFSI, Chemicals, or Manufacturing?

- [ ] BFSI HIGH + INC overlap — ultimate BFSI hot list
      → Companies that are BOTH HIGH urgency AND INC in BFSI
      → Output: csv/bfsi_hot_leads_[YYYYMMDD].csv
      → These are mandatory renewals + already dissatisfied = highest conversion

- [ ] Seasonal issuance pattern analysis
      → Which months have highest new instrument issuances? (from Rating Date)
      → Both files combined
      → Output: csv/seasonal_pattern_[YYYYMMDD].csv
      → Key question: Are we at peak season now (June)?

- [ ] BSE SME company fetch — MANUAL UPLOAD NEEDED
      → Blocked by firewall (403) — automated fetch not possible
      → Action needed: Team to manually download from BSE website and upload to data/ folder
      → Once uploaded: cross-match script ready to run

- [ ] Infrastructure sector deep-dive
      → 1,246 leads in master list but sector brief was Session 1 (basic)
      → Refresh with INC breakdown, agency breakdown, urgency
      → Output: sector_Infrastructure_refresh_[YYYYMMDD].md

---

## P2 — Next Sessions

- [ ] Fetch NSE Emerge listed companies
      → URL: https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv
      → BLOCKED by firewall — needs manual download
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

- [ ] Master company database
      → Unified deduped list across both files
      → Output: csv/master_company_database_[YYYYMMDD].csv
      → Columns: Company | All Raters | All Instruments | Sectors | State | Urgency Score

- [ ] Construction sector brief
      → 439 leads in master list — major sector not yet briefed
      → Output: sector_Construction_[YYYYMMDD].md

- [ ] Healthcare sector brief
      → 194 leads — hospitals, diagnostics, pharma services
      → Output: sector_Healthcare_[YYYYMMDD].md

---

## P3 — Exploratory

- [ ] ACER whitespace map
      → Region x Sector gap table
      → Output: region_whitespace_map_[YYYYMMDD].md

- [ ] Instrument family grouping
      → Short Term / Long Term / Structured Finance buckets
      → Which instrument family has most INC exposure?

- [ ] Brickwork deep-dive
      → 1,527 Brickwork INC companies — largest SME-focused INC pool
      → Most switchable to ACER (Brickwork is direct competitor)
      → Output: csv/brickwork_INC_full_[YYYYMMDD].csv

- [ ] Agency concentration per sector
      → Which sectors are most dependent on a single agency?
      → Single-agency sectors = lowest switching friction for ACER

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
- [x] INC cross-match — 160 doubly-abandoned companies — 2026-06-12 (Session 3)
- [x] Sector × INC breakdown — all 12 sectors — 2026-06-12 (Session 3)
- [x] BFSI sector brief — 475 companies, 115 HIGH urgency, 69 INC — 2026-06-12 (Session 3)
- [x] Chemicals/Pharma sector brief — 889 companies, 142 HIGH urgency, 384 INC — 2026-06-12 (Session 3)
- [x] BSE SME fetch attempted — BLOCKED (403 Forbidden) — 2026-06-12 (Session 3)
