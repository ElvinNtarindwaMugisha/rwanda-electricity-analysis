# Rwanda Electricity Access Trends (2009–2025)
 
A data analytics project examining Rwanda's electricity access expansion over 15 years — one of the fastest electrification journeys in Africa. This project covers national access trends, the urban–rural gap, off-grid solar growth, and the policy milestones that drove acceleration.
 
---
 
## Live Dashboard
 
Open `Rwanda_Electricity_Dashboard.html` in any browser to explore the interactive charts, or view the PDF report for the full written analysis.
 
---
 
## Project Structure
 
```
rwanda-electricity-analysis/
│
├── Rwanda_Electricity_Dashboard.html     # Interactive dashboard (open in browser)
├── Rwanda_Electricity_Access_Analysis.pdf # Full written report with tables & charts
├── rwanda_electricity_analysis.py        # Python analysis script
└── README.md
```
 
---
 
## Key Findings
 
- **75%** of Rwandan households had electricity access by 2024, up from just **6% in 2009**
- Rwanda ranked **3rd in Africa** for electrification speed between 2010 and 2020 (11th globally)
- **25%** of total household connectivity now comes from off-grid solar systems (~850,000 households)
- The **urban–rural gap** narrowed from 53 percentage points (2010) to 47pp (2022) as solar home system programmes scaled
- **2023** recorded the largest single-year gain ever: **+13.3 percentage points**
- The only recorded decline was **2020 (−1.4pp)**, linked to COVID-19 disruptions
- As of July 2025, total connectivity stands at **84.6%** (59.6% on-grid + 25% off-grid solar)
---
 
## Tools & Skills Demonstrated
 
| Area | Tools / Methods |
|---|---|
| Data wrangling | Python, pandas |
| Visualisation | matplotlib, Chart.js (HTML dashboard) |
| Statistical analysis | Year-on-year change, CAGR, trend analysis |
| Reporting | ReportLab (PDF generation) |
| Dashboard | HTML, CSS, JavaScript |
 
---
 
## Data Sources
 
All data used in this project is from official, publicly available sources:
 
- **World Bank** — SDG 7.1.1 Electrification Dataset (ESMAP / trackingsdg7.esmap.org)
- **Rwanda Energy Group (REG)** — Access Dashboard, July 2025 (reg.rw)
- **International Energy Agency (IEA)** — Rwanda Country Profile (iea.org/countries/rwanda)
- **Mugyenyi J. et al. (2024)** — *Rwanda's Path to Universal Electricity Access: Consumption Trends, Tariff Impact, and Challenges Ahead* — Columbia University QSEL / SSRN
- **World Bank Feature Report (April 2024)** — *Ingredients for Accelerating Universal Electricity Access: Lessons from Rwanda's Inspirational Approach*
---
 
## How to Run the Python Script
 
Make sure you have Python 3 installed, then:
 
```bash
pip install pandas matplotlib numpy
python rwanda_electricity_analysis.py
```
 
This will print a summary table to the terminal and save a chart image (`rwanda_electricity_trends.png`) to your working directory.
 
---
 
## About
 
This project collected electrification data from the World Bank SDG 7.1.1 dataset, Rwanda Energy Group (REG), and IEA country reports, then cleaned and structured it in Python using pandas. The analysis computed year-on-year percentage point changes, a 5-year CAGR, and tracked the urban–rural access gap across four reference years. A 3-panel matplotlib figure was generated covering the national trend, urban vs rural comparison, and annual growth rates. The findings were compiled into a structured PDF report using ReportLab, and an interactive HTML dashboard was built with Chart.js featuring four live charts, a data table, and a policy milestones timeline — all sourced from real official data.
 

