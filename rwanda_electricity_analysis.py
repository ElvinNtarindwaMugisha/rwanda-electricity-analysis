"""
Rwanda Electricity Access Trends — Data Analysis
=================================================
Author: Fabrice (Data Analyst Intern Applicant)
Personal data analytics project
Sources:
  - World Bank SDG 7.1.1 Electrification Dataset
  - Rwanda Energy Group (REG) official reports
  - IEA Country Profile: Rwanda
  - Mugyenyi et al. (2024) "Rwanda's Path to Universal Electricity Access"
  - World Bank Feature Report, April 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "--",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

GREEN  = "#1D9E75"
BLUE   = "#185FA5"
AMBER  = "#EF9F27"
RED    = "#E24B4A"
GRAY   = "#888780"

# ─────────────────────────────────────────────────────────────────────────────
# 1.  DATA
# ─────────────────────────────────────────────────────────────────────────────

national = pd.DataFrame({
    "year":   [2009, 2010, 2011, 2012, 2013, 2014, 2015,
                2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "access": [6.0,  9.8, 10.0, 10.8, 11.5, 19.4, 26.0,
               34.0, 39.2, 43.0, 46.6, 45.2, 48.7, 50.6, 63.9],
})

urban_rural = pd.DataFrame({
    "year":  [2010, 2014, 2018, 2022],
    "urban": [58.0, 68.0, 75.0, 87.0],
    "rural": [5.0,  12.0, 17.0, 40.0],
})

connectivity_2025 = pd.Series(
    {"On-grid": 59.6, "Off-grid solar": 25.0, "No access": 15.4},
    name="July 2025"
)

milestones = {
    2008: "EDPRS I launched; eSWAp with World Bank",
    2013: "EDPRS II; REG / EDCL established",
    2018: "Off-grid Solar SHS mandate; mini-grid guidelines",
    2020: "3rd fastest electrification in Africa (2010–2020)",
    2024: "75% household access achieved",
}

# ─────────────────────────────────────────────────────────────────────────────
# 2.  ANALYSIS SUMMARY
# ─────────────────────────────────────────────────────────────────────────────

national["yoy_pp"] = national["access"].diff().round(1)
national["5yr_cagr"] = np.nan
for i in range(5, len(national)):
    start = national.loc[i-5, "access"] / 100
    end   = national.loc[i,   "access"] / 100
    cagr  = (end / start) ** (1/5) - 1
    national.loc[i, "5yr_cagr"] = round(cagr * 100, 2)

print("=" * 55)
print("RWANDA ELECTRICITY ACCESS — SUMMARY STATISTICS")
print("=" * 55)
print(national[["year", "access", "yoy_pp"]].to_string(index=False))
print(f"\nTotal gain 2009→2023 : +{national['access'].iloc[-1] - national['access'].iloc[0]:.1f} pp")
print(f"Peak YoY growth      : +{national['yoy_pp'].max():.1f} pp ({int(national.loc[national['yoy_pp'].idxmax(),'year'])})")
print(f"Only negative year   : 2020 ({national.loc[national['yoy_pp'].idxmin(),'yoy_pp']} pp — COVID-19 impact)")
print(f"\nUrban–rural gap:")
for _, row in urban_rural.iterrows():
    print(f"  {int(row.year)}: Urban {row.urban}% | Rural {row.rural}% | Gap {row.urban - row.rural:.0f} pp")

# ─────────────────────────────────────────────────────────────────────────────
# 3.  FIGURE  (2×2 dashboard)
# ─────────────────────────────────────────────────────────────────────────────

fig = plt.figure(figsize=(14, 10))
fig.suptitle(
    "Rwanda Electricity Access Trends  |  2009 – 2024",
    fontsize=16, fontweight="bold", y=0.98, color="#2C2C2A"
)
fig.text(0.5, 0.955, "Sources: World Bank · REG · IEA · Mugyenyi et al. (2024)",
         ha="center", fontsize=9, color=GRAY)

gs = fig.add_gridspec(2, 2, hspace=0.40, wspace=0.32,
                      left=0.07, right=0.97, top=0.93, bottom=0.07)

# ── Panel A: National trend ──────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(national["year"], national["access"],
         color=GREEN, linewidth=2.5, marker="o", markersize=5, zorder=3)
ax1.fill_between(national["year"], national["access"],
                 color=GREEN, alpha=0.10)

for yr, label in milestones.items():
    val = national.loc[national["year"] == yr, "access"]
    if not val.empty:
        ax1.axvline(yr, color=AMBER, linewidth=1.0, linestyle=":", alpha=0.7)
        ax1.text(yr + 0.15, 5, str(yr), fontsize=8, color=AMBER, va="bottom")

ax1.set_title("A  National electricity access rate (%)", fontsize=11, loc="left", color="#2C2C2A")
ax1.set_ylabel("% of population", fontsize=9, color=GRAY)
ax1.set_ylim(0, 100)
ax1.set_xlim(2008.5, 2023.5)
ax1.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
ax1.tick_params(labelsize=9)

for y, a in zip(national["year"], national["access"]):
    if y in [2009, 2014, 2018, 2020, 2022, 2023]:
        ax1.annotate(f"{a}%", (y, a), textcoords="offset points",
                     xytext=(0, 10), ha="center", fontsize=8, color=GREEN)

ms_patch = mpatches.Patch(color=AMBER, alpha=0.7, label="Policy milestone")
ax1.legend(handles=[ms_patch], fontsize=9, loc="upper left")

# ── Panel B: Urban vs Rural ──────────────────────────────────────────────────
ax2 = fig.add_subplot(gs[1, 0])
x  = np.arange(len(urban_rural))
w  = 0.32
ax2.bar(x - w/2, urban_rural["urban"], width=w, color=BLUE, label="Urban", alpha=0.88)
ax2.bar(x + w/2, urban_rural["rural"], width=w, color=GREEN, label="Rural", alpha=0.88)

for i, row in urban_rural.iterrows():
    ax2.text(i - w/2, row["urban"] + 1.5, f"{row['urban']:.0f}%", ha="center", fontsize=8, color=BLUE)
    ax2.text(i + w/2, row["rural"] + 1.5, f"{row['rural']:.0f}%", ha="center", fontsize=8, color=GREEN)

ax2.set_xticks(x)
ax2.set_xticklabels(urban_rural["year"].astype(int), fontsize=9)
ax2.set_ylim(0, 105)
ax2.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
ax2.set_title("B  Urban vs rural access gap", fontsize=11, loc="left", color="#2C2C2A")
ax2.legend(fontsize=9)
ax2.tick_params(labelsize=9)

# ── Panel C: YoY growth bars ─────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[1, 1])
yoy = national.dropna(subset=["yoy_pp"]).copy()
colors = [RED if v < 0 else GREEN for v in yoy["yoy_pp"]]
bars = ax3.bar(yoy["year"], yoy["yoy_pp"], color=colors, alpha=0.85, width=0.7)

for bar, val in zip(bars, yoy["yoy_pp"]):
    offset = 0.3 if val >= 0 else -1.2
    ax3.text(bar.get_x() + bar.get_width()/2, val + offset,
             f"+{val:.1f}" if val > 0 else f"{val:.1f}",
             ha="center", fontsize=7.5, color=GRAY)

ax3.axhline(0, color=GRAY, linewidth=0.6)
ax3.set_title("C  Year-on-year change (pp)", fontsize=11, loc="left", color="#2C2C2A")
ax3.set_ylabel("Percentage points", fontsize=9, color=GRAY)
ax3.tick_params(axis="x", rotation=45, labelsize=8)
ax3.tick_params(axis="y", labelsize=9)

up_patch   = mpatches.Patch(color=GREEN, label="Growth")
down_patch = mpatches.Patch(color=RED,   label="Decline")
ax3.legend(handles=[up_patch, down_patch], fontsize=9)

plt.savefig("/home/claude/rwanda_electricity_trends.png", dpi=150, bbox_inches="tight")
print("\n[✓] Chart saved to rwanda_electricity_trends.png")
plt.close()
