# Bluestock Mutual Fund Analytics Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique fund identifier |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| plan | TEXT | Direct or Regular plan |
| expense_ratio_pct | REAL | Expense ratio percentage |
| risk_grade | TEXT | Risk level of fund |

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| nav_date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Fund identifier |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | T30/B30 classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | UPI, Cheque, Net Banking, etc. |
| kyc_status | TEXT | KYC verification status |

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year return (%) |
| return_5yr_pct | REAL | 5-year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return (%) |
| alpha | REAL | Alpha metric |
| beta | REAL | Beta metric |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annualized volatility |
| max_drawdown_pct | REAL | Maximum drawdown |
| aum_crore | REAL | Assets Under Management (₹ Crore) |
| morningstar_rating | INTEGER | Morningstar rating |