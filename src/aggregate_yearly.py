def aggregate_yearly(df):
    """
    Aggregates PMGSY metrics at state-year level.
    Returns a yearly time-series DataFrame.
    """
    agg_map = {
        "TN_PROPOSALS": "sum",
        "TN_LEN": "sum",
        "TN_AMT": "sum",
        "TU_PROPOSALS": "sum",
        "TU_LEN": "sum",
        "TU_AMT": "sum",
        "TOT_PROP": "sum",
        "TOT_LEN": "sum",
        "TOT_AMT": "sum",
        "CCN_PROPOSALS": "sum",
        "CCN_LEN": "sum",
        "CCN_AMT": "sum",
        "CCU_PROPOSALS": "sum",
        "CCU_LEN": "sum",
        "CCU_AMT": "sum",
        "CCTOT_PROP": "sum",
        "CCTOT_LEN": "sum",
        "CCTOT_AMT": "sum"
    }

    yearly_df = (
        df
        .groupby(["state", "year"], as_index=False)
        .agg(agg_map)
        .sort_values("year")
    )

    return yearly_df