from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
RAW_FILE = DATA_DIR / "sample_companies.csv"
CLEANED_FILE = DATA_DIR / "cleaned_companies.csv"


def load_data(file_path):
    return pd.read_csv(file_path)


def clean_boolean_columns(df):
    boolean_columns = ["accounts_overdue", "confirmation_statement_overdue"]

    for column in boolean_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
            .str.lower()
            .map({"true": True, "false": False})
        )

    return df


def calculate_company_age(df):
    today = pd.Timestamp.today().normalize()

    df["incorporation_date"] = pd.to_datetime(
        df["incorporation_date"],
        errors="coerce"
    )

    df["company_age_years"] = (
        (today - df["incorporation_date"]).dt.days / 365.25
    ).round(1)

    return df


def assign_risk_category(row):
    status = str(row["company_status"]).lower()
    accounts_overdue = bool(row["accounts_overdue"])
    confirmation_overdue = bool(row["confirmation_statement_overdue"])

    if status in ["dissolved", "inactive"]:
        return "High Risk"

    if accounts_overdue and confirmation_overdue:
        return "High Risk"

    if accounts_overdue or confirmation_overdue:
        return "Medium Risk"

    return "Low Risk"


def create_risk_features(df):
    df["risk_category"] = df.apply(assign_risk_category, axis=1)
    df["is_high_risk"] = df["risk_category"].eq("High Risk")
    return df


def main():
    df = load_data(RAW_FILE)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = clean_boolean_columns(df)
    df = calculate_company_age(df)
    df = create_risk_features(df)

    df.to_csv(CLEANED_FILE, index=False)

    print("Total companies analysed:", len(df))
    print("\nCompany status breakdown:")
    print(df["company_status"].value_counts())

    print("\nRisk category breakdown:")
    print(df["risk_category"].value_counts())

    print(f"\nCleaned dataset saved to: {CLEANED_FILE}")


if __name__ == "__main__":
    main()
