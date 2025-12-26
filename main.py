from src.load_data import load_data
from src.validate_schema import validate_schema
from src.fix_missing_columns import fix_missing_columns
from src.clean_identifiers import clean_identifiers
from src.convert_numeric import convert_numeric
from src.validate_totals import validate_totals
from src.select_metrics import select_metrics
from src.aggregate_yearly import aggregate_yearly
from src.derive_indicators import derive_indicators
from src.export_data import (
    export_yearly_data,
    export_sanction_year_data
)
from src.visualize_dashboard import (
    plot_sanctioned_vs_completed,
    plot_length_completion_rate,
    plot_spend_realization_rate,
    plot_completion_by_sanction_year
)


def main():
    # Load data
    df = load_data()

    # Validate schema (non-destructive)
    validate_schema(df)

    # Fix known missing columns
    df = fix_missing_columns(df)

    # Clean identifiers
    df = clean_identifiers(df)

    # Convert metrics to numeric
    df = convert_numeric(df)

    # Validate internal totals (diagnostic only)
    anomalies = validate_totals(df)
    if not anomalies.empty:
        print("Note: Some total inconsistencies detected (expected for government data).")

    # Select analysis metrics
    analysis_df = select_metrics(df)

    # Aggregate to yearly level
    yearly_df = aggregate_yearly(analysis_df)

    # Derive performance indicators
    yearly_df = derive_indicators(yearly_df)

    # Prepare sanction-year aggregation for dashboard
    sanction_year_df = (
        analysis_df
        .groupby("sanction_year", as_index=False)
        .agg({
            "TOT_LEN": "sum",
            "CCTOT_LEN": "sum",
            "TOT_AMT": "sum",
            "CCTOT_AMT": "sum"
        })
    )

    sanction_year_df["length_completion_rate"] = (
        sanction_year_df["CCTOT_LEN"] / sanction_year_df["TOT_LEN"]
    ) * 100

    sanction_year_df["spend_realization_rate"] = (
        sanction_year_df["CCTOT_AMT"] / sanction_year_df["TOT_AMT"]
    ) * 100

    # Export final datasets
    export_yearly_data(yearly_df)
    export_sanction_year_data(sanction_year_df)

    # Visualize dashboard
    plot_sanctioned_vs_completed(yearly_df)
    plot_length_completion_rate(yearly_df)
    plot_spend_realization_rate(yearly_df)
    plot_completion_by_sanction_year(sanction_year_df)


if __name__ == "__main__":
    main()