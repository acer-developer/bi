# ACER Intelligence — Master Task List
Last Updated: 2026-06-18
Status: Session 15 complete. Session 16 starting next run.

---

## P1 — Do This Session (Tonight)

- [ ] BSE SME company fetch — MANUAL UPLOAD NEEDED (15th attempt note)
      → Blocked by firewall (403) — automated fetch not possible
      → Action needed: Team to manually download from BSE website and upload to data/ folder
      → Once uploaded: cross-match script ready to run

- [ ] MCA CIN NIC code enrichment — PROMOTE TO P1
      → 724 unclassified BRICKWORK INC companies + 8,356 total "Other" companies
      → CIN NIC code (positions 5-10 in CIN) encodes industry activity
      → Estimated unlock: ~3,000–4,000 more companies classified
      → First step: extract CIN from any available source or manual upload
      → Highest-value single unlock remaining in the database

- [ ] ICRA Non-fund-based anomaly investigation — PROMOTE TO P1
      → ICRA NFF INC rate: 44.4% vs CRISIL 9.2% for same instrument
      → Investigate: is ICRA's "non-fund-based" categorization different?
      → This could be a categorization artifact or a real structural issue

---

## P2 — Next Sessions

- [ ] Energy sector brief
      → 36 BRICKWORK INC energy companies identified in master file (session_20260618)
      → Full energy sector likely larger — expand keywords: solar, wind, biogas, biofuel, EPC
      → Output: leads_Energy_[YYYYMMDD].csv + sector_Energy_[YYYYMMDD].md

- [ ] Infomerics steel cross-match
      → ~257 Infomerics-only steel companies not yet cross-matched with D365
      → Could add to the 917-company steel sector list
      → Method: fuzzy name matching (difflib or rapidfuzz)

- [ ] ACER July Outreach Dashboard
      → Compile all 18-sector ULTRA HOT + HOT into one executive CSV
      → Include: sector, agency, instrument, urgency, pitch angle
      → Format: ready-to-load into CRM or share with sales head as single file

- [ ] Agency × Instrument targeting CSV (action version of matrix)
      → Matrix built in session_20260618 — BRICKWORK master file supersedes this
      → Still useful for ACUITE targeting (LC 52.2%, Fund-based 50%) — second-priority displacement
      → Output: csv/acuite_displacement_by_instrument_[YYYYMMDD].csv

- [ ] Fetch NSE Emerge listed companies
      → BLOCKED by firewall — needs manual download
      → Save raw: csv/raw/nse_equity_raw_[YYYYMMDD].csv
      → Cross match with ratings data

- [ ] Enrich company list with director/CEO/CFO names
      → Source: https://www.zaubacorp.com
      → Source: https://www.mca.gov.in
      → Add to existing CSV: Director Name | Designation | Email if available
      → Output: csv/leads_enriched_[YYYYMMDD].csv

- [ ] Regional Territory Maps
      → Currently BLOCKED — no State column in either file
      → Unblock by: MCA CIN state-code enrichment
      → Once unblocked: region_North.md / region_South.md / region_West.md / region_East.md

---

## P3 — Exploratory

- [ ] Bank Guarantee product verification
      → Check if ACER has BG rating capability (3,593 INC BG companies depend on this)
      → If yes: immediate unlock of contractor segment
      → Note for team: confirm with ACER product team before next blitz call

- [ ] Media/Retail sector brief
      → ~76 companies identified in Session 11 reclassification
      → Lead file not yet produced
      → Output: leads_Media_Retail_[YYYYMMDD].csv + sector_Media_Retail_[YYYYMMDD].md

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
- [x] Hotels/Tourism sector blitz — expanded to 247 companies (from 84), 38.1% INC, 85% single-agency, 7 ultra-hot — 2026-06-16 (Session 11)
- [x] IT/Software deep-dive — expanded to 812 companies (from 265), 42.5% INC, 70 HIGH urgency, 30 ultra-hot — 2026-06-16 (Session 11)
- [x] "Other" bucket reclassification — 14,166 companies analyzed, 5,810 reclassified (41%), 7 new sectors discovered — 2026-06-16 (Session 11)
- [x] Automobiles/Auto NEW sector — 309 companies, 67.6% INC, CRISIL-dominant, lead file produced — 2026-06-16 (Session 11)
- [x] Paper/Packaging NEW sector — 64 companies, 76.6% INC (highest sector rate), lead file produced — 2026-06-16 (Session 11)
- [x] Mining/Minerals NEW sector — 183 companies, 54.6% INC, lead file produced — 2026-06-16 (Session 11)
- [x] Automobiles/Auto sector brief — 309 companies, 17 ultra-hot, CRISIL 57%, Brickwork displacement — 2026-06-17 (Session 12)
- [x] Chemicals/Pharma FULL sector brief — 763 companies (+449% vs Session 3), 40 ultra-hot, 4 pitch scripts — 2026-06-17 (Session 12)
- [x] Jewellery/Gems sector brief — 183 companies, 43.2% INC, 86.3% single-agency, Surat/Jaipur/Mumbai clusters — 2026-06-17 (Session 12)
- [x] Logistics lead file produced — 275 companies (139 orig + 136 reclassified), 40.7% INC — 2026-06-17 (Session 12)
- [x] Trading/Exports lead file produced — 198 companies, 64.1% INC — 2026-06-17 (Session 12)
- [x] July 2026 Mega Blitz Master — 1,602 HIGH urgency companies, 451 Ultra Hot, 1,151 Hot, 18 sectors — 2026-06-17 (Session 13)
- [x] Logistics sector brief — 275 companies, 94.1% Brickwork INC, 12 ultra-hot, Whitespace Score 20/25 — 2026-06-17 (Session 13)
- [x] Trading/Exports sector brief — 198 companies, 64.1% INC, 13 ULTRA HOT, BRICKWORK 90% INC, August export window — 2026-06-18 (Session 14)
- [x] Paper/Packaging pitch pack — 64 companies, 76.6% INC (HIGHEST of 18 sectors), LC INC 95%, BRICKWORK 94.7% — 2026-06-18 (Session 14)
- [x] Agency × Instrument INC matrix — 10 instruments × 6 agencies; BRICKWORK BG 86.5%, LC 87.9%, confirmed systemic — 2026-06-18 (Session 14)
- [x] Steel/Metals sector refresh — 917 companies (5.7x vs Session 2), 58.8% INC, 48 ULTRA HOT, BRICKWORK 96.8% — 2026-06-18 (Session 14)
- [x] BRICKWORK Master Displacement File — 1,885 unique companies, 223 ULTRA HOT, 293 HOT, all 18 sectors — 2026-06-18 (Session 15)
- [x] Mining/Minerals sector brief — 602 companies (3.3x expanded), 44.5% INC, 21 ULTRA HOT, BRICKWORK 94.3% — 2026-06-18 (Session 15)
- [x] Media/Retail sector brief — 272 D365 + 100 Infomerics, 50.7% INC, 11 ULTRA HOT, non-core sector — 2026-06-18 (Session 15)
