#!/usr/bin/env python3
"""
ACER Intelligence — Session 27 Analysis
Date: 2026-06-24
Tasks:
  1. CARE NCD INC deep-dive (sector + state + amount breakdown)
  2. BW stabilization root cause (volume trend: total records vs INC per month)
  3. 4-way INC investigation (deep profile both companies)
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
import os
import re

TODAY = date(2026, 6, 24)
SESSION_DIR = "intelligence_outputs/session_20260624_s27/csv"
os.makedirs(SESSION_DIR, exist_ok=True)

print("=" * 70)
print("ACER Intelligence — Session 27")
print(f"Analysis date: {TODAY}")
print("=" * 70)

# ─────────────────────────────────────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────────────────────────────────────
print("\n[LOADING DATA]")
d365_raw = pd.read_excel("d365_data.xlsx")
info_raw = pd.read_excel("infomerics.json.xlsx")
print(f"  D365: {len(d365_raw):,} records loaded")
print(f"  Infomerics: {len(info_raw):,} records loaded")

# ─────────────────────────────────────────────────────────────────────────────
# CLEAN D365
# ─────────────────────────────────────────────────────────────────────────────
d365 = d365_raw.copy()
d365.rename(columns={"Output source file name: W11": "Company Name"}, inplace=True)
d365 = d365[d365["Agency"].isin(["CRISIL","CARE","ICRA","IND-RA","ACUITE","BRICKWORK"])].copy()
d365.reset_index(drop=True, inplace=True)

def parse_date_d365(val):
    if pd.isna(val):
        return pd.NaT
    s = str(val).strip()
    for fmt in ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y"]:
        try:
            return pd.to_datetime(s, format=fmt)
        except:
            pass
    try:
        return pd.to_datetime(s, dayfirst=True)
    except:
        return pd.NaT

d365["Rating_Date"] = d365["Date"].apply(parse_date_d365)
d365["is_INC"] = d365["Company/Issuer not cooperating"].str.strip().str.upper() == "Y"
d365["Days_Since"] = d365["Rating_Date"].apply(
    lambda x: (TODAY - x.date()).days if pd.notna(x) else np.nan
)

def urgency(days):
    if pd.isna(days):
        return "UNKNOWN"
    if days >= 365:
        return "ULTRA HOT"
    if days >= 270:
        return "HOT"
    if days >= 180:
        return "MEDIUM"
    return "LOW"

d365["Urgency"] = d365["Days_Since"].apply(urgency)

# Standardise instrument
def std_instrument(i):
    if pd.isna(i):
        return 'Other'
    il = str(i).strip().lower()
    if 'non-government' in il or 'ncd' in il or 'debenture' in il or 'bond' in il:
        return 'NCD/Bond'
    if 'term loan' in il or il == 'tl':
        return 'Term Loan'
    if 'bank guarantee' in il or il == 'bg':
        return 'Bank Guarantee'
    if 'letter of credit' in il or il == 'lc' or 'l/c' in il:
        return 'Letter of Credit'
    if 'non-fund' in il or 'nfb' in il:
        return 'Non-Fund-Based'
    if ('fund' in il and 'based' in il) or il == 'fb':
        return 'Fund-Based'
    if 'commercial paper' in il or il == 'cp':
        return 'Commercial Paper'
    if 'cash credit' in il or il == 'cc' or 'overdraft' in il:
        return 'Cash Credit/OD'
    if 'working capital' in il:
        return 'Working Capital'
    return str(i).strip()

d365["Instrument_Std"] = d365["Instrument"].apply(std_instrument)

# Amount parsing
def parse_amount(v):
    if pd.isna(v):
        return np.nan
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).lower().replace(',', '').strip()
    m = re.search(r'[\d.]+', s)
    if m:
        val = float(m.group())
        if 'lakh' in s or 'lac' in s:
            val /= 100
        return val
    return np.nan

d365["Amount_Cr"] = d365["Ammount"].apply(parse_amount)

valid_d365 = d365[d365["Rating_Date"].notna()].copy()
print(f"  D365 valid dates: {len(valid_d365):,} records")
print(f"  D365 INC records: {d365['is_INC'].sum():,}")

# ─────────────────────────────────────────────────────────────────────────────
# CLEAN INFOMERICS
# ─────────────────────────────────────────────────────────────────────────────
info = info_raw.copy()

def parse_date_info(val):
    if pd.isna(val):
        return pd.NaT
    s = str(val).strip()
    for fmt in ["%B %d, %Y", "%d %B %Y", "%b %d, %Y", "%d-%m-%Y", "%Y-%m-%d"]:
        try:
            return pd.to_datetime(s, format=fmt)
        except:
            pass
    try:
        return pd.to_datetime(s)
    except:
        return pd.NaT

info["Rating_Date"] = info["Date"].apply(parse_date_info)
info["is_INC"] = info["Current Ratings"].str.contains("INC", na=False, case=False)
info["Days_Since"] = info["Rating_Date"].apply(
    lambda x: (TODAY - x.date()).days if pd.notna(x) else np.nan
)
info["Urgency"] = info["Days_Since"].apply(urgency)

print(f"  Infomerics valid dates: {info['Rating_Date'].notna().sum():,}")
print(f"  Infomerics INC records: {info['is_INC'].sum():,}")

# ─────────────────────────────────────────────────────────────────────────────
# SECTOR CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
SECTOR_PATTERNS = {
    'Steel & Metals':     r'steel|metal|iron|alumin|copper|zinc|tin|ferro|alloy|rolling|wire|pipe|tube|casting|forging',
    'Agro/Food':          r'agro|food|rice|sugar|cotton|grain|wheat|dal|oil mill|flour|poultry|dairy|spice|tea|coffee|tobacco|seed|farm|fert|pesticide|crop|mandi',
    'Construction':       r'construct|infra|build|cement|sand|stone|brick|tiles|real estate|realt|property|housing|township|developer',
    'Manufacturing':      r'manufactur|engineer|fabricat|component|assembly|industrial|equipment|machin',
    'Chemicals/Pharma':   r'chem|pharma|drug|\bapi\b|solvent|dye|pigment|polymer|plastic|rubber|petro|lubric|paint|varnish|resin|adhesive',
    'Textiles':           r'textile|garment|yarn|fabric|weav|spinning|knitting|cloth|apparel|fashion|silk|jute|fibre|fiber',
    'BFSI':               r'\bnbfc\b|\bnbf\b|finance|bank|lending|microfinance|mfi|housing finance|insurance|leasing|asset management|securities|stock|broker|mutual fund|wealth',
    'Energy':             r'energy|power|solar|wind|renew|electric|generat|turbine|coal\b|oil\b|gas\b|fuel|petrol|diesel|thermal|hydro',
    'Healthcare':         r'hospital|health|medical|clinic|diagnostic|lab|nursing|biotech|life science',
    'Logistics':          r'logistic|transport|shipping|freight|cargo|warehou|cold chain|courier|truck|fleet|port|aviation',
    'IT/Technology':      r'\bit\b|software|tech|digital|telecom|communicat|network|data|cloud|app|e-commerce|internet',
    'Automobiles':        r'auto|vehicle|\bcar\b|\bbike\b|motor|tyre|component|ancillar',
    'Mining/Minerals':    r'mining|mineral|quarry|granite|marble|coal mine|iron ore|bauxite|limestone',
    'Education':          r'school|college|university|educat|institute|academy|coaching|training',
    'Jewellery/Gems':     r'jewel|gem|diamond|gold|silver|ornament|bullion',
    'Paper/Packaging':    r'paper|packaging|cardboard|corrugat|carton|\bbag\b|sack|print|ink',
    'Hotels/Tourism':     r'hotel|resort|hospitality|tourism|travel|restaurant|cafe',
    'Trading/Exports':    r'trad|export|import|merchant|wholesale|distribut|dealer',
}

STATE_PATTERNS = {
    'Gujarat':      r'\bguj\b|gujarat|surat|ahmedabad|vadodara|baroda|rajkot|anand|mehsana|gandhinagar',
    'Maharashtra':  r'maharashtra|mumbai|pune|nagpur|nashik|aurangabad|solapur|kolhapur',
    'Tamil Nadu':   r'tamil|chennai|coimbatore|madurai|tirupur|salem|trichy',
    'UP':           r'\bup\b|uttar pradesh|lucknow|kanpur|agra|varanasi|meerut|allahabad',
    'Rajasthan':    r'rajasthan|jaipur|jodhpur|udaipur|kota|ajmer|bikaner',
    'Punjab':       r'punjab|ludhiana|amritsar|jalandhar|patiala',
    'Haryana':      r'haryana|gurugram|faridabad|panipat|ambala|rohtak',
    'Telangana':    r'telangana|hyderabad|secunderabad|warangal',
    'Karnataka':    r'karnataka|bengaluru|bangalore|mysore|hubli|mangalore',
    'West Bengal':  r'west bengal|kolkata|calcutta|howrah|durgapur|asansol',
    'Madhya Pradesh': r'madhya pradesh|bhopal|indore|gwalior|jabalpur|ujjain',
    'Delhi':        r'\bdelhi\b',
    'Andhra Pradesh': r'andhra|visakhapatnam|vizag|vijayawada|guntur|tirupati',
    'Odisha':       r'odisha|orissa|bhubaneswar|cuttack|rourkela',
    'Bihar':        r'\bbihar\b|patna|gaya|muzaffarpur',
    'Jharkhand':    r'jharkhand|ranchi|jamshedpur|dhanbad|bokaro',
    'Uttarakhand':  r'uttarakhand|dehradun|haridwar|rishikesh',
    'Chhattisgarh': r'chhattisgarh|raipur|bhilai|durg|bilaspur',
    'Kerala':       r'kerala|kochi|thiruvananthapuram|kozhikode|thrissur',
    'Goa':          r'\bgoa\b|panaji',
    'Assam':        r'\bassam\b|guwahati|dibrugarh|silchar',
}

def classify_sector(name):
    if pd.isna(name):
        return 'Other'
    n = str(name).lower()
    for sector, pattern in SECTOR_PATTERNS.items():
        if re.search(pattern, n):
            return sector
    return 'Other'

def infer_state(name):
    if pd.isna(name):
        return 'Unknown'
    n = str(name).lower()
    for state, pattern in STATE_PATTERNS.items():
        if re.search(pattern, n):
            return state
    return 'Unknown'

# ══════════════════════════════════════════════════════════════════════════════
# TASK 1 — CARE NCD INC DEEP-DIVE
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("TASK 1: CARE NCD INC DEEP-DIVE")
print("="*70)

# CARE NCD INC filter
care_ncd = d365[
    (d365["Agency"] == "CARE") &
    (d365["Instrument_Std"] == "NCD/Bond") &
    (d365["is_INC"])
].copy()

print(f"\nCARE NCD INC records: {len(care_ncd):,}")
print(f"CARE NCD INC unique companies: {care_ncd['Company Name'].nunique():,}")
print(f"\nInstrument values in CARE NCD INC records:")
print(care_ncd["Instrument"].value_counts().head(10))

# Check what NCD instruments CARE has
care_all_ncd = d365[(d365["Agency"] == "CARE") & (d365["Instrument_Std"] == "NCD/Bond")]
print(f"\nAll CARE NCD records (inc + non-inc): {len(care_all_ncd):,}")
print(f"CARE NCD INC rate: {len(care_ncd)/len(care_all_ncd)*100:.1f}%" if len(care_all_ncd) > 0 else "N/A")

# Also check CARE instruments distribution to find actual NCD label
print("\nAll CARE instrument values:")
print(d365[d365["Agency"]=="CARE"]["Instrument"].value_counts().head(20))

# Sector and state
care_ncd["Sector"] = care_ncd["Company Name"].apply(classify_sector)
care_ncd["State"] = care_ncd["Company Name"].apply(infer_state)

# Urgency breakdown
urg_breakdown = care_ncd.groupby("Urgency")["Company Name"].nunique().reset_index()
urg_breakdown.columns = ["Urgency", "Companies"]
print(f"\nUrgency breakdown:")
print(urg_breakdown.to_string(index=False))

# Sector breakdown
sector_breakdown = care_ncd.groupby("Sector").agg(
    Companies=("Company Name", "nunique"),
    Records=("Sector", "count"),
    ULTRA_HOT=("Urgency", lambda x: (x=="ULTRA HOT").sum()),
    HOT=("Urgency", lambda x: (x=="HOT").sum()),
    Avg_Days=("Days_Since", "mean"),
    Total_Amount_Cr=("Amount_Cr", "sum"),
    Max_Amount_Cr=("Amount_Cr", "max"),
).reset_index().sort_values("Companies", ascending=False)

print(f"\nCARE NCD INC — Sector Breakdown:")
print(sector_breakdown.to_string(index=False))

# State breakdown (identified ones)
state_identified = care_ncd[care_ncd["State"] != "Unknown"]
if len(state_identified) > 0:
    state_breakdown = state_identified.groupby("State").agg(
        Companies=("Company Name", "nunique"),
        ULTRA_HOT=("Urgency", lambda x: (x=="ULTRA HOT").sum()),
        HOT=("Urgency", lambda x: (x=="HOT").sum()),
    ).reset_index().sort_values("Companies", ascending=False)
    print(f"\nCARE NCD INC — State Breakdown (identified, {len(state_identified)} records):")
    print(state_breakdown.head(15).to_string(index=False))
else:
    print(f"\nState: No state identification from name for CARE NCD INC")

# Top companies by amount
top_by_amount = (care_ncd
    .sort_values("Amount_Cr", ascending=False)
    .drop_duplicates(subset=["Company Name"])
    [["Company Name", "Amount_Cr", "Urgency", "Days_Since", "Sector", "State"]]
    .head(25))
print(f"\nTop 25 CARE NCD INC companies by amount:")
print(top_by_amount.to_string(index=False))

# Monthly trend
care_ncd_valid = care_ncd[care_ncd["Rating_Date"].notna()].copy()
care_ncd_valid["YM"] = care_ncd_valid["Rating_Date"].dt.to_period("M").astype(str)
ym_trend = (care_ncd_valid.groupby("YM").agg(
    Records=("YM", "count"),
    Companies=("Company Name", "nunique"),
).reset_index().sort_values("YM"))
print(f"\nCARE NCD INC monthly trend (last 18 months):")
print(ym_trend[ym_trend["YM"] >= "2025-01"].to_string(index=False))

# Compare CARE NCD INC vs CARE NCD total by month
care_all_ncd_valid = care_all_ncd[care_all_ncd["Rating_Date"].notna()].copy()
care_all_ncd_valid["YM"] = care_all_ncd_valid["Rating_Date"].dt.to_period("M").astype(str)
care_ncd_total_monthly = (care_all_ncd_valid.groupby("YM").agg(
    Total_Records=("YM", "count"),
    INC_Records=("is_INC", "sum"),
).reset_index())
care_ncd_total_monthly["INC_Rate_pct"] = (
    care_ncd_total_monthly["INC_Records"] / care_ncd_total_monthly["Total_Records"] * 100
).round(1)
print(f"\nCARE NCD total vs INC by month (last 18 months):")
print(care_ncd_total_monthly[care_ncd_total_monthly["YM"] >= "2025-01"].to_string(index=False))

# Build output CSV — full list
care_ncd_out = care_ncd[[
    "Company Name", "Instrument", "Amount_Cr", "Rating", "Rating_Date",
    "Days_Since", "Urgency", "Sector", "State"
]].copy()
care_ncd_out.columns = [
    "Company Name", "Instrument", "Amount (Cr)", "Rating", "Rating Date",
    "Days Since Rating", "Urgency", "Sector", "State"
]
care_ncd_out["Current Rater"] = "CARE"
care_ncd_out["Why Target"] = care_ncd_out.apply(
    lambda r: (
        f"CARE NCD INC {r['Days Since Rating']:.0f} days — NCD instrument non-functional; "
        "active rating needed for compliance and re-issuance"
    ), axis=1
)
care_ncd_out["ACER Pitch Angle"] = care_ncd_out.apply(
    lambda r: (
        f"Your NCD at CARE has been INC for {r['Days Since Rating']:.0f} days — "
        "this blocks bond re-issuance and triggers investor communication obligations. "
        "ACER provides fresh NCD ratings in 30 days with dedicated analyst access."
        if r["Urgency"] in ("ULTRA HOT", "HOT")
        else f"CARE NCD INC — {r['Days Since Rating']:.0f} days. ACER can restore active NCD status."
    ), axis=1
)
care_ncd_out = care_ncd_out.sort_values("Days Since Rating", ascending=False)

out1 = f"{SESSION_DIR}/care_ncd_inc_deepdive_20260624.csv"
care_ncd_out.to_csv(out1, index=False)
print(f"\n✓ Saved: {out1} ({len(care_ncd_out):,} rows)")

# Sector summary
sector_out = f"{SESSION_DIR}/care_ncd_inc_sector_summary_20260624.csv"
sector_breakdown.to_csv(sector_out, index=False)
print(f"✓ Saved: {sector_out} ({len(sector_breakdown)} rows)")

# Hot-only (callable now: ULTRA HOT + HOT)
care_ncd_hot = care_ncd_out[care_ncd_out["Urgency"].isin(["ULTRA HOT", "HOT"])].copy()
hot_out = f"{SESSION_DIR}/care_ncd_inc_hot_only_20260624.csv"
care_ncd_hot.to_csv(hot_out, index=False)
print(f"✓ Saved: {hot_out} ({len(care_ncd_hot):,} rows)")

# Print CARE NCD INC summary stats
print(f"\n--- CARE NCD INC SUMMARY ---")
print(f"Total unique companies: {care_ncd['Company Name'].nunique():,}")
print(f"ULTRA HOT (365+ days): {(care_ncd['Urgency']=='ULTRA HOT').sum():,}")
print(f"HOT (270-364 days): {(care_ncd['Urgency']=='HOT').sum():,}")
print(f"MEDIUM (180-269 days): {(care_ncd['Urgency']=='MEDIUM').sum():,}")
print(f"LOW (<180 days): {(care_ncd['Urgency']=='LOW').sum():,}")
total_amount_identified = care_ncd["Amount_Cr"].sum()
print(f"Total rated amount (identified): ₹{total_amount_identified:,.1f} Cr")
print(f"Top sector: {sector_breakdown.iloc[0]['Sector']} ({int(sector_breakdown.iloc[0]['Companies'])} companies)")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 2 — BRICKWORK STABILIZATION ROOT CAUSE
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("TASK 2: BRICKWORK STABILIZATION ROOT CAUSE")
print("="*70)

bw = d365[d365["Agency"] == "BRICKWORK"].copy()
bw_valid = bw[bw["Rating_Date"].notna()].copy()
bw_valid["YM"] = bw_valid["Rating_Date"].dt.to_period("M").astype(str)

print(f"\nBW total records: {len(bw):,}")
print(f"BW valid dates: {len(bw_valid):,}")
print(f"BW date range: {bw_valid['Rating_Date'].min().date()} to {bw_valid['Rating_Date'].max().date()}")
print(f"BW INC records: {bw['is_INC'].sum():,}")
print(f"BW non-INC records: {(~bw['is_INC']).sum():,}")

# Monthly breakdown
monthly_rows = []
for ym, grp in bw_valid.groupby("YM"):
    total_rec = len(grp)
    inc_rec = int(grp["is_INC"].sum())
    non_inc_rec = total_rec - inc_rec
    unique_co = grp["Company Name"].nunique()
    inc_co = grp[grp["is_INC"]]["Company Name"].nunique()
    non_inc_co = grp[~grp["is_INC"]]["Company Name"].nunique()
    inc_rate = inc_rec / total_rec * 100 if total_rec > 0 else 0
    monthly_rows.append({
        "Year_Month": ym,
        "Total_Records": total_rec,
        "INC_Records": inc_rec,
        "Active_Non_INC_Records": non_inc_rec,
        "Total_Companies": unique_co,
        "INC_Companies": inc_co,
        "Active_Companies": non_inc_co,
        "INC_Rate_pct": round(inc_rate, 1),
    })

bw_monthly = pd.DataFrame(monthly_rows).sort_values("Year_Month")
print(f"\nBW Monthly Volume vs INC (all months):")
print(bw_monthly.to_string(index=False))

# Half-year aggregations
def half_year_avg(df, ym_start, ym_end, col):
    subset = df[(df["Year_Month"] >= ym_start) & (df["Year_Month"] <= ym_end)]
    return subset[col].mean() if len(subset) > 0 else np.nan

print(f"\n--- Volume Trend Analysis ---")
for period, ym_s, ym_e in [
    ("H1 2024", "2024-01", "2024-06"),
    ("H2 2024", "2024-07", "2024-12"),
    ("H1 2025", "2025-01", "2025-06"),
    ("H2 2025", "2025-07", "2025-12"),
    ("H1 2026", "2026-01", "2026-06"),
]:
    total_avg = half_year_avg(bw_monthly, ym_s, ym_e, "Total_Records")
    active_avg = half_year_avg(bw_monthly, ym_s, ym_e, "Active_Non_INC_Records")
    inc_avg = half_year_avg(bw_monthly, ym_s, ym_e, "INC_Records")
    inc_rate_avg = half_year_avg(bw_monthly, ym_s, ym_e, "INC_Rate_pct")
    if not np.isnan(total_avg):
        print(f"  {period}: Total={total_avg:.0f}/mo | Active={active_avg:.0f}/mo | INC={inc_avg:.0f}/mo | INC_Rate={inc_rate_avg:.1f}%")

# Year over year new active ratings
bw_2024_active = bw_valid[(bw_valid["Rating_Date"].dt.year == 2024) & (~bw_valid["is_INC"])]
bw_2025_active = bw_valid[(bw_valid["Rating_Date"].dt.year == 2025) & (~bw_valid["is_INC"])]
bw_2026_active = bw_valid[(bw_valid["Rating_Date"].dt.year == 2026) & (~bw_valid["is_INC"])]

print(f"\nBW Active (non-INC) ratings by year:")
print(f"  2024: {len(bw_2024_active):,} records ({bw_2024_active['Company Name'].nunique():,} companies)")
print(f"  2025: {len(bw_2025_active):,} records ({bw_2025_active['Company Name'].nunique():,} companies)")
print(f"  2026: {len(bw_2026_active):,} records ({bw_2026_active['Company Name'].nunique():,} companies) [partial year]")

# What instruments is BW still active in?
print(f"\nBW active instruments in 2025:")
print(bw_2025_active["Instrument_Std"].value_counts().head(10))
print(f"\nBW active instruments in 2026 (partial):")
print(bw_2026_active["Instrument_Std"].value_counts().head(10))

# INC records by year — is BW INC pool GROWING or just static?
bw_2024_inc = bw_valid[(bw_valid["Rating_Date"].dt.year == 2024) & (bw_valid["is_INC"])]
bw_2025_inc = bw_valid[(bw_valid["Rating_Date"].dt.year == 2025) & (bw_valid["is_INC"])]
bw_2026_inc = bw_valid[(bw_valid["Rating_Date"].dt.year == 2026) & (bw_valid["is_INC"])]

print(f"\nBW INC issuances by year:")
print(f"  2024: {len(bw_2024_inc):,} records ({bw_2024_inc['Company Name'].nunique():,} companies)")
print(f"  2025: {len(bw_2025_inc):,} records ({bw_2025_inc['Company Name'].nunique():,} companies)")
print(f"  2026: {len(bw_2026_inc):,} records ({bw_2026_inc['Company Name'].nunique():,} companies)")

# Key diagnostic: Is the INC pool growing (new INC) or staying same (old INC never cleared)?
# Look at INC records issued MOST RECENTLY — these are new INC entries
bw_inc_recent = bw_valid[bw_valid["is_INC"]].copy()
bw_inc_recent["YM"] = bw_inc_recent["Rating_Date"].dt.to_period("M").astype(str)
bw_inc_by_year = bw_inc_recent.groupby(bw_inc_recent["Rating_Date"].dt.year)["Company Name"].nunique()
print(f"\nBW INC unique companies per year (by INC date):")
print(bw_inc_by_year)

# Save monthly trend
bw_monthly.to_csv(f"{SESSION_DIR}/brickwork_volume_vs_inc_20260624.csv", index=False)
print(f"\n✓ Saved: {SESSION_DIR}/brickwork_volume_vs_inc_20260624.csv ({len(bw_monthly)} rows)")

# Diagnosis
print(f"\n--- BW DIAGNOSIS ---")
h1_2025_total = half_year_avg(bw_monthly, "2025-01", "2025-06", "Total_Records")
h1_2026_total = half_year_avg(bw_monthly, "2026-01", "2026-06", "Total_Records")
h1_2025_active_v = half_year_avg(bw_monthly, "2025-01", "2025-06", "Active_Non_INC_Records")
h1_2026_active_v = half_year_avg(bw_monthly, "2026-01", "2026-06", "Active_Non_INC_Records")
if not np.isnan(h1_2025_total) and not np.isnan(h1_2026_total):
    total_change = (h1_2026_total - h1_2025_total) / h1_2025_total * 100
    active_change = (h1_2026_active_v - h1_2025_active_v) / max(1, h1_2025_active_v) * 100
    print(f"Total volume change H1 2025 → H1 2026: {total_change:+.1f}%")
    print(f"Active (non-INC) volume change H1 2025 → H1 2026: {active_change:+.1f}%")
    if active_change < -20:
        print("→ ROOT CAUSE: BW volume DECLINE — issuing far fewer new ratings")
    elif active_change > 0:
        print("→ ROOT CAUSE: BW active volume STABLE/GROWING — INC backlog is structural, not resolved")
    else:
        print("→ ROOT CAUSE: BW active volume declining moderately — both volume loss and INC retention")

# ══════════════════════════════════════════════════════════════════════════════
# TASK 3 — 4-WAY INC INVESTIGATION
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "="*70)
print("TASK 3: 4-WAY INC INVESTIGATION")
print("="*70)

# Find companies INC at 4+ agencies
inc_only = d365[d365["is_INC"]].copy()
agency_count_per_company = (
    inc_only.groupby("Company Name")["Agency"]
    .nunique()
    .reset_index()
    .rename(columns={"Agency": "N_INC_Agencies"})
)

four_plus = agency_count_per_company[agency_count_per_company["N_INC_Agencies"] >= 4].copy()
three_plus = agency_count_per_company[agency_count_per_company["N_INC_Agencies"] >= 3].copy()
two_plus = agency_count_per_company[agency_count_per_company["N_INC_Agencies"] >= 2].copy()

print(f"\nCompanies INC at 2+ agencies: {len(two_plus):,}")
print(f"Companies INC at 3+ agencies: {len(three_plus):,}")
print(f"Companies INC at 4+ agencies: {len(four_plus):,}")

if len(four_plus) > 0:
    print(f"\n4-way+ INC companies:")
    print(four_plus.sort_values("N_INC_Agencies", ascending=False).to_string(index=False))
else:
    print("No companies found with INC at 4+ agencies in D365 alone.")
    print("Checking 'New Modern Technomech' specifically...")
    nmt_matches = d365[d365["Company Name"].str.lower().str.contains("modern technomech|new modern", na=False)]
    if len(nmt_matches) > 0:
        print(f"Found: {nmt_matches['Company Name'].unique()}")
        print(nmt_matches[["Company Name", "Agency", "Instrument", "Rating", "Rating_Date", "Days_Since", "Urgency", "Amount_Cr", "is_INC"]].to_string(index=False))
    else:
        print("New Modern Technomech not found by name.")

# For 4-way companies, get full profiles
four_way_companies = four_plus["Company Name"].tolist()
profiles = []

if four_way_companies:
    for co in four_way_companies:
        co_all = d365[d365["Company Name"] == co].copy()
        co_inc = co_all[co_all["is_INC"]].copy()
        inc_agencies = sorted(co_inc["Agency"].unique().tolist())
        sector = classify_sector(co)
        state = infer_state(co)
        max_amt = co_all["Amount_Cr"].max()
        max_days = co_inc["Days_Since"].max()

        print(f"\n{'='*60}")
        print(f"COMPANY: {co}")
        print(f"Sector: {sector} | State: {state}")
        print(f"INC at {len(inc_agencies)} agencies: {', '.join(inc_agencies)}")
        print(f"Max amount: ₹{max_amt:.1f} Cr" if not np.isnan(max_amt) else "Amount: Unknown")
        print(f"Most overdue INC: {max_days:.0f} days" if not np.isnan(max_days) else "Days: Unknown")

        print(f"\nAll records:")
        display_cols = ["Company Name", "Agency", "Instrument", "Rating", "Rating_Date", "Days_Since", "Urgency", "Amount_Cr", "is_INC"]
        display_cols = [c for c in display_cols if c in co_all.columns]
        print(co_all[display_cols].sort_values("Rating_Date", ascending=False).to_string(index=False))

        # Rating history narrative
        print(f"\nRating history (chronological):")
        for _, row in co_all.sort_values("Rating_Date").iterrows():
            inc_flag = "⚠️ INC" if row["is_INC"] else "✓ ACTIVE"
            amt_str = f"₹{row['Amount_Cr']:.1f}Cr" if not np.isnan(row["Amount_Cr"]) else ""
            print(f"  {row['Rating_Date'].date() if pd.notna(row['Rating_Date']) else 'UNKNOWN'} | "
                  f"{row['Agency']:12} | {str(row['Instrument'])[:30]:30} | "
                  f"{str(row['Rating']):20} | {amt_str:15} | {inc_flag}")

        # Was this company ever not INC?
        ever_active = co_all[~co_all["is_INC"]]
        if len(ever_active) > 0:
            latest_active = ever_active.sort_values("Rating_Date").iloc[-1]
            print(f"\n  Last ACTIVE rating: {latest_active['Rating_Date'].date()} at {latest_active['Agency']} — {latest_active['Rating']}")
            print(f"  → Company WAS active, then went INC at all agencies")
        else:
            print(f"\n  NO active (non-INC) records found — company has ALWAYS been INC in this dataset")

        # Profile row for CSV
        for _, irec in co_inc.iterrows():
            profiles.append({
                "Company Name": co,
                "Agency": irec["Agency"],
                "Instrument": irec["Instrument"],
                "Rating": irec["Rating"],
                "Rating Date": irec["Rating_Date"],
                "Days Since Rating": irec["Days_Since"],
                "Urgency": irec["Urgency"],
                "Amount (Cr)": irec["Amount_Cr"],
                "Sector": sector,
                "State": state,
                "N_INC_Agencies": len(inc_agencies),
                "INC_Agencies_List": ", ".join(inc_agencies),
                "Why Target": (
                    f"INC at ALL {len(inc_agencies)} major agencies simultaneously — "
                    f"maximum displacement opportunity; {irec['Days_Since']:.0f} days overdue at {irec['Agency']}"
                ),
                "ACER Pitch Angle": (
                    f"{co} has been INC at every established agency. "
                    "ACER offers a fresh start: dedicated analyst, transparent criteria, "
                    "new review process within 45 days. This is likely a documentation "
                    "or cooperation issue we can help resolve."
                ),
            })

# Also look for 4-way counting across d365 + infomerics combined
print(f"\n--- Cross-source 4-way check (D365 + Infomerics) ---")
# Normalise company names for fuzzy match
def normalise_name(n):
    if pd.isna(n): return ''
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', '', str(n).lower())).strip()

d365_inc_cos = set(d365[d365["is_INC"]]["Company Name"].dropna().unique())
inf_inc_cos  = set(info[info["is_INC"]]["Company Name"].dropna().unique())

# For each infomerics INC company, check if it's ALSO INC at 3+ D365 agencies
inf_inc_normalised = {normalise_name(c): c for c in inf_inc_cos}
d365_3way = agency_count_per_company[agency_count_per_company["N_INC_Agencies"] >= 3]["Company Name"].tolist()

cross_4way = []
for d365_co in d365_3way:
    d365_norm = normalise_name(d365_co)
    # Check if matching infomerics INC
    for inf_norm, inf_co in inf_inc_normalised.items():
        # Simple token overlap check
        d365_tokens = set(d365_norm.split())
        inf_tokens  = set(inf_norm.split())
        if len(d365_tokens) >= 2 and len(inf_tokens) >= 2:
            overlap = len(d365_tokens & inf_tokens) / max(len(d365_tokens), len(inf_tokens))
            if overlap >= 0.7:
                d365_agencies = inc_only[inc_only["Company Name"] == d365_co]["Agency"].unique()
                cross_4way.append({
                    "D365_Company": d365_co,
                    "Infomerics_Company": inf_co,
                    "D365_INC_Agencies": ", ".join(sorted(d365_agencies)),
                    "D365_N_INC": len(d365_agencies),
                    "Total_INC_Sources": len(d365_agencies) + 1,  # +1 for Infomerics
                    "Name_Match_Score": round(overlap, 2),
                })

cross_4way_df = pd.DataFrame(cross_4way) if cross_4way else pd.DataFrame()
if len(cross_4way_df) > 0:
    cross_4way_df = cross_4way_df.sort_values("Total_INC_Sources", ascending=False)
    print(f"\nCompanies INC at 3+ D365 agencies AND Infomerics = effectively 4-way:")
    print(cross_4way_df.head(20).to_string(index=False))
else:
    print("No cross-source 4-way matches found.")

# Also specifically search for "New Modern Technomech" in infomerics
print("\n--- Searching for 'New Modern Technomech' in Infomerics ---")
nmt_inf = info[info["Company Name"].str.lower().str.contains("modern|technomech", na=False)]
if len(nmt_inf) > 0:
    print(nmt_inf[["Company Name", "Instruments", "Current Ratings", "Rating_Date", "Days_Since", "Urgency", "is_INC"]].to_string(index=False))
else:
    print("Not found in Infomerics.")

# Save profiles
if profiles:
    profiles_df = pd.DataFrame(profiles)
    out_4way = f"{SESSION_DIR}/four_way_inc_profiles_20260624.csv"
    profiles_df.to_csv(out_4way, index=False)
    print(f"\n✓ Saved: {out_4way} ({len(profiles_df)} rows)")
elif cross_4way_df is not None and len(cross_4way_df) > 0:
    out_4way = f"{SESSION_DIR}/four_way_inc_profiles_20260624.csv"
    cross_4way_df.to_csv(out_4way, index=False)
    print(f"\n✓ Saved cross-source 4-way: {out_4way} ({len(cross_4way_df)} rows)")
else:
    # Find all 3-way+ companies for context
    three_way_df = agency_count_per_company[agency_count_per_company["N_INC_Agencies"] >= 3].copy()
    three_way_df["INC_Agencies_List"] = three_way_df["Company Name"].apply(
        lambda co: ", ".join(sorted(inc_only[inc_only["Company Name"]==co]["Agency"].unique()))
    )
    three_way_df["Sector"] = three_way_df["Company Name"].apply(classify_sector)
    three_way_df["Max_Amount"] = three_way_df["Company Name"].apply(
        lambda co: d365[d365["Company Name"]==co]["Amount_Cr"].max()
    )
    three_way_df["Max_Days"] = three_way_df["Company Name"].apply(
        lambda co: inc_only[inc_only["Company Name"]==co]["Days_Since"].max()
    )
    out_4way = f"{SESSION_DIR}/four_way_inc_profiles_20260624.csv"
    three_way_df.sort_values("N_INC_Agencies", ascending=False).to_csv(out_4way, index=False)
    print(f"\n✓ Saved 3-way+ context: {out_4way} ({len(three_way_df)} rows)")

print("\n" + "="*70)
print("ALL TASKS COMPLETE — Session 27")
print(f"Output directory: {SESSION_DIR}")
print("="*70)
