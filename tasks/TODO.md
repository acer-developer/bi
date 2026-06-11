# ACER Intelligence — Master Task List
Last Updated: 2026-06-11
Status: Session 1 — Data profiling complete; regional/sector analysis blocked on missing fields

---

## DATA GAPS (Action Required Before Next Session)

> **Leadership action needed:**
> 1. Add **State/Region** column to d365_data.xlsx — required for regional territory maps
> 2. Add **Sector/Industry** column to infomerics data — required for sector attractiveness matrix
> Without these fields, WHERE and WHICH questions remain blocked.

---

## P1 — Next Session

- [ ] Regional lead lists — North, South, West, East, Central
      → BLOCKED until State field added to source files
      → Once available: produce region_map_[REGION]_20260611.md for top 3 regions

- [ ] Sector Attractiveness Matrix
      → BLOCKED until Sector field added to infomerics
      → Score each sector: volume + competitor spread + recency

- [ ] Top 30 lead profiles with pitch sheets
      → Expand leads_NATIONAL_20260611.md top 30 into individual pitch cards
      → Include: company background, current rater, why switching, ACER pitch angle

- [ ] Downgrade trend analysis
      → Which agencies are downgrading the most? (by sector if data available)
      → Which time periods had highest downgrade rates?

- [ ] Competitor concentration deep-dive by instrument type
      → Which instruments have highest multi-agency penetration?
      → Where is CRISIL most captive?

---

## P2 — Backlog

- [ ] Fuzzy name matching to unify cross-file company records
      → Only 4 exact matches found despite large overlap
      → Need NLP/fuzzy logic to deduplicate across infomerics + d365

- [ ] Seasonal issuance pattern analysis
      → Which months have highest new issuances in infomerics?
      → Align ACER sales cycles to peak activity months

- [ ] ACER whitespace map — region × sector gap table
      → Requires both State and Sector fields

- [ ] Master company database — unified deduped list across both files

---

## P3 — Exploratory

- [ ] Instrument family grouping — Short Term / Long Term / Structured
- [ ] INC company deep-dive — which sectors have most INC companies?
- [ ] Rating trajectory analysis — companies that were upgraded after INC

---

## Completed

- [x] Repo structure created — 2026-06-11
- [x] INSTRUCTIONS.md added to repo — 2026-06-11
- [x] TODO.md initialized — 2026-06-11
- [x] Profile infomerics.json.xlsx — Session 1, 2026-06-11
      → 8,438 rows, 4,175 companies, Dec 2016–Feb 2026
      → Columns: Company Name, Date, Instruments, Size, Current Ratings, Outlook, Rating Rationale PDF, Source URL
      → FINDING: No State or Sector column — data enrichment needed
- [x] Profile d365_data.xlsx — Session 1, 2026-06-11
      → 49,945 rows, 17,622 companies, May 2025–May 2026
      → Agencies: CRISIL 37.1%, CARE 22.1%, ICRA 12.7%, IND-RA 10.3%, ACUITE 9.3%, BRICKWORK 8.5%
      → FINDING: No State/Region column — data enrichment needed
- [x] Cross-file overlap check — Session 1, 2026-06-11
      → Only 4 exact matches; fuzzy matching needed
- [x] State-to-region mapping — BLOCKED (no state data in either file)
- [x] Build Instrument Recency Score — Session 1, 2026-06-11
      → Infomerics: HIGH 4,308 / MEDIUM 2,687 / LOW 1,439
      → D365: HIGH 8,926 / MEDIUM 21,576 / LOW 19,441
- [x] Competitor concentration analysis — Session 1, 2026-06-11
      → 3,623 multi-agency companies (VERY HIGH opportunity)
      → 13,999 single-agency companies (MEDIUM opportunity)
- [x] Identify downgraded entities — Session 1, 2026-06-11
      → 2,966 companies downgraded in last 12 months
      → Saved: downgraded_targets_20260611.md
- [x] INC company identification — Session 1, 2026-06-11
      → 55 unique INC companies in Infomerics (1,008 instruments)
      → Saved: infomerics_INC_targets_20260611.md
- [x] First Sales Lead List — Session 1, 2026-06-11
      → Top 50 national leads with lead scores
      → Saved: leads_NATIONAL_20260611.md
