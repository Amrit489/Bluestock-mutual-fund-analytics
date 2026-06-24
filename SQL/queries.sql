SELECT
    amfi_code,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    scheme_name,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT
    transaction_type,
    ROUND(AVG(amount_inr), 2) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT
    amfi_code,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

SELECT
    state,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

SELECT
    payment_mode,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY payment_mode
ORDER BY transaction_count DESC;

SELECT
    age_group,
    ROUND(AVG(annual_income_lakh), 2) AS avg_income
FROM fact_transactions
GROUP BY age_group
ORDER BY avg_income DESC;

SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_grade
ORDER BY fund_count DESC;