def derive_indicators(yearly_df):
    """
    Derives completion and efficiency indicators from yearly aggregates.
    """
    yearly_df = yearly_df.copy()

    yearly_df["length_completion_rate"] = (
        yearly_df["CCTOT_LEN"] / yearly_df["TOT_LEN"]
    ) * 100

    yearly_df["proposal_completion_rate"] = (
        yearly_df["CCTOT_PROP"] / yearly_df["TOT_PROP"]
    ) * 100

    yearly_df["spend_realization_rate"] = (
        yearly_df["CCTOT_AMT"] / yearly_df["TOT_AMT"]
    ) * 100

    return yearly_df