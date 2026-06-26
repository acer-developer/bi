# ACER Intelligence — Master Task List
Last Updated: 2026-06-26
Status: Session 30 complete. Session 31 starting next run.

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

- [x] "Dead company" audit — COMPLETE 2026-06-20 (Session 19)
      → 1,647 ULTRA HOT screened (D365 + Infomerics combined)
      → MCA API still blocked (403); proxy signals used instead
      → 0 name-flagged defunct companies; 62 medium-risk; 1,463 clean to call
      → Output: csv/ultra_hot_dead_risk_audit_20260620.csv (1,647 rows)

- [x] CRISIL × BRICKWORK dual-INC overlap — COMPLETE 2026-06-20 (Session 19)
      → 281 companies with INC at BOTH CRISIL AND BRICKWORK simultaneously
      → 6 ULTRA HOT + 57 HOT + 188 WARM; top: Jaidayal Hitex (410 days CRISIL + 365 days BW)
      → Output: csv/crisil_bw_dual_inc_20260620.csv (281 rows)

- [x] Recent INC transitions (downgraded TO INC in last 6 months) — COMPLETE 2026-06-20 (Session 19)
      → 95 confirmed transitions (had prior non-INC history); 43 JUST NOW (0-90 days)
      → CRISIL responsible for 61% of 2026 transitions — aggressive reclassification pattern
      → Output: csv/recent_inc_transitions_20260620.csv (95 rows) + fresh subset (43 rows)

- [x] Multi-signal super-target scoring — NEW — COMPLETE 2026-06-20 (Session 19)
      → 5 signals stacked; 81 TIER 1 MAXIMUM PRIORITY (score ≥ 5); 1,288 TIER 2
      → Top company: Arya Steels Rolling — score 7 (4 signals simultaneously)
      → Output: csv/super_targets_tier1_2_20260620.csv (1,369 rows) + csv/master_inc_scored_20260620.csv

---

## P1 — Do This Session (Session 20)

- [x] CARE × CRISIL dual-INC overlap — COMPLETE 2026-06-21 (Session 20)
      → 270 companies INC at BOTH CARE and CRISIL simultaneously
      → 7 ULTRA HOT + 228 HOT + 35 WARM; top: Shree Sita Pulses (411+376 days)
      → Output: csv/care_crisil_dual_inc_20260621.csv (270 rows)

- [x] INC trend analysis (2025 vs 2026) — COMPLETE 2026-06-21 (Session 20)
      → INC is STRUCTURAL (not cyclical): avg 1,500/month for 12 months
      → CRISIL dominates 35-45% every month; BRICKWORK declining; CARE+ACUITE accelerating
      → July 2026 expected peak (aligns with March fiscal year + 4-month rating cycle)
      → Output: csv/inc_trend_monthly_by_agency_20260621.csv + inc_trend_new_companies_monthly_20260621.csv

- [x] Sector breakdown of 81 TIER 1 super-targets — COMPLETE 2026-06-21 (Session 20)
      → Steel & Metals leads: 19 TIER 1 companies (23.5%); Agro Food 11; Construction 10
      → IT & Technology has highest avg score (6.0)
      → Enhanced sector engine: 99% classification rate (18 sector categories)
      → Output: csv/super_targets_by_sector_20260621.csv + tier1_sector_summary_20260621.csv

---

## P1 — Do This Session (Session 21)

- [x] Three-way INC overlap (CRISIL + CARE + BRICKWORK simultaneously) — COMPLETE 2026-06-21 (Session 21)
      → 32 companies INC at ALL THREE agencies simultaneously
      → 11 ULTRA HOT + 21 HOT — all callable; Steel sector dominates (5 of 11 ULTRA HOT)
      → Top: Alamelu Balaji Spg. Mills (408 days CARE, 299 CRISIL, 81 BW)
      → Output: csv/three_way_inc_crisil_care_bw_20260621.csv (32) + csv/three_way_inc_ultra_hot_20260621.csv (11)

- [x] IND-RA × CRISIL dual-INC for NCD instrument — COMPLETE 2026-06-21 (Session 21)
      → IND-RA NCD INC rate: 49.4% (674/1,363 records); 663 unique companies
      → 109 dual-INC (IND-RA NCD + CRISIL any): 13 ULTRA HOT + 84 HOT; 85/109 HIGH revenue
      → 554 exclusive IND-RA NCD INC (no CRISIL) — 303 HOT
      → Output: csv/indra_crisil_dual_inc_ncd_20260621.csv (109) + csv/indra_ncd_inc_exclusive_20260621.csv (554)

- [x] CARE 2026 acceleration — geographic breakdown — COMPLETE 2026-06-21 (Session 21)
      → 641 unique companies INC'd by CARE in 2026; April peak: 233 companies (73% above baseline)
      → Geo classification 7.8% (name-only): Gujarat 17, UP 10, Tamil Nadu 7 — MCA CIN needed for full geo
      → April 2026 instrument mix: Term Loans 40%, BG 25%, NCD 16%
      → Output: csv/care_2026_acceleration_geo_20260621.csv (641) + csv/care_april2026_peak_companies_20260621.csv (233)

---

## P1 — Do This Session (Session 22)

- [x] Instrument INC trend over time — COMPLETE 2026-06-22 (Session 22)
      → NCD is MOST RESILIENT: -1.1% decline vs Term Loans -22.9%, BG -18.3%
      → LC highest absolute INC rate (50.6%), BG (48.6%), NCD lowest (21.3%) but stable
      → NCD is proportionally growing share of INC pool — highest revenue per deal
      → Output: csv/instrument_inc_trend_20260622.csv (90 rows) + csv/instrument_inc_overall_20260622.csv (7 rows)

- [x] Infomerics INC acceleration check — COMPLETE 2026-06-22 (Session 22)
      → YES — Infomerics IS accelerating: 17.4% (Jan 2025) → 32.8% (Feb 2026) — doubled in 14 months
      → 749 ULTRA HOT + 426 HOT = 1,175 Infomerics companies callable now
      → D365 has ZERO Infomerics records — infomerics.json.xlsx is sole source
      → Output: csv/infomerics_inc_trend_20260622.csv (89 rows) + csv/infomerics_inc_leads_20260622.csv (1,928 rows)

- [x] Three-way INC companies with NCD instruments — COMPLETE 2026-06-22 (Session 22)
      → 7 of 32 three-way INC companies also have NCD instruments (all from CARE)
      → Top target: New Modern Technomech Pvt. Ltd. — ₹45 Cr NCD + triple INC
      → 2 ULTRA HOT + 5 HOT; total NCD instrument value ~₹102 Cr
      → Output: csv/three_way_plus_ncd_20260622.csv (7 rows)

---

## P1 — Do This Session (Session 23)

- [x] ACUITE 2026 acceleration geographic breakdown — COMPLETE 2026-06-22 (Session 23)
      → April 2026 peak: 128 companies (57.4% INC rate) — mirrors CARE April spike
      → INC rate rose from 37.2% (May 2025) to 57.4% (Apr 2026) — structural acceleration
      → 348 callable now (83 ULTRA HOT + 265 HOT); geo 97% unknown (MCA CIN needed)
      → Output: csv/acuite_2026_acceleration_geo_20260622.csv (1,926 rows) + acuite_monthly_inc_trend_20260622.csv

- [x] Feb 2026 CARE cohort targeting — COMPLETE 2026-06-22 (Session 23)
      → 183 unique companies, 317 records; all LOW urgency (115–140 days) but MAXIMUM RECEPTIVITY
      → 85% in High Risk or Default grade; top: Term Loans (122), BG (68), NCD (39)
      → Note: "HOT window" assumption incorrect — these are 4–5 months post-INC, not 6+ months
      → Output: csv/care_feb2026_cohort_20260622.csv (317 rows)

- [x] Infomerics ULTRA HOT × D365 multi-agency cross-match — COMPLETE 2026-06-22 (Session 23)
      → 102 of 367 Infomerics ULTRA HOT in D365 (27.8%): 77 exact + 25 fuzzy matches
      → 72 companies ALSO INC at D365 agencies — completely non-functional ratings everywhere
      → D365 overlap: CRISIL 110, CARE 75, ACUITE 51, BRICKWORK 49 records
      → Output: csv/infomerics_ultrahot_multiagency_20260622.csv (757) + csv/infomerics_ultrahot_d365_matched_20260622.csv (232)

---

## P1 — Do This Session (Session 24)

- [x] IND-RA 2026 acceleration check — COMPLETE 2026-06-23 (Session 24)
      → IND-RA shows DUAL-WAVE pattern: Jan 2026 (47.6% INC) + April 2026 (38.8% INC)
      → NCD INC rate extreme: 75.2% Aug 2025, 71.7% Jan 2026, 64.6% Apr 2026
      → Callable: 41 ULTRA HOT + 951 HOT + 248 MEDIUM = 1,412 unique INC companies
      → Output: csv/indra_2026_acceleration_20260623.csv + 3 trend CSVs

- [x] April 2026 cross-agency simultaneous INC spike analysis — COMPLETE 2026-06-23 (Session 24)
      → 984 unique companies INC in April 2026 — largest single-month event in dataset
      → 18 companies INC at 2 agencies simultaneously; no 3-way found
      → All 18 in LOW urgency (60–83 days) but maximum receptivity — July call deadline
      → Output: csv/april2026_all_inc_20260623.csv (984) + csv/april2026_cross_agency_inc_20260623.csv (18)

- [x] Steel sector master consolidation — COMPLETE 2026-06-23 (Session 24)
      → 1,040 companies (802 D365 + 238 Infomerics-only); 527 INC; 280 ULTRA HOT + 510 HOT
      → CRISIL 204 INC + BRICKWORK 120 + CARE 119; 36 multi-agency; 7 dual-INC
      → Output: csv/steel_sector_master_20260623.csv (1,040) + INC/ULTRA HOT/crossmatch subsets

---

## P1 — Do This Session (Session 25)

- [x] ICRA 2026 trend check — COMPLETE 2026-06-23 (Session 25)
      → ICRA did NOT spike in April 2026 — only agency without acceleration
      → Stable 24-34% INC rate throughout 2025-2026; 139 ULTRA HOT + 484 HOT callable
      → Output: csv/icra_2026_acceleration_20260623.csv (914 rows) + trend + comparison CSVs + brief

- [x] April 2026 dual-INC companies — deep sector profiles — COMPLETE 2026-06-23 (Session 25)
      → 18 companies profiled: Agro/Food 4, Chemicals 3, Infra 2, Steel 2, Energy 2
      → CARE in 13/18 cases; KBK Biotech (₹277 Cr) + Veda Biofuel (₹154 Cr) largest
      → Output: csv/april2026_dual_inc_profiles_20260623.csv (18 rows)

- [x] Final July 2026 calling master — COMPLETE 2026-06-23 (Session 25)
      → 6,866 unique companies: 1,612 ULTRA HOT + 5,242 HOT + 12 July-priority
      → 78 TIER 1 | 32 three-way INC | 18 April dual-INC | 1,363 multi-agency INC
      → Output: csv/july2026_calling_master_20260623.csv (6,866 rows — FINAL ACTION FILE)

---

## P1 — Do This Session (Session 26)

- [x] NCD-focused calling list — COMPLETE 2026-06-24 (Session 26)
      → 1,470 NCD INC companies (1,454 D365 + 16 Infomerics); "Non-government debt" = NCD in D365
      → IND-RA 652 (44%), CARE 441, ICRA 278, BW 80 — IND-RA is primary NCD displacement target
      → ULTRA HOT: 134 | HOT: 789 | 923 callable now — SEBI CRA license required before pitching
      → Output: csv/ncd_priority_calling_list_20260624.csv (1,470) + ncd_hot_only_20260624.csv (923)

- [x] Brickwork 2026 trend check — COMPLETE 2026-06-24 (Session 26)
      → H1 2025: 95.8% → H2 2025: 79.3% → H1 2026: 79.6% — DECLINED then STABILIZED
      → BW is NOT recovering INC companies — Phase 1 window CONFIRMED OPTIMAL NOW
      → 1,950 BW INC companies: 418 ULTRA HOT + 916 HOT = 1,334 callable immediately
      → Output: csv/brickwork_2026_trend_20260624.csv + brickwork_inc_leads_20260624.csv (1,950)

- [x] 78 TIER 1 super-targets — senior RM assignment brief — COMPLETE 2026-06-24 (Session 26)
      → 77 ULTRA HOT + 1 HOT; 24 three-way INC + 52 dual-INC + 2 four-way INC
      → Top: Arya Steels (390 days, 3-way) | J B Rolling Mills ₹463.7 Cr (385 days, 3-way) | New Modern Technomech ₹271.8 Cr (4-way)
      → Pitch scripts + call cadence embedded (Week of Jun 30: first call; Jul 7: follow-up)
      → Output: csv/tier1_senior_rm_assignments_20260624.csv (78 rows)

---

## P1 — Do This Session (Session 27)

- [x] CARE NCD INC deep-dive — COMPLETE 2026-06-24 (Session 27)
      → 454 unique companies (15.1% INC rate) — LOWER than IND-RA 44%; more selective
      → 71 ULTRA HOT + 115 HOT = 186 callable now; ₹56,923 Cr total identified amount
      → Energy sector: 14/32 companies ULTRA HOT — highest concentration; Lanco Babandh ₹750 Cr
      → April 2026 spike: 49 companies → October 2026 second calling window
      → Output: csv/care_ncd_inc_deepdive_20260624.csv (553) + hot_only (219) + sector summary (17)

- [x] BW stabilization root cause — COMPLETE 2026-06-24 (Session 27)
      → ROOT CAUSE: STRUCTURAL INC BACKLOG — active volume GROWING (+305% H1 2025→H1 2026)
      → BW issuing ~70 new active ratings/month AND ~276 new INC/month simultaneously
      → INC pool self-replenishes at ~2,000+ new INC companies/year — ACER pipeline permanent
      → Phase 1 displacement window CONFIRMED PERMANENT — BW not clearing INC
      → Output: csv/brickwork_volume_vs_inc_20260624.csv (12 monthly rows)

- [x] 4-way INC investigation — COMPLETE 2026-06-24 (Session 27)
      → CORRECTION: 8 companies (not 2) INC at 4 agencies simultaneously
      → Pattern: multi-lender structure → cascade INC across all agencies (not sequential failures)
      → Best target: Siddapur Distilleries (₹108 Cr) — was ACTIVE at CARE Jan 2026, most solvable
      → Ashok Bricks rated "D" at all 4 — likely actual default; skip for now
      → Output: csv/four_way_inc_profiles_20260624.csv (58 rows)

---

## P1 — Do This Session (Session 28)

- [x] October 2026 Calling Calendar — COMPLETE 2026-06-25 (Session 28)
      → 4,151 unique companies escalating Oct–Nov 2026 (4x the July blitz volume)
      → 3,478 HOT/ULTRA HOT escalations; April 2026 cohort (984 cos) enters MEDIUM Oct–Nov
      → CRISIL 1,479 | CARE 834 | BW 639 | ACUITE 421 | ICRA 383 | IND-RA 373 | Infomerics 290
      → Output: csv/october2026_calling_calendar_20260625.csv (7,837) + hot_ultraHOT (6,467) + april cohort (1,647)

- [x] Energy NCD consolidated calling list — COMPLETE 2026-06-25 (Session 28)
      → 63 unique companies, 78 records (CARE 32, IND-RA 21, ICRA 10, BW 1); 27 callable now
      → Total identified NCD amount: ₹13,286 Cr (avg ₹172.6 Cr — highest ticket in dataset)
      → Top: Senvion Wind ₹3,000 Cr (Oct window), Jsw Mahanadi ₹773 Cr (ULTRA HOT), Lanco Babandh ₹750 Cr
      → Output: csv/energy_ncd_inc_all_agencies_20260625.csv (78) + energy_ncd_hot_only (33)

- [x] ICRA NCD vs CARE NCD comparison — COMPLETE 2026-06-25 (Session 28)
      → CARE wins all metrics: 454 cos (vs ICRA 282), ₹56,923 Cr (vs ₹24,330 Cr), callable 186 (vs 123)
      → CARE avg ₹104.8 Cr vs ICRA ₹70.9 Cr per record; ICRA concentrated in IL&FS group (NCLT risk)
      → Combined pipeline: ₹15.5 Cr at ₹5L avg fee; CARE first priority
      → Output: csv/icra_vs_care_ncd_comparison_20260625.csv (40) + full lists (349 ICRA, 553 CARE)

---

## P1 — Do This Session (Session 29)

- [x] October calling calendar — filter "D" grade companies — COMPLETE 2026-06-25 (Session 29)
      → 1,876 records / 1,007 companies removed as actual defaults (24.3% removal rate)
      → Clean callable: 5,961 rows, 3,179 unique companies (from 4,151 raw)
      → CRISIL 2,255 | CARE 997 | BW 822 | ACUITE 688 | ICRA 463 | IND-RA 289
      → Output: csv/october2026_clean_callable_20260625.csv (5,961 rows) + removed_defaults (1,876)

- [x] BRICKWORK October escalation deep-dive — COMPLETE 2026-06-25 (Session 29)
      → 639 raw → 168 defaults removed (26.3%) → 471 clean unique, 822 records
      → 366 ULTRA HOT + 379 HOT escalations (90.6% in highest urgency)
      → Top target: Akbar Travels India ₹812.5 Cr escalating ULTRA HOT by Oct 7
      → Output: csv/brickwork_october2026_targets_20260625.csv (822 rows)

- [x] ACUITE NCD INC standalone profile — COMPLETE 2026-06-25 (Session 29)
      → FINDING: ACUITE has ZERO NCD INC companies (0.0% INC rate on NCD)
      → ACUITE NCD book = only 61 records, 19 companies — none INC
      → ACUITE is bank-instrument only (TL/BG/LC); NCD pitch inapplicable
      → NCD INC ranking confirmed: IND-RA 663 > CARE 454 > ICRA 282 > BW 82 > ACUITE 0
      → Output: csv/acuite_ncd_inc_profile_20260625.csv (0 rows — confirmed no data) + ncd_all_agencies_comparison

---

## P1 — Do This Session (Session 30)

- [x] IND-RA NCD INC standalone deep-dive — COMPLETE 2026-06-26 (Session 30)
      → 663 unique companies | 53.5% NCD INC rate (highest of any agency-instrument pair)
      → 373 callable now (4 ULTRA HOT + 369 HOT) | ₹40,918 Cr total
      → Top sector: Construction (93 cos, ₹7,569 Cr); Top target: P E C Ltd. (₹3,432 Cr)
      → Output: csv/indra_ncd_inc_standalone_20260626.csv (674 rows) + sector summary

- [x] CRISIL October escalation deep-dive — COMPLETE 2026-06-26 (Session 30)
      → 2,255 records | 1,220 unique companies | 953 ULTRA HOT + 879 HOT + 423 MEDIUM escalations
      → Construction leads (124 companies, ₹8,428 Cr); Automobiles anomaly (94 cos, 87 UH)
      → Top target: C S Construction Co. (₹978 Cr, ULTRA HOT); all bank instruments (no NCD)
      → Output: csv/crisil_october2026_targets_20260626.csv (2,255) + UH subset (953) + sector summary

- [x] October 2026 clean callable — sector breakdown — COMPLETE 2026-06-26 (Session 30)
      → 5,961 records | 3,179 unique | 21 sectors | 68.4% classification rate
      → Construction #1 (344 cos, ₹53,422 Cr, score 54.1); Energy highest ticket (₹120 Cr avg)
      → 4,914 rows / 2,665 companies in HOT+ULTRA HOT escalation
      → Output: csv/october2026_clean_sector_breakdown_20260626.csv + agency-sector matrix + enriched full file

---

## P1 — Do This Session (Session 31)

- [ ] CARE October escalation deep-dive — NEW P1
      → CARE has 997 clean October records (2nd largest pool after CRISIL)
      → Build sector breakdown, urgency profile, top targets list
      → Output: csv/care_october2026_targets_20260626.csv

- [ ] ACUITE + BRICKWORK combined October brief — NEW P1
      → ACUITE 688 + BW 822 = 1,510 records combined (MSME-focus agencies)
      → BW: 90.6% HOT+UH (confirmed highest rate); ACUITE: lower rate
      → Build combined MSME calling brief with sector and urgency breakdown
      → Output: csv/msme_agencies_october2026_20260626.csv

- [ ] October 2026 week-by-week call schedule — NEW P1
      → 5,961 companies escalating Oct–Nov 2026 — when exactly does each escalate?
      → Build week-level calendar: Week 1 Oct (Oct 1-7), Week 2 (Oct 8-14), etc.
      → Enables daily/weekly call planning for sales team
      → Output: csv/october2026_weekly_calendar_20260626.csv

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
- [x] CRISIL × BRICKWORK Dual-INC Overlap — 281 companies, 6 ULTRA HOT, doubly-abandoned — 2026-06-20 (Session 19)
- [x] Recent INC Transitions — 95 confirmed transitions; 43 JUST NOW (0-90 days); CRISIL 61% — 2026-06-20 (Session 19)
- [x] Dead Company Risk Audit — 1,647 ULTRA HOT screened; 1,463 clean to call (88.8%) — 2026-06-20 (Session 19)
- [x] Multi-Signal Super-Target Scoring — 81 TIER 1 + 1,288 TIER 2; top score 7 — 2026-06-20 (Session 19)
- [x] Recent Downgrades (90 days) — 523 companies; 456 also INC; CRISIL 194 — 2026-06-20 (Session 19)
- [x] CARE × CRISIL Dual-INC Overlap — 270 companies, 7 ULTRA HOT — 2026-06-21 (Session 20)
- [x] INC Trend Analysis — structural 1,500/month; CARE accelerating; BRICKWORK declining — 2026-06-21 (Session 20)
- [x] Sector Breakdown of 81 TIER 1 — Steel 19, Agro 11, Construction 10; IT highest score (6.0) — 2026-06-21 (Session 20)
- [x] Three-Way INC Overlap (CRISIL+CARE+BW) — 32 companies, 11 ULTRA HOT; Steel dominates — 2026-06-21 (Session 21)
- [x] IND-RA × CRISIL NCD Dual-INC — 109 dual + 554 exclusive; 49.4% NCD INC rate — 2026-06-21 (Session 21)
- [x] CARE 2026 Geo Breakdown — 641 companies, April peak 233; Gujarat/UP/Tamil Nadu clusters — 2026-06-21 (Session 21)
- [x] Instrument INC Trend — NCD most resilient (-1.1%), LC highest rate (50.6%), BG -18.3%, TL -22.9% — 2026-06-22 (Session 22)
- [x] Infomerics INC Acceleration — confirmed: 17.4% → 32.8% in 14 months; 749 ULTRA HOT + 426 HOT — 2026-06-22 (Session 22)
- [x] Three-Way INC + NCD Cross-Reference — 7 companies; New Modern Technomech top target (₹45 Cr NCD) — 2026-06-22 (Session 22)
- [x] ACUITE 2026 Acceleration + Geo Breakdown — April 2026 peak 128 companies (57.4%), mirrors CARE; 348 callable — 2026-06-22 (Session 23)
- [x] Feb 2026 CARE Cohort — 183 companies, 85% High Risk/Default, peak receptivity window — 2026-06-22 (Session 23)
- [x] Infomerics ULTRA HOT × D365 Cross-Match — 102/367 in D365 (27.8%); 72 also INC at D365 — 2026-06-22 (Session 23)
- [x] IND-RA 2026 Acceleration — dual-wave Jan+Apr; NCD 75% INC peak; 41 UH + 951 HOT callable — 2026-06-23 (Session 24)
- [x] April 2026 Cross-Agency INC Spike — 984 companies, 18 dual-agency; July 2026 deadline — 2026-06-23 (Session 24)
- [x] Steel Sector Master — 1,040 companies, 527 INC, 280 ULTRA HOT + 510 HOT — 2026-06-23 (Session 24)
