def validate_totals(df, tol=1e-3):
    """
    Validates internal consistency of totals.
    Flags rows where component sums do not match reported totals.
    """
    checks = {
        "TOT_LEN_DIFF": df["TOT_LEN"] - (df["TN_LEN"] + df["TU_LEN"]),
        "TOT_AMT_DIFF": df["TOT_AMT"] - (df["TN_AMT"] + df["TU_AMT"]),
        "CCTOT_LEN_DIFF": df["CCTOT_LEN"] - (df["CCN_LEN"] + df["CCU_LEN"]),
        "CCTOT_AMT_DIFF": df["CCTOT_AMT"] - (df["CCN_AMT"] + df["CCU_AMT"]),
    }

    anomaly_mask = False

    for diff in checks.values():
        anomaly_mask |= diff.abs() > tol

    anomalies = df.loc[
        anomaly_mask,
        ["state", "sanction_year", "year"]
    ]

    if not anomalies.empty:
        print(f"\nTotal consistency issues found: {len(anomalies)} rows")

    return anomalies