-- UK Company Risk Dashboard
-- SQL Business Questions and Analysis Queries

-- 1. Count companies by status
SELECT
    company_status,
    COUNT(*) AS company_count
FROM cleaned_companies
GROUP BY company_status
ORDER BY company_count DESC;

-- 2. Calculate percentage distribution by company status
SELECT
    company_status,
    COUNT(*) AS company_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage_share
FROM cleaned_companies
GROUP BY company_status
ORDER BY percentage_share DESC;

-- 3. Count companies by company type
SELECT
    company_type,
    COUNT(*) AS company_count
FROM cleaned_companies
GROUP BY company_type
ORDER BY company_count DESC;

-- 4. Analyse average company age by status
SELECT
    company_status,
    ROUND(AVG(company_age_years), 1) AS average_company_age
FROM cleaned_companies
GROUP BY company_status
ORDER BY average_company_age DESC;

-- 5. Count companies by risk category
SELECT
    risk_category,
    COUNT(*) AS company_count
FROM cleaned_companies
GROUP BY risk_category
ORDER BY company_count DESC;

-- 6. Identify higher-risk companies
SELECT
    company_number,
    company_name,
    company_status,
    company_age_years,
    accounts_overdue,
    confirmation_statement_overdue,
    risk_category
FROM cleaned_companies
WHERE risk_category = 'High Risk'
ORDER BY company_age_years DESC;

-- 7. Executive summary KPIs
SELECT
    COUNT(*) AS total_companies,
    SUM(CASE WHEN company_status = 'active' THEN 1 ELSE 0 END) AS active_companies,
    SUM(CASE WHEN company_status = 'dissolved' THEN 1 ELSE 0 END) AS dissolved_companies,
    SUM(CASE WHEN company_status = 'inactive' THEN 1 ELSE 0 END) AS inactive_companies,
    SUM(CASE WHEN risk_category = 'High Risk' THEN 1 ELSE 0 END) AS high_risk_companies
FROM cleaned_companies;
