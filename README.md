# UK Company Risk Dashboard

A data analyst portfolio project using **Python, SQL and Power BI** to analyse UK company records, identify risk indicators and present executive-level dashboard insights.

## Dashboard Preview

![UK Company Risk Dashboard](screenshots/dashboard_overview.png)

## Project Overview

This project analyses UK company records to identify risk indicators, company status patterns and business-health signals.

The goal is to demonstrate how public company data can be cleaned, transformed and visualised into a decision-ready dashboard for finance, banking, operations and risk teams.

## Key Results

- Analysed 15 UK company records.
- Identified 10 active companies, 3 dissolved companies and 2 inactive companies.
- Classified 5 companies as High Risk based on company status and overdue filing indicators.
- Built a Power BI dashboard showing company status, risk category breakdown and high-risk company details.

## Business Problem

Finance and operations teams often need to quickly understand which companies may require closer review based on company status, filing behaviour, company age and other risk indicators.

This project answers:

- Which companies show higher-risk characteristics?
- How many companies are active, dissolved or inactive?
- Which companies should be prioritised for review?
- What summary KPIs should appear in an executive dashboard?

## Tools Used

- Python
- Pandas
- SQL
- SQLite
- Power BI
- GitHub

## Project Workflow

1. Created a sample UK company dataset.
2. Cleaned and transformed the data using Python.
3. Created risk-category logic based on company status and overdue filing indicators.
4. Exported a cleaned dataset for analysis.
5. Ran SQL queries to generate business insights.
6. Built a Power BI dashboard for executive reporting.
7. Added dashboard screenshot and documentation to GitHub.

## Risk Logic

Companies were classified as **High Risk** if:

- Company status was dissolved or inactive.
- Accounts were overdue.
- Confirmation statement was overdue.

Companies with fewer warning signs were classified as Medium Risk or Low Risk.

## Repository Structure

```text
data/
  sample_companies.csv
  cleaned_companies.csv

notebooks/
  01_company_risk_analysis.py
  02_sql_analysis.py

sql/
  business_questions.sql

reports/
  initial_findings.md
  sql_results.md
  business_summary.md
  project_plan.md

dashboard/
  uk_company_risk_dashboard.pbix
  dashboard_plan.md

screenshots/
  dashboard_overview.png

How to Reproduce the Analysis

This project includes Python scripts that clean the raw dataset and generate SQL analysis results.

To run the project locally:

Install the required Python packages:
pip install -r requirements.txt
Run the data-cleaning script:
python notebooks/01_company_risk_analysis.py

This creates the cleaned dataset:

data/cleaned_companies.csv
Run the SQL analysis script:
python notebooks/02_sql_analysis.py

This creates the SQL results report:

reports/sql_results.md
Dashboard File

The Power BI dashboard file is available here:

dashboard/uk_company_risk_dashboard.pbix
Skills Demonstrated
Data cleaning
Data transformation
Risk classification
SQL analysis
KPI reporting
Power BI dashboarding
Business insight generation
GitHub project documentation
Future Improvements
Replace the sample dataset with a larger Companies House dataset.
Add sector-level risk analysis.
Add region-level company risk trends.
Add more dashboard pages for company age, SIC code and filing behaviour.

Commit message:

```text
Polish README for portfolio presentation
