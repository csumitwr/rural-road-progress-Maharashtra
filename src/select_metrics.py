def select_metrics(df):
    """
    Selects only the metrics required for analysis.
    Drops auxiliary and administrative columns.
    """
    id_cols = ["state", "sanction_year", "year"]

    metric_cols = [
        # Sanctioned works
        "TN_PROPOSALS", "TN_LEN", "TN_AMT",
        "TU_PROPOSALS", "TU_LEN", "TU_AMT",
        "TOT_PROP", "TOT_LEN", "TOT_AMT",

        # Completed works
        "CCN_PROPOSALS", "CCN_LEN", "CCN_AMT",
        "CCU_PROPOSALS", "CCU_LEN", "CCU_AMT",
        "CCTOT_PROP", "CCTOT_LEN", "CCTOT_AMT"
    ]

    return df[id_cols + metric_cols]