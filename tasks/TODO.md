# ACER Intelligence — Master Task List
Last Updated: 2026-06-11
Status: Session 0 — Initialized, no analysis done yet

---

## P1 — Do This Session (Tonight)

- [ ] Read and profile infomerics.json.xlsx
      → Print column names, row count, date range
      → Check for nulls in Company Name, Rating Date, Instrument
      → List all unique instrument types and sectors found

- [ ] Read and profile d365_data.xlsx
      → Same profiling as above
      → List all unique agency names found in this file
      → Check date range coverage

- [ ] Check overlap between both files
      → Are the same companies appearing in both?
      → Are column names consistent or need mapping?

- [ ] Map all states to regions
      → North / South / East / West / Central
      → Tag every record in both files

- [ ] Build Instrument Recency Score on both files
      → Less than 6 months → LOW
      → 6 to 11 months → MEDIUM
      → More than 12 months → HIGH

---

## P2 — Next Sessions

- [ ] Competitor Concentration Analysis
      → Count how many agencies rated each company in d365_data
      → Flag single-agency vs multi-agency companies
      → Identify recently downgraded companies

- [ ] Sector Attractiveness Matrix
      → Score each sector: volume + competitor spread + recency

- [ ] First Regional Territory Map
      → Pick top 2 regions by company density
      → Produce regional intelligence brief

- [ ] First Sales Lead List
      → 20 to 30 companies with priority score and pitch angle
      → Save to intelligence_outputs/

- [ ] Identify downgraded entities
      → Companies whose rating moved negatively in last 12 months
      → These are priority outreach targets

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
