from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")


def load_data():
    """
    Load all PMGSY cleaned CSV files from data/raw/,
    extract year from filename, and return a combined DataFrame.
    """
    csv_files = sorted(DATA_DIR.glob("MPR_*_Clean.csv"))

    if not csv_files:
        raise FileNotFoundError("No PMGSY CSV files found in data/raw/")

    dfs = []

    for file_path in csv_files:
        year = int(file_path.stem.split("_")[1])
        df = pd.read_csv(file_path)
        df["year"] = year
        dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)

    return combined_df