# 📈 Bluestock Mutual Fund Analytics Capstone

<div align="center">

![Bluestock](https://img.shields.io/badge/Bluestock-Fintech-blue?style=for-the-badge)

### End-to-End Mutual Fund Analytics using Python, SQLite, SQL & Power BI

**Summer Internship Capstone Project – Bluestock Fintech**

**Developed by:** Amrit Raj Gupta  
**B.E. Computer Science Engineering (7th Semester)**  
**Thapar Institute of Engineering and Technology**

</div>

---

# 📌 Project Overview

The **Bluestock Mutual Fund Analytics Capstone** is a comprehensive end-to-end data analytics project developed during my **Data Analytics Internship at Bluestock Fintech**.

The project transforms raw mutual fund datasets into actionable business insights using **Python, SQLite, SQL, and Power BI**. It covers the complete analytics lifecycle—from data ingestion and cleaning to advanced financial metrics and interactive dashboards.

This project demonstrates practical implementation of:

- Data Engineering
- Database Management
- Financial Analytics
- Risk Analysis
- Business Intelligence
- Data Visualization
- Dashboard Development

---

# 🎯 Project Objectives

- Develop an automated ETL pipeline for multiple mutual fund datasets.
- Build a normalized SQLite database for efficient querying.
- Perform comprehensive Exploratory Data Analysis (EDA).
- Calculate key financial performance metrics.
- Implement advanced risk and investor analytics.
- Design an interactive four-page Power BI dashboard.
- Generate actionable business insights and recommendations.

---

# 📊 Dataset Overview

| Metric | Value |
|---------|------:|
| Mutual Fund Schemes | 40 |
| Fund Houses | 10 |
| Historical NAV Records | 46,000+ |
| Investor Transactions | 32,778 |
| Unique Investors | 5,000 |
| Historical Coverage | 2022–2026 |

### Datasets Used

- Fund Master
- NAV History
- Monthly SIP Data
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

# 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Database | SQLite, SQL |
| Visualization | Matplotlib, Plotly |
| Dashboard | Power BI |
| IDE | VS Code, Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 🏗 Project Architecture

```text
Raw CSV Files
        │
        ▼
Python ETL Pipeline
        │
        ▼
Data Cleaning & Validation
        │
        ▼
SQLite Database
        │
        ▼
SQL Queries
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Performance Analytics
        │
        ▼
Advanced Analytics
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Insights
```

---

# 📁 Repository Structure

```text
Bluestock-Capstone/
│
├── Charts/
├── Dashboards/
│   ├── Bluestock Dashboard.pbix
│   ├── Dashboard.pdf
│   ├── Page1_IndustryOverview.png
│   ├── Page2_FundPerformance.png
│   ├── Page3_InvestorAnalytics.png
│   └── Page4_SIPMarketTrends.png
│
├── Data/
│   ├── Raw/
│   ├── Processed/
│   └── Database/
│
├── Notebooks/
│   ├── Data Cleaning.ipynb
│   ├── EDA Analysis.ipynb
│   ├── Performance Analytics.ipynb
│   └── Advanced Analytics.ipynb
│
├── PythonScripts/
│   ├── create_database.py
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── load_data.py
│   ├── multi_fund_fetch.py
│   ├── recommender.py
│   ├── run_query.py
│   └── verify_data.py
│
├── Reports/
├── SQL/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📈 Exploratory Data Analysis

The project includes comprehensive EDA to understand market trends, investor behaviour, and fund performance.

### Analyses Performed

- Daily NAV Trend Analysis
- AUM by Fund House
- Monthly SIP Inflow Trend
- Industry Folio Growth
- Category Inflow Heatmap
- Investor Age Distribution
- State-wise Investment Analysis
- Sector Allocation
- Correlation Matrix
- Investment Amount Distribution
- Rolling Sharpe Ratio
- Sector Concentration (HHI)

---

# 📊 Performance Analytics

Financial metrics were computed for all mutual fund schemes.

| Metric | Purpose |
|---------|----------|
| Annual Return | Yearly Performance |
| CAGR | Long-Term Growth |
| Sharpe Ratio | Risk-Adjusted Return |
| Sortino Ratio | Downside Risk |
| Alpha | Excess Return |
| Beta | Market Sensitivity |
| Maximum Drawdown | Worst Decline |
| Fund Score | Composite Ranking |

---

# 📉 Advanced Analytics

Implemented advanced financial and investor analytics:

- Historical Value at Risk (VaR)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector Concentration (HHI)
- Rule-Based Fund Recommendation Engine

---

# 📊 Power BI Dashboard

The project includes a **4-page interactive Power BI dashboard**.

### 📍 Page 1 – Industry Overview

- Total AUM
- SIP Inflows
- Industry Folios
- Number of Schemes
- AUM Trend
- Top Fund Houses

---

### 📍 Page 2 – Fund Performance

- Risk vs Return Scatter Plot
- Fund Scorecard
- NAV Trend
- Dynamic Filters

---

### 📍 Page 3 – Investor Analytics

- State-wise Transactions
- Investor Age Distribution
- Transaction Type Analysis
- Monthly Investment Trends

---

### 📍 Page 4 – SIP & Market Trends

- SIP vs NIFTY Comparison
- Category-wise Inflows
- Active SIP Accounts
- YoY Growth

---

# 💡 Key Business Insights

- Nippon India Mutual Fund and Kotak Mahindra Mutual Fund lead the sample in Assets Under Management.
- Mid-cap and Small-cap funds generated the highest CAGR during the analysis period.
- SIP inflows showed consistent year-on-year growth.
- Investors aged **26–35 years** represented the largest investor segment.
- Banking and IT dominated portfolio sector allocation.
- Rolling Sharpe Ratio revealed changing risk-adjusted performance over time.
- HHI analysis identified highly concentrated portfolios requiring diversification.

---

# 🚀 Future Enhancements

- Streamlit Web Application
- Monte Carlo Simulation
- Markowitz Portfolio Optimization
- Power BI Service Deployment
- Predictive SIP Churn Model
- Automated Email Reporting

---

# ▶️ How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/Amrit489/Bluestock-mutual-fund-analytics.git
cd Bluestock-Capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python PythonScripts/data_ingestion.py
```

### Fetch Live NAV

```bash
python PythonScripts/live_nav_fetch.py
```

### Open Dashboard

Open the Power BI dashboard:

```text
Dashboards/Bluestock Dashboard.pbix
```

---

# 📂 Project Deliverables

- ✅ ETL Pipeline
- ✅ SQLite Database
- ✅ SQL Queries
- ✅ EDA Notebook
- ✅ Performance Analytics Notebook
- ✅ Advanced Analytics Notebook
- ✅ Power BI Dashboard
- ✅ Final Report
- ✅ Presentation
- ✅ GitHub Repository

---

# 👨‍💻 Author

**Amrit Raj Gupta**

B.E. Computer Science Engineering (7th Semester)

Thapar Institute of Engineering and Technology

📧 Email: amritgupta489@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/amrit-raj-gupta/

💻 GitHub: https://github.com/Amrit489

---

# ⭐ Acknowledgement

This project was completed as part of the **Summer Data Analytics Internship at Bluestock Fintech**. It demonstrates the practical application of data engineering, financial analytics, business intelligence, and dashboard development using real-world mutual fund data.

---

<div align="center">

### ⭐ If you found this project interesting, consider giving it a Star!

</div>