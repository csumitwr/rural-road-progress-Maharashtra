def validate_schema(df, reference_year=2025):
    """
    Validate column consistency across years using a reference year.
    Prints missing or extra columns for each year.
    """
    reference_cols = set(df[df["year"] == reference_year].columns)

    for year in sorted(df["year"].unique()):
        year_cols = set(df[df["year"] == year].columns)

        missing = reference_cols - year_cols
        extra = year_cols - reference_cols

        if missing or extra:
            print(f"\nSchema issues found for year {year}:")

            if missing:
                print(f"  Missing columns: {sorted(missing)}")

            if extra:
                print(f"  Extra columns: {sorted(extra)}")