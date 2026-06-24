"""
ACER Intelligence Session 26 — 2026-06-24
P1 Tasks:
  1. NCD-focused calling list
  2. Brickwork 2026 trend check
  3. 78 TIER 1 super-targets senior RM assignment brief
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
import os
import warnings
warnings.filterwarnings('ignore')

TODAY = date(2026, 6, 24)
SESSION_DATE = "20260624"
OUTPUT_DIR = f"/home/user/bi/intelligence_outputs/session_{SESSION_DATE}/csv"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────
print("=== LOADING DATA ===")

d365_raw = pd.read_excel("/home/user/bi/d365_data.xlsx")
d365_raw.columns = [c.strip() for c in d365_raw.columns]
d365_raw = d365_raw.rename(columns={
    "Output source file name: W11": "Company Name",
    "Ammount": "Amount",
    "Company/Issuer not cooperating": "INC_Flag"
})
print(f"D365 raw: {len(d365_raw):,} records, {d365_raw['Company Name'].nunique():,} unique companies")

inf_raw = pd.read_excel("/home/user/bi/infomerics.json.xlsx")
inf_raw.columns = [c.strip() for c in inf_raw.columns]
print(f"Infomerics raw: {len(inf_raw):,} records, {inf_raw['Company Name'].nunique():,} unique companies")

# ─────────────────────────────────────────
# PARSE DATES
# ─────────────────────────────────────────
def parse_date_d365(val):
    if pd.isna(val):
        return None
    val = str(val).strip()
    for fmt in ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]:
        try:
            return datetime.strptime(val[:10], fmt).date()
        except:
            pass
    return None

def parse_date_inf(val):
    if pd.isna(val):
        return None
    val = str(val).strip()
    # "July 18, 2025"
    try:
        return datetime.strptime(val, "%B %d, %Y").date()
    except:
        pass
    try:
        return datetime.strptime(val[:10], "%Y-%m-%d").date()
    except:
        pass
    return None

d365_raw["Rating Date"] = d365_raw["Date"].apply(parse_date_d365)
inf_raw["Rating Date"] = inf_raw["Date"].apply(parse_date_inf)

# ─────────────────────────────────────────
# INC FLAG
# ─────────────────────────────────────────
d365_raw["Is INC"] = d365_raw["INC_Flag"].astype(str).str.strip().str.upper().isin(["Y", "YES", "1", "TRUE"])
inf_raw["Is INC"] = inf_raw["Current Ratings"].str.contains(r"\bINC\b", case=False, na=False)

# ─────────────────────────────────────────
# URGENCY SCORING
# ─────────────────────────────────────────
def urgency(days):
    if pd.isna(days):
        return "UNKNOWN"
    if days >= 365:
        return "ULTRA HOT"
    elif days >= 180:
        return "HOT"
    elif days >= 90:
        return "MEDIUM"
    else:
        return "LOW"

d365_raw["Days Since Rating"] = d365_raw["Rating Date"].apply(
    lambda d: (TODAY - d).days if d else None)
d365_raw["Urgency"] = d365_raw["Days Since Rating"].apply(urgency)

inf_raw["Days Since Rating"] = inf_raw["Rating Date"].apply(
    lambda d: (TODAY - d).days if d else None)
inf_raw["Urgency"] = inf_raw["Days Since Rating"].apply(urgency)

# ─────────────────────────────────────────
# INSTRUMENT NORMALIZATION
# ─────────────────────────────────────────
def classify_instrument(txt):
    if pd.isna(txt):
        return "Unknown"
    t = str(txt).lower().strip()
    if "non-convertible debenture" in t or "ncd" in t or "non convertible debenture" in t:
        return "NCD"
    if "non-government debt" in t or "non government debt" in t:
        return "NCD"
    if "debenture" in t and "convertible" not in t:
        return "NCD"
    if "bond" in t and "term loan" not in t:
        return "Bond"
    if "term loan" in t or "term-loan" in t:
        return "Term Loan"
    if "bank guarantee" in t or " bg " in t or t == "bg":
        return "Bank Guarantee"
    if "letter of credit" in t or " lc " in t or t == "lc":
        return "Letter of Credit"
    if "commercial paper" in t or " cp " in t or t == "cp":
        return "Commercial Paper"
    if "non-fund" in t or "nfb" in t or "non fund" in t:
        return "Non-Fund Based"
    if "fund based" in t or "fund-based" in t:
        return "Fund Based"
    if "overdraft" in t or " od " in t:
        return "OD/CC"
    if "cash credit" in t or " cc " in t:
        return "OD/CC"
    if "working capital" in t:
        return "Working Capital"
    if "long term" in t or "longterm" in t or "lt bank" in t:
        return "Long Term Bank"
    if "short term" in t or "shortterm" in t or "st bank" in t:
        return "Short Term Bank"
    return "Other"

d365_raw["Instrument Type"] = d365_raw["Instrument"].apply(classify_instrument)
inf_raw["Instrument Type"] = inf_raw["Instruments"].apply(classify_instrument)

print(f"\nD365 NCD records: {(d365_raw['Instrument Type'] == 'NCD').sum():,}")
print(f"Infomerics NCD records: {(inf_raw['Instrument Type'] == 'NCD').sum():,}")

# ─────────────────────────────────────────
# SECTOR CLASSIFICATION
# ─────────────────────────────────────────
SECTOR_MAP = {
    "Steel": ["steel", "iron", "ferro", "sponge iron", "rolling mill", "wire rod", "pig iron", "billets", "casting", "foundry", "galvan", "induction furnac", "alloy"],
    "Agro/Food": ["agro", "food", "rice", "sugar", "dal", "pulse", "oil mill", "poultry", "flour", "grain", "seed", "cotton", "edible", "meat", "dairy", "cattle", "spice", "tea", "coffee", "jute", "kisan", "farm", "agri"],
    "Construction": ["construct", "infra", "build", "realty", "cement", "brick", "tile", "road", "highway", "civil", "housing", "real estate", "developer", "township"],
    "Textiles": ["textile", "cotton", "yarn", "fabric", "garment", "spinning", "weaving", "knitting", "dyeing", "thread", "apparel", "cloth", "fiber", "saree"],
    "Chemicals/Pharma": ["chem", "pharma", "drug", "medic", "lab", "biotech", "life science", "pigment", "dye", "resin", "polymer", "plastic", "rubber", "pesticide", "fertilizer", "agrochemical"],
    "BFSI": ["bank", "finance", "nbfc", "microfinance", "mfi", "insurance", "asset management", "leasing", "investment", "capital", "credit", "lending", "mortgage", "housing finance"],
    "Energy": ["energy", "power", "solar", "wind", "renew", "electri", "generat", "distribut", "thermal", "hydro", "coal", "gas", "petro", "oil", "fuel"],
    "Manufacturing": ["manufactur", "engineer", "industry", "product", "machin", "equipment", "tool", "pump", "valve", "bearing", "press", "forging", "wire", "cable"],
    "Automobiles": ["auto", "vehicle", "car", "truck", "bus", "tyre", "motor", "automobile", "ancillar"],
    "IT/Technology": ["software", "tech", "it ", "digital", "data", "system", "solution", "information", "telecom", "cloud"],
    "Healthcare": ["health", "hospital", "clinic", "medic", "diagnos", "nursing", "ayurved", "dental"],
    "Logistics": ["logistic", "transport", "warehousing", "shipping", "freight", "cargo", "supply chain", "courier"],
    "Hotels/Tourism": ["hotel", "resort", "travel", "tourism", "hospitality", "restaurant"],
    "Mining/Minerals": ["mining", "mineral", "granite", "marble", "stone", "quarry", "coal mine"],
    "Paper/Packaging": ["paper", "packaging", "carton", "corrugat", "print", "board"],
    "Media/Retail": ["media", "retail", "trade", "publish", "advertis", "entertain"],
    "Jewellery": ["jewel", "gem", "diamond", "gold", "silver"],
    "Trading/Exports": ["trading", "export", "import", "dealer", "wholesal", "distribut"],
}

def classify_sector(name):
    if pd.isna(name):
        return "Other"
    n = str(name).lower()
    for sector, keywords in SECTOR_MAP.items():
        if any(k in n for k in keywords):
            return sector
    return "Other"

d365_raw["Sector"] = d365_raw["Company Name"].apply(classify_sector)
inf_raw["Sector"] = inf_raw["Company Name"].apply(classify_sector)

# ─────────────────────────────────────────
# PARSE INFOMERICS AMOUNT
# ─────────────────────────────────────────
def parse_inf_amount(val):
    if pd.isna(val):
        return None
    s = str(val).lower().replace(",", "")
    import re
    m = re.search(r"[\d.]+", s)
    if m:
        try:
            v = float(m.group())
        except ValueError:
            return None
        if "lakh" in s:
            v = v / 100
        return round(v, 2)
    return None

inf_raw["Amount Cr"] = inf_raw["Size"].apply(parse_inf_amount)

print("\n=== DATA LOADED SUCCESSFULLY ===\n")

# ─────────────────────────────────────────
# TASK 1: NCD PRIORITY CALLING LIST
# ─────────────────────────────────────────
print("=" * 60)
print("TASK 1: NCD-FOCUSED CALLING LIST")
print("=" * 60)

# D365 NCD INC companies
d365_ncd = d365_raw[
    (d365_raw["Instrument Type"] == "NCD") &
    (d365_raw["Is INC"] == True)
].copy()

print(f"\nD365 NCD INC records: {len(d365_ncd):,}")
print(f"D365 NCD INC unique companies: {d365_ncd['Company Name'].nunique():,}")

# Get best record per company (most recent)
d365_ncd_best = d365_ncd.sort_values("Days Since Rating", ascending=False).groupby("Company Name").first().reset_index()

# Infomerics NCD INC companies
inf_ncd = inf_raw[
    (inf_raw["Instrument Type"] == "NCD") &
    (inf_raw["Is INC"] == True)
].copy()

print(f"\nInfomerics NCD INC records: {len(inf_ncd):,}")
print(f"Infomerics NCD INC unique companies: {inf_ncd['Company Name'].nunique():,}")

inf_ncd_best = inf_ncd.sort_values("Days Since Rating", ascending=False).groupby("Company Name").first().reset_index()

# Load the july2026 master for SEBI flag and multi-agency info
master = pd.read_csv("/home/user/bi/intelligence_outputs/session_20260623/csv/july2026_calling_master_20260623.csv")
print(f"\nJuly 2026 master: {len(master):,} rows")

# Build D365 NCD calling list
d365_ncd_out = pd.DataFrame()
d365_ncd_out["Company Name"] = d365_ncd_best["Company Name"]
d365_ncd_out["Current Rating Agency"] = d365_ncd_best["Agency"]
d365_ncd_out["Instrument"] = "NCD"
d365_ncd_out["Rating"] = d365_ncd_best["Rating"]
d365_ncd_out["Rating Date"] = d365_ncd_best["Rating Date"]
d365_ncd_out["Days Since Rating"] = d365_ncd_best["Days Since Rating"]
d365_ncd_out["Urgency"] = d365_ncd_best["Urgency"]
d365_ncd_out["Amount Cr"] = d365_ncd_best["Amount"]
d365_ncd_out["Sector"] = d365_ncd_best["Sector"]
d365_ncd_out["Source"] = "D365"

# Build Infomerics NCD calling list
inf_ncd_out = pd.DataFrame()
inf_ncd_out["Company Name"] = inf_ncd_best["Company Name"]
inf_ncd_out["Current Rating Agency"] = "Infomerics"
inf_ncd_out["Instrument"] = "NCD"
inf_ncd_out["Rating"] = inf_ncd_best["Current Ratings"]
inf_ncd_out["Rating Date"] = inf_ncd_best["Rating Date"]
inf_ncd_out["Days Since Rating"] = inf_ncd_best["Days Since Rating"]
inf_ncd_out["Urgency"] = inf_ncd_best["Urgency"]
inf_ncd_out["Amount Cr"] = inf_ncd_best["Amount Cr"]
inf_ncd_out["Sector"] = inf_ncd_best["Sector"]
inf_ncd_out["Source"] = "Infomerics"

# Combine and deduplicate
combined_ncd = pd.concat([d365_ncd_out, inf_ncd_out], ignore_index=True)
# Keep D365 record if company in both
combined_ncd = combined_ncd.sort_values(["Source", "Days Since Rating"], ascending=[True, False])
combined_ncd = combined_ncd.drop_duplicates(subset=["Company Name"], keep="first")

print(f"\nCombined NCD INC unique companies: {len(combined_ncd):,}")

# Merge master signals
master_signals = master[["Company Name", "Is Super Target T1", "Is Super Target T2",
                          "Is Three Way INC", "Multi Agency INC", "Priority Score"]].copy()
combined_ncd = combined_ncd.merge(master_signals, on="Company Name", how="left")

# SEBI note
combined_ncd["SEBI Note"] = "NCD requires SEBI debt rating license — confirm ACER has SEBI CRA registration before pitching"

def ncd_why_target(row):
    parts = []
    if str(row.get("Is Super Target T1", "")).lower() in ["true", "1", "yes"]:
        parts.append("TIER 1 Super Target")
    if str(row.get("Is Three Way INC", "")).lower() in ["true", "1", "yes"]:
        parts.append("3-way INC")
    if str(row.get("Multi Agency INC", "")).lower() in ["true", "1", "yes"]:
        parts.append("Multi-agency INC")
    urg = row.get("Urgency", "")
    if urg == "ULTRA HOT":
        parts.append(f"ULTRA HOT ({int(row['Days Since Rating'])} days overdue)")
    elif urg == "HOT":
        parts.append(f"HOT ({int(row['Days Since Rating'])} days)")
    if not parts:
        parts.append("NCD INC — SEBI debt revenue target")
    return " | ".join(parts)

def ncd_pitch(row):
    agency = row.get("Current Rating Agency", "the current agency")
    days = row.get("Days Since Rating", 0)
    urg = row.get("Urgency", "")
    if urg == "ULTRA HOT":
        return f"Your NCD rating at {agency} has been INC for {int(days)} days — you cannot use this instrument for fundraising. ACER can reactivate your SEBI-regulated NCD program within 30 days."
    elif urg == "HOT":
        return f"Your NCD rating at {agency} has been INC for {int(days)} days. ACER offers SEBI-registered NCD ratings — let us unlock your debenture program."
    else:
        return f"Your NCD rating at {agency} shows INC status. ACER provides SEBI-compliant NCD ratings — let us discuss activating your capital market access."

combined_ncd["Why Target"] = combined_ncd.apply(ncd_why_target, axis=1)
combined_ncd["ACER Pitch Script"] = combined_ncd.apply(ncd_pitch, axis=1)

# Sort by urgency priority
urgency_order = {"ULTRA HOT": 0, "HOT": 1, "MEDIUM": 2, "LOW": 3, "UNKNOWN": 4}
combined_ncd["Urgency Rank"] = combined_ncd["Urgency"].map(urgency_order).fillna(4)
combined_ncd = combined_ncd.sort_values(["Urgency Rank", "Days Since Rating"], ascending=[True, False])
combined_ncd = combined_ncd.drop(columns=["Urgency Rank"])

# Summary stats
urgency_counts = combined_ncd["Urgency"].value_counts()
print("\nNCD INC breakdown by urgency:")
for u in ["ULTRA HOT", "HOT", "MEDIUM", "LOW"]:
    print(f"  {u}: {urgency_counts.get(u, 0)}")

print("\nNCD INC breakdown by agency (D365):")
print(d365_ncd_best["Agency"].value_counts().head(8).to_string())

print("\nNCD INC breakdown by sector:")
print(combined_ncd["Sector"].value_counts().head(10).to_string())

# Save
out_path = f"{OUTPUT_DIR}/ncd_priority_calling_list_{SESSION_DATE}.csv"
combined_ncd.to_csv(out_path, index=False)
print(f"\nSaved: {out_path} ({len(combined_ncd):,} rows)")

# Also save ULTRA HOT + HOT only
ncd_hot = combined_ncd[combined_ncd["Urgency"].isin(["ULTRA HOT", "HOT"])]
out_path_hot = f"{OUTPUT_DIR}/ncd_hot_only_{SESSION_DATE}.csv"
ncd_hot.to_csv(out_path_hot, index=False)
print(f"Saved: {out_path_hot} ({len(ncd_hot):,} rows)")

# ─────────────────────────────────────────
# TASK 2: BRICKWORK 2026 TREND CHECK
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("TASK 2: BRICKWORK 2026 TREND CHECK")
print("=" * 60)

# Filter to Brickwork records
bw = d365_raw[d365_raw["Agency"].str.upper().str.contains("BRICKWORK|BRICKWK|BWR|BW ", na=False)].copy()
# Also try just "BW" alone or variations
bw_check = d365_raw["Agency"].dropna().unique()
bw_agencies = [a for a in bw_check if "brick" in str(a).lower() or "bwr" in str(a).lower()]
print(f"\nBrickwork agency name variants found: {bw_agencies}")

bw = d365_raw[d365_raw["Agency"].isin(bw_agencies)].copy()
print(f"Brickwork total records: {len(bw):,}")
print(f"Brickwork unique companies: {bw['Company Name'].nunique():,}")

if len(bw) == 0:
    # Fallback: search for any form of BW
    bw = d365_raw[d365_raw["Agency"].str.lower().str.contains("brickwork|bwr|bwraatings", na=False)].copy()
    print(f"Fallback Brickwork records: {len(bw):,}")

# Monthly analysis
bw["YM"] = bw["Rating Date"].apply(lambda d: f"{d.year}-{d.month:02d}" if d else None)
bw_monthly = bw.dropna(subset=["YM"]).copy()

monthly_stats = bw_monthly.groupby("YM").agg(
    Total_Records=("Is INC", "count"),
    INC_Records=("Is INC", "sum"),
    Unique_Companies=("Company Name", "nunique")
).reset_index()
monthly_stats["INC_Rate_Pct"] = (monthly_stats["INC_Records"] / monthly_stats["Total_Records"] * 100).round(1)
monthly_stats = monthly_stats.sort_values("YM")

# Filter to Jan 2025 onward
monthly_stats_recent = monthly_stats[monthly_stats["YM"] >= "2025-01"].copy()
print(f"\nBrickwork monthly trend (2025–2026):")
print(monthly_stats_recent.to_string(index=False))

# Trend analysis
if len(monthly_stats_recent) >= 3:
    early = monthly_stats_recent.head(6)["INC_Rate_Pct"].mean()
    late = monthly_stats_recent.tail(6)["INC_Rate_Pct"].mean()
    direction = "DECLINING" if late < early else "RISING"
    change = late - early
    print(f"\nBW INC rate — early 2025 avg: {early:.1f}% | recent avg: {late:.1f}% | Direction: {direction} ({change:+.1f}pp)")

# BW INC company list with urgency
bw_inc = bw[bw["Is INC"] == True].copy()
bw_inc_best = bw_inc.sort_values("Days Since Rating", ascending=False).groupby("Company Name").first().reset_index()
bw_inc_best["Sector"] = bw_inc_best["Company Name"].apply(classify_sector)
bw_inc_best["Instrument Type"] = bw_inc_best["Instrument"].apply(classify_instrument)

print(f"\nBW INC companies total: {len(bw_inc_best):,}")
bw_urgency = bw_inc_best["Urgency"].value_counts()
for u in ["ULTRA HOT", "HOT", "MEDIUM", "LOW"]:
    print(f"  {u}: {bw_urgency.get(u, 0)}")

# Check trend by year-half
bw_monthly["Half"] = bw_monthly["YM"].apply(lambda x: f"{x[:4]}-H1" if int(x[5:7]) <= 6 else f"{x[:4]}-H2")
half_stats = bw_monthly.groupby("Half").agg(
    Total=("Is INC", "count"),
    INC=("Is INC", "sum")
).reset_index()
half_stats["INC_Rate"] = (half_stats["INC"] / half_stats["Total"] * 100).round(1)
half_stats = half_stats[half_stats["Half"] >= "2025-H1"]
print(f"\nBrickwork INC rate by half-year:")
print(half_stats.to_string(index=False))

# Save monthly trend
out_trend = f"{OUTPUT_DIR}/brickwork_2026_trend_{SESSION_DATE}.csv"
monthly_stats.to_csv(out_trend, index=False)
print(f"\nSaved: {out_trend} ({len(monthly_stats):,} rows)")

# Save BW INC company list
bw_inc_out = pd.DataFrame({
    "Company Name": bw_inc_best["Company Name"],
    "Current Rating Agency": "Brickwork",
    "Instrument": bw_inc_best["Instrument"],
    "Instrument Type": bw_inc_best["Instrument Type"],
    "Rating": bw_inc_best["Rating"],
    "Rating Date": bw_inc_best["Rating Date"],
    "Days Since Rating": bw_inc_best["Days Since Rating"],
    "Urgency": bw_inc_best["Urgency"],
    "Amount Cr": bw_inc_best["Amount"],
    "Sector": bw_inc_best["Sector"],
    "Why Target": "Brickwork INC — displacement opportunity",
    "ACER Pitch": "Brickwork has INC'd your rating — ACER can replace with a fresh rating within 30 days"
})
out_bw_leads = f"{OUTPUT_DIR}/brickwork_inc_leads_{SESSION_DATE}.csv"
bw_inc_out.to_csv(out_bw_leads, index=False)
print(f"Saved: {out_bw_leads} ({len(bw_inc_out):,} rows)")

# ─────────────────────────────────────────
# TASK 3: 78 TIER 1 — SENIOR RM BRIEF
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("TASK 3: TIER 1 SUPER-TARGETS — SENIOR RM ASSIGNMENT BRIEF")
print("=" * 60)

# Load tier 1 super targets from the master (Is Super Target T1 flag)
tier1 = master[master["Is Super Target T1"].astype(str).str.lower().isin(["true", "1", "yes"])].copy()
print(f"\nTIER 1 companies in July master: {len(tier1):,}")

if len(tier1) == 0:
    # Try original super_targets file
    st_file = "/home/user/bi/intelligence_outputs/session_20260620/csv/super_targets_tier1_2_20260620.csv"
    st = pd.read_csv(st_file)
    tier1_names = st[st["Priority Tier"] == "TIER 1"]["Company Name"].unique()
    print(f"TIER 1 from super_targets file: {len(tier1_names):,} unique companies")
    tier1 = master[master["Company Name"].isin(tier1_names)].copy()
    print(f"Matched in master: {len(tier1):,}")
    if len(tier1) == 0:
        tier1 = st[st["Priority Tier"] == "TIER 1"].copy()
        print(f"Using original super_targets file directly: {len(tier1):,} rows")

print(f"\nFinal TIER 1 count: {len(tier1):,}")

# Merge with D365 data for richer profile
tier1_names = tier1["Company Name"].unique()
print(f"TIER 1 unique companies: {len(tier1_names):,}")

# Get all D365 records for tier1 companies
t1_d365 = d365_raw[d365_raw["Company Name"].isin(tier1_names)].copy()
t1_inf = inf_raw[inf_raw["Company Name"].isin(tier1_names)].copy()
print(f"D365 records for TIER 1: {len(t1_d365):,}")
print(f"Infomerics records for TIER 1: {len(t1_inf):,}")

# Build enriched profile per company
def build_tier1_profile(company_name, master_row, d365_records, inf_records):
    """Build one-page profile for a TIER 1 company."""

    # Get all agencies rating this company
    agencies = list(d365_records["Agency"].unique()) if len(d365_records) > 0 else []
    if len(inf_records) > 0:
        agencies.append("Infomerics")

    # INC at which agencies
    inc_agencies_d365 = list(d365_records[d365_records["Is INC"]]["Agency"].unique()) if len(d365_records) > 0 else []
    inc_agencies_inf = ["Infomerics"] if len(inf_records[inf_records["Is INC"]]) > 0 else []
    inc_agencies = inc_agencies_d365 + inc_agencies_inf

    # Total amount
    total_amt_d365 = pd.to_numeric(d365_records["Amount"], errors="coerce").dropna().sum() if len(d365_records) > 0 else 0
    total_amt_inf = pd.to_numeric(inf_records["Amount Cr"], errors="coerce").dropna().sum() if len(inf_records) > 0 else 0
    total_amt = float(total_amt_d365) + float(total_amt_inf)

    # Instruments
    instruments_d365 = list(d365_records["Instrument Type"].unique()) if len(d365_records) > 0 else []
    instruments_inf = list(inf_records["Instrument Type"].unique()) if len(inf_records) > 0 else []
    all_instruments = list(set(instruments_d365 + instruments_inf))

    # Most overdue rating
    max_days_d365 = d365_records[d365_records["Is INC"]]["Days Since Rating"].max() if len(d365_records[d365_records["Is INC"]]) > 0 else 0
    max_days_inf = inf_records[inf_records["Is INC"]]["Days Since Rating"].max() if len(inf_records[inf_records["Is INC"]]) > 0 else 0
    max_days = max(max_days_d365 or 0, max_days_inf or 0)

    # Urgency
    if max_days >= 365:
        urg = "ULTRA HOT"
    elif max_days >= 180:
        urg = "HOT"
    elif max_days >= 90:
        urg = "MEDIUM"
    else:
        urg = "LOW"

    # Sector
    sector = classify_sector(company_name)

    # Priority score
    score = master_row.get("Priority Score", 0) if isinstance(master_row, dict) else 0
    try:
        score = int(score)
    except:
        score = 5  # minimum for T1

    # Signals
    signals = []
    if urg in ["ULTRA HOT", "HOT"]:
        signals.append(f"Rating overdue {int(max_days)} days")
    if len(inc_agencies) > 1:
        signals.append(f"INC at {len(inc_agencies)} agencies ({', '.join(inc_agencies[:3])})")
    if len(agencies) > 1:
        signals.append(f"Rated by {len(agencies)} agencies simultaneously")

    is_t1 = master_row.get("Is Super Target T1", "") if isinstance(master_row, dict) else ""
    is_3way = master_row.get("Is Three Way INC", "") if isinstance(master_row, dict) else ""
    is_april = master_row.get("Is April2026 Dual INC", "") if isinstance(master_row, dict) else ""

    if str(is_3way).lower() in ["true", "1", "yes"]:
        signals.append("THREE-WAY INC (CRISIL+CARE+BW simultaneously)")
    if str(is_april).lower() in ["true", "1", "yes"]:
        signals.append("APRIL 2026 DUAL INC — July 18 funding deadline")

    # Pitch script
    if len(inc_agencies) >= 3:
        pitch = f"{company_name} is INC at {', '.join(inc_agencies[:3])} simultaneously — no functional credit rating anywhere. ACER's senior team can complete a fresh rating in 21 days, restoring capital market and bank credit access immediately."
    elif max_days >= 365:
        pitch = f"{company_name}'s rating has been INC for {int(max_days)} days at {', '.join(inc_agencies[:2] if inc_agencies else ['the current agency'])}. This is a year-long blackout from rated credit. ACER will fix this in 30 days — guaranteed SLA."
    elif len(inc_agencies) == 2:
        pitch = f"{company_name} is INC at both {inc_agencies[0]} and {inc_agencies[1]} — doubly locked out of rated credit. ACER's senior team offers a clean rating in 21 days with dedicated RM support."
    else:
        pitch = f"{company_name} is an ACER TIER 1 priority — {int(max_days)} days overdue rating at {', '.join(inc_agencies[:2] if inc_agencies else ['current agency'])}. Assign senior RM for direct CEO/CFO outreach."

    return {
        "Company Name": company_name,
        "Priority Tier": "TIER 1",
        "Priority Score": score,
        "Sector": sector,
        "All Rating Agencies": " | ".join(agencies) if agencies else "Infomerics",
        "INC At Agencies": " | ".join(inc_agencies) if inc_agencies else "Unknown",
        "Num Agencies INC": len(inc_agencies),
        "All Instruments": " | ".join(all_instruments),
        "Total Rated Amount Cr": round(total_amt, 1) if total_amt > 0 else None,
        "Max Days Overdue": int(max_days) if max_days else None,
        "Urgency": urg,
        "Signal 1": signals[0] if len(signals) > 0 else "",
        "Signal 2": signals[1] if len(signals) > 1 else "",
        "Signal 3": signals[2] if len(signals) > 2 else "",
        "Signal 4": signals[3] if len(signals) > 3 else "",
        "Senior RM Assigned": "",  # To be filled by ACER team
        "Target Contact": "CFO / Treasury Head",
        "Recommended First Call": "Week of 2026-06-30" if max_days >= 365 else "Week of 2026-07-07",
        "ACER Pitch Script": pitch
    }

# Build profiles for all TIER 1 companies
profiles = []
for company in tier1_names:
    d365_recs = t1_d365[t1_d365["Company Name"] == company]
    inf_recs = t1_inf[t1_inf["Company Name"] == company]

    # Get master row
    m_rows = tier1[tier1["Company Name"] == company]
    master_dict = m_rows.iloc[0].to_dict() if len(m_rows) > 0 else {}

    profile = build_tier1_profile(company, master_dict, d365_recs, inf_recs)
    profiles.append(profile)

profiles_df = pd.DataFrame(profiles)
# Sort by priority score descending, then days overdue descending
profiles_df["_sort1"] = profiles_df["Priority Score"].fillna(0).astype(float)
profiles_df["_sort2"] = profiles_df["Max Days Overdue"].fillna(0).astype(float)
profiles_df = profiles_df.sort_values(["_sort1", "_sort2"], ascending=[False, False])
profiles_df = profiles_df.drop(columns=["_sort1", "_sort2"])

print(f"\nTIER 1 profiles built: {len(profiles_df):,}")
print("\nTop 10 by priority score:")
top10 = profiles_df.head(10)[["Company Name", "Priority Score", "Max Days Overdue", "Urgency", "Sector", "INC At Agencies", "Total Rated Amount Cr"]]
print(top10.to_string(index=False))

# Sector breakdown of TIER 1
print("\nSector breakdown:")
print(profiles_df["Sector"].value_counts().to_string())

print("\nUrgency breakdown:")
print(profiles_df["Urgency"].value_counts().to_string())

print("\nAgencies INC breakdown (count of companies):")
print(profiles_df["Num Agencies INC"].value_counts().sort_index().to_string())

# Save
out_t1 = f"{OUTPUT_DIR}/tier1_senior_rm_assignments_{SESSION_DATE}.csv"
profiles_df.to_csv(out_t1, index=False)
print(f"\nSaved: {out_t1} ({len(profiles_df):,} rows)")

# ─────────────────────────────────────────
# FINAL SUMMARY
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("SESSION 26 — FINAL SUMMARY")
print("=" * 60)

print(f"""
TASK 1 — NCD PRIORITY CALLING LIST
  Total NCD INC companies: {len(combined_ncd):,}
  ULTRA HOT: {urgency_counts.get('ULTRA HOT', 0)}
  HOT: {urgency_counts.get('HOT', 0)}
  MEDIUM: {urgency_counts.get('MEDIUM', 0)}
  Files: ncd_priority_calling_list_{SESSION_DATE}.csv
         ncd_hot_only_{SESSION_DATE}.csv

TASK 2 — BRICKWORK 2026 TREND CHECK
  BW INC companies: {len(bw_inc_out):,}
  Direction: {"DECLINING" if len(monthly_stats_recent) > 0 and late < early else "STABLE/RISING"}
  Files: brickwork_2026_trend_{SESSION_DATE}.csv
         brickwork_inc_leads_{SESSION_DATE}.csv

TASK 3 — TIER 1 SENIOR RM BRIEF
  Companies profiled: {len(profiles_df):,}
  ULTRA HOT: {(profiles_df['Urgency'] == 'ULTRA HOT').sum()}
  HOT: {(profiles_df['Urgency'] == 'HOT').sum()}
  Files: tier1_senior_rm_assignments_{SESSION_DATE}.csv
""")

print("All outputs saved to:", OUTPUT_DIR)
