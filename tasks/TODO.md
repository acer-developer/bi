# ACER Intelligence — Master Task List
Last Updated: 2026-06-13
Status: Session 5 complete. Session 6 starting next run.

---

## P1 — Do This Session (Tonight)

- [ ] Manufacturing sector brief
      → 29 doubly-INC + likely 500+ more from full dataset — not yet briefed
      → Use both files; keyword match: 'manufactur', 'industries', 'engineering', 'mfg', etc.
      → Output: sector_Manufacturing_[YYYYMMDD].md + csv/leads_Manufacturing_[YYYYMMDD].csv

- [ ] Infomerics vulnerability deep-dive
      → Map ALL Infomerics INC clients: sector × size × instrument × urgency
      → INC rates: Infra 41.5%, Construction 23.1%, BFSI dominates ULTRA HOT
      → Output: csv/infomerics_full_vulnerability_[YYYYMMDD].csv + sector_Infomerics_vulnerability_[YYYYMMDD].md
      → Promoted from P2 — Infomerics is ACER's #1 acquisition target

- [ ] BSE SME company fetch — MANUAL UPLOAD NEEDED (4th attempt note)
      → Blocked by firewall (403) — automated fetch not possible
      → Action needed: Team to manually download from BSE website and upload to data/ folder
      → Once uploaded: cross-match script ready to run

- [ ] July contact blitz list — INC + renewal due July 2026
      → Subset of renewal pipeline: companies where INC = Y AND renewal month = July 2026
      → Filter by Infomerics + Brickwork (most switchable) first
      → Output: csv/july_blitz_INC_20260613.csv — prioritized outreach list for first week of July

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
- [x] Sub-sector breakdown of 160 doubly-INC companies — Infrastructure leads (24) — 2026-06-13 (Session 4)
- [x] BFSI hot list — 12 ULTRA HOT (overdue + INC), 186 total hot — 2026-06-13 (Session 4)
- [x] Seasonal issuance pattern — July peak (9.7%), June below-average (7.7%) — 2026-06-13 (Session 4)
- [x] Infrastructure sector deep-dive refresh — 1,246 leads, 305 HIGH, 124 INC — 2026-06-13 (Session 4)
- [x] Forward renewal calendar — 15,406 records, 7,144 unique companies, Jul–Sep 2026 — 2026-06-13 (Session 5)
- [x] Sector tagging of 84 Other/Unknown doubly-INC companies — all classified — 2026-06-13 (Session 5)
- [x] 12 BFSI ULTRA HOT deep profiles — overdue days, sizes, pitch scripts — 2026-06-13 (Session 5)
- [x] Construction sector brief — 1,289 companies, 624 HIGH, 1,231 INC (38%) — 2026-06-13 (Session 5)
