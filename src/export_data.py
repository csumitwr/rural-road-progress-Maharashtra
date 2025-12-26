from pathlib import Path


EXPORT_DIR = Path("data/exports")


def export_yearly_data(yearly_df, filename="pmgsy_yearly_summary.csv"):
    """
    Exports yearly aggregated PMGSY data to CSV.
    """
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = EXPORT_DIR / filename
    yearly_df.to_csv(output_path, index=False)


def export_sanction_year_data(sanction_year_df, filename="pmgsy_sanction_year_summary.csv"):
    """
    Exports sanction-year aggregated PMGSY data to CSV.
    """
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = EXPORT_DIR / filename
    sanction_year_df.to_csv(output_path, index=False)