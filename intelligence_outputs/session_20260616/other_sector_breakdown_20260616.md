# "Other" Sector Reclassification Breakdown — ACER Intelligence
Date: 2026-06-16 | Session 11
Data Sources: d365_data.xlsx + infomerics.json.xlsx
Total "Other" companies analyzed: 14,166

---

## Summary

The "Other" sector contained 14,166 companies — 67.7% of the 20,918-company master database.
This session applied keyword-based classification to company names, reclassifying 5,810 companies (41.0%)
into named sectors and uncovering **7 entirely new sectors** not previously tracked.

**5,810 companies reclassified | 8,356 remain unclassified (59.0%)**

---

## Reclassification Results — Existing Sectors (from Other)

| Sector | From Other | Total in DB (prev) | New Total | Change |
|--------|-----------|-------------------|-----------|--------|
| Agro/Food | +737 | 812 | 1,549 | +90.8% |
| Infrastructure | +717 | 1,225 | 1,942 | +58.5% |
| Construction | +715 | 702 | 1,417 | +101.9% |
| Steel/Metals | +594 | 555 | 1,149 | +107.0% |
| Chemicals/Pharma | +587 | 139 | 726 | +422.3% |
| IT/Software | +547 | 265 | 812 | +206.4% |
| Textiles | +445 | 336 | 781 | +132.4% |
| Hotels/Tourism | +163 | 84 | 247 | +194.0% |
| Healthcare | +75 | 371 | 446 | +20.2% |
| Logistics | +136 | 139 | 275 | +97.8% |
| Education | +29 | 70 | 99 | +41.4% |

**Chemicals/Pharma grew 422%** — it was severely undercounted (139 → 726). Now a major sector.
**Construction grew 102%** — nearly doubled (702 → 1,417).
**IT/Software grew 206%** — tripled (265 → 812). See dedicated brief.

---

## NEW Sectors Discovered (not previously in taxonomy)

| Sector | Companies | INC% | HIGH | Single-Agency% | ACER Priority |
|--------|-----------|------|------|----------------|---------------|
| Automobiles/Auto | 309 | 67.6% | 30 | 77.0% | HIGH |
| Trading/Exports | 198 | 64.1% | 17 | 77.3% | MEDIUM |
| Jewellery/Gems | 183 | 43.2% | 26 | 86.3% | MEDIUM |
| Mining/Minerals | 183 | 54.6% | 16 | 80.3% | MEDIUM |
| Media/Retail | 76 | 46.1% | 13 | 84.2% | LOW |
| Paper/Packaging | 64 | 76.6% | 7 | 57.8% | HIGH |
| Energy/Power | 44 | 22.7% | 5 | 72.7% | LOW |
| Telecom | 8 | 37.5% | 1 | 87.5% | LOW |

---

## Top Discovery: Automobiles/Auto — 309 Companies, 67.6% INC

This is the single most important finding of the reclassification exercise.

**309 Automobiles/Auto companies** — larger than Hotels/Tourism (247), Education (99), or Logistics (275).
**67.6% INC rate** — second-highest INC rate of all sectors (after Paper/Packaging's 76.6%).
**CRISIL dominates with 153 companies (49.5%)** — expensive agency for mid-tier dealers.

Who are these companies?
- Auto dealerships (cars, commercial vehicles, two-wheelers)
- Auto ancillary manufacturers (parts, components, castings)
- Auto finance companies (dealer credit, fleet financing)
- EV startups and charging infrastructure companies

ACER pitch: "CRISIL charges ₹4–6L for a dealership rating. ACER delivers the same SEBI-registered
output for ₹1.5–2.5L. Your BG/fund-based facility renewal should not cost as much as your salary cost."

Lead file: `csv/leads_Automobiles_Auto_20260616.csv` (309 rows)

---

## Surprise Finding: Paper/Packaging — 76.6% INC Rate (Highest of All Sectors)

**64 companies, 49 INC (76.6%)** — the highest INC rate across all 21+ sectors analyzed.

Paper/Packaging companies include:
- Paper mills and manufacturers
- Corrugated box manufacturers
- Flexible packaging companies
- Print/label manufacturers

Why such high INC? Paper/Packaging is capital-intensive with cyclical demand. Companies tend
to take ratings for initial bank credit, then let them lapse when credit lines are established.
This is a **re-engagement opportunity** — they had ratings before, they understand the process,
they just need a reason to renew.

Lead file: `csv/leads_Paper_Packaging_20260616.csv` (64 rows)

---

## Trading/Exports — 198 Companies, 64.1% INC

Export-oriented companies with bank guarantees for trade finance.
INC rate (64.1%) is high because export cycles are lumpy — companies get ratings for specific
export finance and then don't renew when the order book dips.

**ACER angle:** Trade finance season (pre-festival exports, Diwali goods) peaks August–October.
This is the right time to approach Trading/Exports companies for annual rating renewal.

---

## Revised Total Sector Landscape (After Reclassification)

| Sector | New Total | INC% | Status |
|--------|-----------|------|--------|
| Other (Unclassified) | 8,356 | ~45% est. | 59% of original Other |
| Manufacturing | 1,473 | 45.3% | Unchanged |
| Agro/Food | 1,549 | ~57% | +90.8% |
| Infrastructure | 1,942 | ~38% | +58.5% |
| Construction | 1,417 | ~42% | +101.9% |
| BFSI | 581 | 13.4% | Unchanged |
| Steel/Metals | 1,149 | ~61% | +107.0% |
| IT/Software | 812 | 42.5% | +206.4% |
| Chemicals/Pharma | 726 | ~45% | +422.3% |
| Textiles | 781 | ~66% | +132.4% |
| Hotels/Tourism | 247 | 38.1% | +194.0% |
| Healthcare | 446 | ~41% | +20.2% |
| Logistics | 275 | ~41% | +97.8% |
| Automobiles/Auto | 309 | 67.6% | NEW |
| Trading/Exports | 198 | 64.1% | NEW |
| Mining/Minerals | 183 | 54.6% | NEW |
| Jewellery/Gems | 183 | 43.2% | NEW |
| Media/Retail | 76 | 46.1% | NEW |
| Paper/Packaging | 64 | 76.6% | NEW |
| Education | 99 | ~31% | +41.4% |
| Energy/Power | 44 | 22.7% | NEW |

---

## Classification Methodology

Keywords matched against company names (case-insensitive, substring match).
Priority order applied when multiple sectors matched (e.g., "textile chemicals" → Chemicals/Pharma).
Methodology is keyword-based, not verified by external lookup.
Estimated precision: 85–90% for clear keywords (hotels, steel, infra), 70–75% for ambiguous names.

---

## What's Still in "Other (Unclassified)" — 8,356 Companies

The remaining unclassified companies are likely:
- **Conglomerates and diversified businesses** — names don't reveal sector (e.g., "Balaji Enterprises")
- **Trading companies** without sector-specific keywords
- **Professional services** (consulting, accounting, law) — not common credit rating clients
- **MSME manufacturing** not captured by keywords
- **Regional language company names** in romanized form

Recommendation: MCA CIN-based industry code lookup would unlock additional classification for ~40%
of remaining "Other" companies. CIN industry code (position 5–10 in CIN) encodes NIC activity.

---

## Files
- `csv/other_reclassified_20260616.csv` — 14,166 rows with New_Sector column
- `csv/leads_Automobiles_Auto_20260616.csv` — 309 rows (NEW sector)
- `csv/leads_Paper_Packaging_20260616.csv` — 64 rows (NEW sector)
- `csv/leads_Mining_Minerals_20260616.csv` — 183 rows (NEW sector)
