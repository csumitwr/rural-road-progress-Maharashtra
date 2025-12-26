import pandas as pd


def convert_numeric(df, id_cols=None):
    """
    Converts all non-identifier columns to numeric.
    Commas are removed and invalid values are coerced to NaN.
    """
    if id_cols is None:
        id_cols = ["state", "sanction_year", "year"]

    metric_cols = [c for c in df.columns if c not in id_cols]

    for col in metric_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df