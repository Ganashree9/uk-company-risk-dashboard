from pathlib import Path
import sqlite3
import pandas as pd

DATA_DIR = Path("data")
REPORTS_DIR = Path("reports")

CLEANED_FILE = DATA_DIR / "cleaned_companies.csv"
DB_FILE = DATA_DIR / "company_risk.db"
REPORT_FILE = REPORTS_DIR / "sql_results.md"


def run_query(connection, query):
    return pd.read_sql_query(query, connection)


def main():
    df = pd.read_csv(CLEANED_FILE)

    connection = sqlite3.connect(DB_FILE)
    df.to_sql("cleaned_companies", connection, if_exists="replace", index=False)

    queries = {
        "Company Status Breakdown": """
            SELECT
                company_status,
                COUNT(*) AS company_count
            FROM cleaned_companies
            GROUP BY company_status
            ORDER BY company_count DESC;
        """,

        "Risk Category Breakdown": """
            SELECT
                risk_category,
                COUNT(*) AS company_count
            FROM cleaned_companies
            GROUP BY risk_category
            ORDER BY company_count DESC;
        """,

        "Average Company Age by Status": """
            SELECT
                company_status,
                ROUND(AVG(company_age_years), 1) AS average_company_age
            FROM cleaned_companies
            GROUP BY company_status
            ORDER BY average_company_age DESC;
        """,

        "Executive Summary KPIs": """
            SELECT
                COUNT(*) AS total_companies,
                SUM(CASE WHEN company_status = 'active' THEN 1 ELSE 0 END) AS active_companies,
                SUM(CASE WHEN company_status = 'dissolved' THEN 1 ELSE 0 END) AS dissolved_companies,
                SUM(CASE WHEN company_status = 'inactive' THEN 1 ELSE 0 END) AS inactive_companies,
                SUM(CASE WHEN risk_category = 'High Risk' THEN 1 ELSE 0 END) AS high_risk_companies
            FROM cleaned_companies;
        """
    }

    report_lines = ["# SQL Analysis Results\n"]

    for title, query in queries.items():
        result = run_query(connection, query)

        print(f"\n{title}")
        print(result)

        report_lines.append(f"## {title}\n")
        report_lines.append(result.to_markdown(index=False))
        report_lines.append("\n")

    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text("\n".join(report_lines), encoding="utf-8")

    connection.close()

    print(f"\nSQL results report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
