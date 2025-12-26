def clean_identifiers(df):
    """
    Cleans and standardizes identifier columns.
    - Maps LOCATION_NAME to sanction_year
    - Adds state column
    - Drops unused identifier fields
    """

    if "LOCATION_NAME" not in df.columns:
        raise KeyError("Expected column 'LOCATION_NAME' not found")

    # Rename LOCATION_NAME → sanction_year
    df = df.rename(columns={"LOCATION_NAME": "sanction_year"})

    # Add explicit state column
    df["state"] = "MAHARASHTRA"

    # Clean text formatting
    df["sanction_year"] = (
        df["sanction_year"]
        .astype(str)
        .str.strip()
    )

    # Drop unused identifier column if present
    if "IMS_YEAR" in df.columns:
        df = df.drop(columns=["IMS_YEAR"])

    return df