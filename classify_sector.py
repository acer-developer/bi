"""
Canonical sector classifier for ACER intelligence pipelines (H12, Session 43).

Every prior pipeline-window build (Sessions 33-42) re-implemented this logic inline,
each with a slightly different keyword list and priority order — the root cause traced
in intelligence_outputs/session_20260702/csv/sector_tagging_root_cause_20260702.csv.
This module is the single source of truth going forward: import classify_sector() /
SECTOR_PATTERNS here instead of redefining them in a new session script.

Usage:
    from classify_sector import classify_sector
    df['Sector'] = df['Company Name'].apply(classify_sector)

Design notes:
- Dict order = check order; first regex match wins. Ordering resolves the specific
  collisions found in sector_misclassification_flags_20260701.csv (97 companies):
  paper/hospitality/medicare/housing-finance/beverages/fincorp/broadcast keywords are
  placed ahead of sectors whose own keywords are generic tokens that can appear embedded
  in unrelated names (auto, trad, tin, car).
- Jewellery/Gems is checked last (before Other) because diamond/gold/silver are common
  brand-name modifiers unrelated to the jewellery trade ("Diamond Beverages", "Diamond
  Textile Mills", "Diamond Shipping Agencies").
- Short/collision-prone tokens (car, tin, oil, gas, up) use \\b..\\b word boundaries;
  longer distinctive stems (construct, manufactur, textile) use a leading \\b only so
  plurals/derivatives still match.
- Classification from company name text alone is inherently ambiguous for some names
  (e.g. bare "Biotech", "Autolinks", "Projects") — MCA CIN NIC code enrichment (P1
  backlog item) is the only way to fully resolve these; this module is a same-day
  quality floor, not a replacement for ground-truth industry codes.
"""
import re

import pandas as pd

# The live master pipeline (acer_revenue_model_20260630.csv) carries duplicate labels
# for the same concept because each window used a different classifier variant. Map
# any pre-existing duplicate label found in prior outputs to its one canonical form.
SECTOR_ALIASES = {
    'Energy/Power': 'Energy',
    'BFSI/NBFC': 'BFSI',
    'Jewellery': 'Jewellery/Gems',
    'Mining': 'Mining & Minerals',
}

SECTOR_PATTERNS = {
    'Paper/Packaging':    r'\bpapers?\b|packaging|cardboard|corrugat|carton|\bbags?\b|\bsacks?\b|\bprint(ing)?\b|\binks?\b|\bpulps?\b',
    'Hotels & Tourism':   r'\bhotels?\b|\bresorts?\b|hospitality|tourism|\btravels?\b|\brestaurants?\b|\bcafe\b',
    'BFSI':               r'\bnbfc\b|\bnbf\b|\bfinance\b|financ(e|ial)|\bfincorp\b|\bbank\b|lending|microfinance|\bmfi\b|housing finance|\binsurance\b|leasing|asset management|\bsecurities\b|\bstock\b|\bbroker|mutual fund|wealth',
    'Media/Retail':       r'\bbroadcast(ing)?\b|\bmedia\b|\bretail\b|\btelevision\b|\bpublish',
    'Mining & Minerals':  r'\bmining\b|\bmineral|\bquarry\b|\bgranite\b|\bmarble\b|coal mine|iron ore|\bbauxite\b|\blimestone\b',
    'Steel & Metals':     r'\bsteel\b|\bmetals?\b|\biron\b|alumin|\bcopper\b|\bzinc\b|\btin\b|\btitanium\b|\bferro|\balloy\b|\brolling\b|\bwires?\b|\bpipes?\b|\btubes?\b|\bcasting\b|\bforging\b',
    'Automobiles':        r'\bauto(mobile)?s?\b|\bvehicles?\b|\bcar\b|\bbike\b|\bmotors?\b|\btyre\b|auto component|ancillar',
    'Agro & Food':        r'\bagro\b|\bagri\b|\bfood\b|\brice\b|\bsugar\b|\bcotton\b|\bgrain\b|\bwheat\b|\bdal\b|oil mill|\boils?\b|\bflour\b|\bpoultry\b|\bdairy\b|\bspice|\btea\b|\bcoffee\b|\btobacco\b|\bseeds?\b|\bfarm\b|\bfert|pesticide|\bcrops?\b|\bmandi\b|\bbeverages?\b|\bsprinklers?\b|\birrigation\b',
    'Healthcare':         r'\bhospitals?\b|\bhealth\b|healthcare|\bmedical\b|\bmedicare\b|\bclinics?\b|diagnostic|\bnursing\b|biotech|life science',
    'Construction':       r'\bconstruct|\binfra(structure)?\b|\bbuild(ers?|ing)?\b|\bcement\b|\bsand\b|\bstone\b|\bbricks?\b|\btiles?\b|real estate|\brealty\b|\bproperty\b|\bhousing\b|\btownship\b|\bdevelopers?\b',
    'Manufacturing':      r'\bmanufactur|\bengineer|\bfabricat|\bassembly\b|\bindustrial\b|\bequipment\b|\bmachin',
    'Chemicals & Pharma': r'\bchem|\bpharma|\bdrugs?\b|\bapi\b|\bsolvent|\bdye\b|\bpigment|\bpolymer|\bplastic|\brubber\b|\bpetro|lubric|\bpaint|\bvarnish|\bresin|\badhesive',
    'Textiles':           r'\btextile|\bgarment|\byarn\b|\bfabric|\bweav|spinning|\bknit|\bcloth|\bapparel|\bfashion\b|\bsilk\b|\bjute\b|\bfibre|\bfiber',
    'Energy':             r'\benergy\b|\bpower\b|\bsolar\b|\bwind\b|\brenewabl|\belectric|\bgenerat|\bturbine\b|\bcoal\b|\bgas\b|\bfuel\b|\bpetrol\b|\bdiesel\b|\bthermal\b|\bhydro',
    'Logistics':          r'\blogistic|\btransport|\bshipping\b|\bfreight\b|\bcargo\b|warehous|cold chain|\bcourier\b|\btrucks?\b|\bfleet\b|\bport\b|\baviation\b',
    'IT/Technology':      r'\bit\b|\bsoftware\b|\btech\b|\bdigital\b|\btelecom|communicat|\bnetwork\b|\bdata\b|\bcloud\b|\bapp\b|e-commerce|\binternet\b|\bcyber',
    'Trading/Exports':    r'\btrad(e|ing|es)\b|\bexports?\b|\bimports?\b|\bmerchant|\bwholesale\b|\bdistribut|\bdealers?\b',
    'Jewellery/Gems':     r'\bjewel|\bgems?\b|\bdiamonds?\b|\bgold\b|\bsilver\b|\bornament|\bbullion\b',
    'Education':          r'\bschools?\b|\bcolleges?\b|\buniversity\b|\beducat|\binstitutes?\b|\bacademy\b|\bcoaching\b|\btraining\b',
}


def classify_sector(name):
    """Classify a company name into one of the canonical SECTOR_PATTERNS keys, or 'Other'."""
    if pd.isna(name):
        return 'Other'
    n = str(name).lower()
    for sector, pattern in SECTOR_PATTERNS.items():
        if re.search(pattern, n):
            return sector
    return 'Other'


def normalize_sector_label(label):
    """Collapse a pre-existing (possibly duplicate) Sector column value to its canonical form."""
    return SECTOR_ALIASES.get(label, label)
