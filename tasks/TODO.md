# ACER Intelligence — Master Task List
Last Updated: 2026-06-11
Status: Session 1 — Initial analysis complete. Key outputs generated.

---

## P1 — Do This Session (Tonight)

- [x] Read and profile infomerics.json.xlsx
      → 8,438 rows | 4,175 companies | Dec 2016–Feb 2026
      → Nulls: Date(4), Current Ratings(14), Size(21) — minor
      → Instruments normalized: Long Term 57.8%, Short Term 31.9%, NCD 2.2%
      → NOTE: No State or Sector column found — gap vs expected schema

- [x] Read and profile d365_data.xlsx
      → 49,945 rows | 17,622 companies | May 2025–May 2026
      → Agencies: CRISIL 37%, CARE 22%, ICRA 13%, IND-RA 10%, ACUITÉ 9%, BRICKWORK 8%
      → NOTE: No State or Region column found — regional maps blocked

- [x] Check overlap between both files
      → Exact name matches: 4 companies only (name format differences)
      → True overlap likely higher — fuzzy match needed (Session 2 task)
      → Column names differ significantly — mapping documented in data_profile output

- [ ] Map all states to regions — BLOCKED
      → Neither file has State/Region column
      → Workaround: inferred sectors from company name keywords
      → Resolution: needs external data enrichment (GST/MCA lookup)

- [x] Build Instrument Recency Score on both files
      → Infomerics: HIGH 44.5% | MEDIUM 38.2% | LOW 17.3%
      → d365: MEDIUM 51.5% | LOW 39.4% | HIGH 9.2%
      → 82.7% of Infomerics instruments approaching or past renewal — ACT NOW

---

## P2 — Next Sessions

- [x] Competitor Concentration Analysis — DONE (Session 1)
      → 3,623 companies use 2+ agencies — highest opportunity tier
      → Top 18 companies use 4–5 agencies AND were recently downgraded
      → CRISIL 37% share dominant; CARE turnaround complaints = ACER entry point
      → Output: intelligence_outputs/competitor_concentration_20260611.md

- [x] First Sales Lead List — DONE (Session 1)
      → 50 leads from Infomerics (downgraded + negative outlook + overdue)
      → 25 leads from d365 (recently downgraded by CRISIL/CARE)
      → Output: intelligence_outputs/leads_ALL_20260611.md

- [x] Identify downgraded entities — DONE (Session 1)
      → 1,380 downgrades in Infomerics; 5,608 in d365
      → Top targets in lead list

- [ ] Sector Attractiveness Matrix — PARTIAL
      → Infrastructure sector brief done (Session 1)
      → Agro/Food, Steel & Metals, Textiles briefs pending (Session 2)

- [ ] First Regional Territory Map — BLOCKED
      → Cannot do without State data
      → Need to enrich data with external source

- [ ] Fuzzy match Infomerics ↔ d365 companies
      → 4 exact matches; true overlap likely 200–500 companies
      → Use rapidfuzz in Session 2

- [ ] INC company extraction
      → Companies with "(INC)" in rating walked out on Infomerics
      → Hottest possible leads — count and list them (Session 2)

- [ ] Agro/Food sector brief (Session 2)
- [ ] Steel & Metals sector brief (Session 2)
- [ ] Textiles sector brief (Session 2)

---

## P3 — Exploratory

- [ ] Seasonal pattern — which months have highest new issuances?
- [ ] Instrument family grouping — Short Term / Long Term / Structured
- [ ] ACER whitespace map — region x sector gap table
- [ ] Master company database — unified deduped list across both files

---

## Completed

- [x] Repo structure created — 2026-06-11
- [x] INSTRUCTIONS.md added to repo — 2026-06-11
- [x] TODO.md initialized — 2026-06-11
- [x] Full data profiling — both files — 2026-06-11 (Session 1)
- [x] Recency scoring — both files — 2026-06-11 (Session 1)
- [x] Competitor concentration analysis — d365 — 2026-06-11 (Session 1)
- [x] Top 50 sales lead list generated — 2026-06-11 (Session 1)
- [x] Infrastructure sector brief — 2026-06-11 (Session 1)
- [x] Company overlap check — 2026-06-11 (Session 1)
