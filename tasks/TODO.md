# ACER Intelligence — Master Task List
Last Updated: 2026-06-16
Status: Session 10 complete. Session 11 starting next run.

---

## P1 — Do This Session (Tonight)

- [ ] Hotels/Tourism sector blitz — PROMOTE TO P1
      → 84 companies, 90.5% single-agency (HIGHEST of any sector) — easiest penetration
      → 38.1% INC rate + 11.9% HIGH urgency — moderate but concentrated
      → Geographic hypothesis: Maharashtra, Goa, Rajasthan, Delhi — one regional push
      → Output: sector_Hotels_Tourism_[YYYYMMDD].md
      → Output: csv/leads_Hotels_Tourism_[YYYYMMDD].csv

- [ ] IT/Software sector deep-dive — PROMOTE TO P1
      → 265 companies, 44.2% INC rate — significant opportunity
      → Likely clustered in Bangalore/Hyderabad/Pune — regional angle possible
      → Output: sector_IT_Software_[YYYYMMDD].md
      → Output: csv/leads_IT_Software_[YYYYMMDD].csv

- [ ] "Other" bucket sub-classification attempt — PROMOTE TO P1
      → 14,166 companies in "Other" sector = 67.7% of master DB
      → Attempt keyword classification to uncover hidden sectors
      → Even 20% reclassification = 2,800 companies newly organized
      → Output: csv/other_reclassified_[YYYYMMDD].csv
      → Output: other_sector_breakdown_[YYYYMMDD].md

- [ ] BSE SME company fetch — MANUAL UPLOAD NEEDED (9th attempt note)
      → Blocked by firewall (403) — automated fetch not possible
      → Action needed: Team to manually download from BSE website and upload to data/ folder
      → Once uploaded: cross-match script ready to run

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

- [ ] MCA enrichment pilot
      → Test CIN-based state mapping on 50 companies manually via mca.gov.in
      → CIN state codes: MH=Maharashtra, GJ=Gujarat, DL=Delhi, TN=Tamil Nadu etc.
      → If feasible: unlock regional mapping for full 3,230 blitz list

- [ ] Agency × Instrument Family matrix
      → Which agency has highest BG/LC INC rate?
      → Brickwork suspected top for BG; CARE suspected for LC
      → Output: csv/agency_instrument_INC_matrix_[YYYYMMDD].csv

---

## P3 — Exploratory

- [ ] Bank Guarantee product verification
      → Check if ACER has BG rating capability (3,593 INC BG companies depend on this)
      → If yes: immediate unlock of contractor segment
      → Note for team: confirm with ACER product team before next blitz call

- [ ] Logistics sector brief
      → 139 companies, 40.3% INC — aligned with industrial corridors
      → Output: sector_Logistics_[YYYYMMDD].md

- [ ] Chemicals/Pharma sector refresh
      → 139 companies, 49.6% INC — significant but small sector
      → Was covered in Session 3 — refresh with current urgency scores
      → Output: sector_ChemicalsPharma_refresh_[YYYYMMDD].md

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
- [x] Manufacturing sector brief — 3,572 companies, 846 HIGH, 1,619 INC (45.3%) — 2026-06-14 (Session 6)
- [x] Infomerics vulnerability deep-dive — 996 INC companies, 23.9% overall INC rate — 2026-06-14 (Session 6)
- [x] July contact blitz list — 3,230 companies, Brickwork 572 + Infomerics 350 top targets — 2026-06-14 (Session 6)
- [x] Healthcare sector brief — 807 companies, 315 INC (39%), 106 HIGH urgency — 2026-06-14 (Session 7)
- [x] Brickwork deep-dive — 1,950 INC companies (89.7% INC rate), displacement playbook written — 2026-06-14 (Session 7)
- [x] Regional clustering of July blitz — 116/3,230 geolocated, June urgent cohort identified (1,018) — 2026-06-14 (Session 7)
- [x] Master company database — 20,918 unique companies, 9,461 INC (45.2%) — 2026-06-15 (Session 8)
- [x] June 2026 urgent "Call TODAY" list — 1,883 overdue companies, 984 INC — 2026-06-15 (Session 8)
- [x] ACER whitespace map — Sector scores + Region x Sector INC density — 2026-06-15 (Session 8)
- [x] Top targets CSV (INC + HIGH urgency) — 962 companies — 2026-06-15 (Session 8)
- [x] Multi-agency + HIGH urgency warmest leads — 83 companies — 2026-06-15 (Session 8)
- [x] Agro/Food sector deep-dive — 812 companies, 478 INC (58.9%), June Kharif pitch window — 2026-06-15 (Session 9)
- [x] Textiles sector deep-dive — 336 companies, 214 INC (63.7%), cluster playbook written — 2026-06-15 (Session 9)
- [x] Instrument family grouping — Short-term 40% INC, Long-term 35.4% INC; BG (48.6%) + LC (50.6%) are hottest instruments — 2026-06-15 (Session 9)
- [x] BFSI NBFC/MFI sub-segment playbook — 496 NBFC/MFI/HFC leads, 56 HIGH urgency, regulatory pitch scripts — 2026-06-16 (Session 10)
- [x] Education sector deep-dive — 70 companies, 31.4% HIGH urgency (highest sector), Infomerics leads sector — 2026-06-16 (Session 10)
- [x] Agency concentration by sector — 14 sectors scored, vulnerability index built, no monopoly found, 3-phase attack sequence — 2026-06-16 (Session 10)
