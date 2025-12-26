import numpy as np


def fix_missing_columns(df, reference_year=2025):
    """
    Ensures all years have the same columns as the reference year.
    Missing columns are added with NaN values.
    """
    reference_cols = set(df[df["year"] == reference_year].columns)

    for year in sorted(df["year"].unique()):
        year_mask = df["year"] == year
        year_cols = set(df.loc[year_mask].columns)

        missing = reference_cols - year_cols

        for col in missing:
            df.loc[year_mask, col] = np.nan

    return df