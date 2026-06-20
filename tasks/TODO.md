# ACER Intelligence — Master Task List
Last Updated: 2026-06-20
Status: Session 18 complete. Session 19 starting next run.

---

## P1 — Do This Session (Tonight)

- [ ] BSE SME company fetch — MANUAL UPLOAD NEEDED (17th session note)
      → Blocked by firewall (403) — automated fetch not possible
      → Action needed: Team to manually download from BSE website and upload to data/ folder
      → Once uploaded: cross-match script ready to run

- [ ] MCA CIN NIC code enrichment — PROMOTE TO P1
      → 724 unclassified BRICKWORK INC companies + 8,356 total "Other" companies
      → CIN NIC code (positions 5-10 in CIN) encodes industry activity
      → Estimated unlock: ~3,000–4,000 more companies classified
      → First step: extract CIN from any available source or manual upload
      → Highest-value single unlock remaining in the database

- [x] CRISIL INC Master — COMPLETE 2026-06-20 (Session 18)
      → 3,429 CRISIL INC companies (46.7% INC) — largest absolute INC pool
      → 488 ULTRA HOT + 1,931 HOT + 1,114 WARM; 412 doubly-abandoned (CRISIL+BW or ACUITE INC)
      → Most overdue: Jaidayal Hitex Pvt. Ltd. (410 days)
      → Output: csv/crisil_displacement_master_20260620.csv (6,785 rows) + brief

- [x] July 2026 daily calling calendar — COMPLETE 2026-06-20 (Session 18)
      → 1,131 companies hitting 12-month mark in July 2026 (2,018 records)
      → Peak day: July 18 = 216 companies; by agency: CRISIL 444, BW 204, IND-RA 185
      → Output: csv/july_daily_calendar_20260620.csv

- [x] SEBI license gap analysis — COMPLETE 2026-06-20 (Session 18)
      → Bank credit (no license): 7,994 INC companies | 1,563 ULTRA HOT
      → SEBI debt license unlock: 1,454 additional companies | IND-RA 663, CARE 454, ICRA 282
      → 136 ULTRA HOT in SEBI debt instruments — call on license day
      → Estimated revenue unlock: ₹72.7 Cr at ₹5L avg fee
      → Output: csv/sebi_gap_analysis_20260620.csv + leads_SEBI_debt_INC_20260620.csv + brief

- [x] ICRA Non-fund-based anomaly investigation — SOLVED 2026-06-19 (Session 16)
      → Root cause: Portfolio MIX EFFECT — ICRA rates smaller/riskier SMEs under NF
      → ICRA NF INC median ₹6.8 Cr vs CRISIL NF ₹38.4 Cr — different segments
      → 499 ICRA NF INC companies identified (59 ULTRA HOT, 258 HOT)
      → Output: leads_ICRA_NF_INC_20260619.csv + ICRA_NF_anomaly_20260619.md

---

- [x] Infomerics-only whitespace analysis — COMPLETE 2026-06-20 (Session 18) [was H2]
      → 4,170 of 4,175 Infomerics companies not in D365 — zero competitor overlap
      → 998 INC: 375 ULTRA HOT + 440 HOT + 183 WARM = 815 callable now
      → Output: csv/infomerics_only_whitespace_20260620.csv + brief

---

## P1 — Do This Session (Session 19)

- [ ] "Dead company" audit — PROMOTE TO P1
      → Cross-check 1,429 ULTRA HOT companies against MCA for dissolved/struck-off entities
      → Remove defunct companies from calling list before team mobilizes
      → Avoids wasted calls on non-existent companies

- [ ] CRISIL × BRICKWORK dual-INC overlap — NEW P1
      → Find companies with INC at BOTH CRISIL AND BRICKWORK simultaneously
      → These "super targets" have been abandoned by two agencies — highest probability of switching
      → Output: csv/crisil_bw_dual_inc_[YYYYMMDD].csv

- [ ] Recent INC transitions (downgraded TO INC in last 6 months) — NEW P1
      → Most recently frustrated companies — highest emotional urgency to switch
      → Filter d365 for companies that moved from standard rating to INC post Jan 2026
      → Output: csv/recent_inc_transitions_[YYYYMMDD].csv

---

## P2 — Next Sessions

- [x] Energy sector brief — COMPLETE 2026-06-19 (Session 16)
      → 1,501 D365 + 247 Infomerics = 1,748 total companies (sector 40x larger than estimated)
      → BRICKWORK energy INC rate: 73.2% — prime displacement target
      → 58 ULTRA HOT + 209 HOT across both sources
      → Output: leads_Energy_FULL_20260619.csv (1,642 rows) + sector_Energy_20260619.md

- [x] Infomerics steel cross-match — COMPLETE 2026-06-19 (Session 16)
      → 202 pure Infomerics-only steel companies (not in D365) identified
      → 27 ULTRA HOT, 15 HOT — exclusive leads vs competitors
      → 63 fuzzy-matched companies confirmed as same entity (variant naming)
      → Output: leads_Steel_Infomerics_only_20260619.csv + infomerics_steel_crossmatch_20260619.csv

- [x] ACER July Outreach Dashboard — COMPLETE 2026-06-19 (Session 16)
      → 2,191 unique companies across 20 sectors: 527 ULTRA HOT + 1,664 HOT
      → Top 5 sectors: Manufacturing (104), Construction (86), AgroFood (52), ChemPharma (40), Energy (58)
      → Output: july_outreach_dashboard_20260619.csv + july_ULTRA_HOT_only_20260619.csv

- [x] ACUITE Displacement Playbook — COMPLETE 2026-06-19 (Session 17)
      → 911 unique ACUITE INC companies (41.6% INC rate)
      → 89 ULTRA HOT + 454 HOT + 368 WARM
      → LC 52.2% INC, Fund-based 50.0%, Term loans 43.6%, BG 43.4%
      → Output: acuite_displacement_master_20260619.csv (1,926 rows) + acuite_displacement_brief_20260619.md

- [x] Agency × Instrument targeting CSV (action version of matrix)
      → Full 6-agency competitor vulnerability matrix built (Session 17)
      → Attack sequencing: Phase 1 BW+ACUITE, Phase 2 CRISIL+CARE, Phase 3 IND-RA+ICRA
      → Total pipeline: 10,338 INC companies | 1,429 ULTRA HOT | 5,489 HOT
      → Output: competitor_vulnerability_summary_20260619.csv + competitor_master_brief_20260619.md
      → ACUITE playbook complete; CARE and IND-RA masters also built in Session 17

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

- [x] Media/Retail sector brief — COMPLETE 2026-06-18 (Session 15)
      → 272 D365 + 100 Infomerics = 372 total, 50.7% INC, 11 ULTRA HOT
      → Output: leads_Media_Retail_20260618.csv + sector_Media_Retail_20260618.md

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
- [x] ICRA NF anomaly investigated + solved — mix effect confirmed, 499 leads identified — 2026-06-19 (Session 16)
- [x] Energy sector brief — 1,642 companies, 58 ULTRA HOT, BRICKWORK 73.2% INC — 2026-06-19 (Session 16)
- [x] Infomerics steel cross-match — 202 pure Infomerics-only companies, 27 ULTRA HOT — 2026-06-19 (Session 16)
- [x] ACER July Outreach Dashboard — 2,191 companies across 20 sectors, 527 ULTRA HOT — 2026-06-19 (Session 16)
- [x] ACUITE Displacement Playbook — 911 INC companies (41.6% INC), 89 ULTRA HOT + 454 HOT — 2026-06-19 (Session 17)
- [x] CARE Vulnerability Analysis — 1,722 INC companies (27.4% INC), 271 ULTRA HOT + 787 HOT — 2026-06-19 (Session 17)
- [x] IND-RA Displacement Master — 1,412 INC companies (33.0% INC), NCD 53.5% INC — 2026-06-19 (Session 17)
- [x] Full 6-Agency Competitor Vulnerability Matrix — 10,338 INC total, attack sequencing Phase 1/2/3 — 2026-06-19 (Session 17)
- [x] Regional City Cluster Analysis — 79 cities mapped via name inference, Anand (Gujarat) top priority — 2026-06-19 (Session 17)
- [x] CRISIL Displacement Master — 3,429 INC companies, 488 ULTRA HOT, 412 doubly-abandoned — 2026-06-20 (Session 18)
- [x] July 2026 Daily Calling Calendar — 1,131 companies, peak July 18 (216 companies) — 2026-06-20 (Session 18)
- [x] SEBI License Gap Analysis — 7,994 bank credit INC + 1,454 SEBI debt INC, ₹72.7 Cr unlock — 2026-06-20 (Session 18)
- [x] Infomerics-only Whitespace Analysis — 4,170 exclusive companies, 815 INC callable now — 2026-06-20 (Session 18)
