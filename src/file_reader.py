import warnings
from pathlib import Path

import pandas as pd


def load_stock_data(path):
    path = Path(path)

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        a = pd.to_datetime(df["Date"].astype(str), dayfirst=True, errors="coerce", infer_datetime_format=True)
        b = pd.to_datetime(df["Date"].astype(str), dayfirst=False, errors="coerce", infer_datetime_format=True)

    df["Date"] = a.where(a.notna(), b)
    df = df.dropna(subset=["Date"]).reset_index(drop=True)

    if "Close" not in df.columns and "Price" in df.columns:
        df = df.rename(columns={"Price": "Close"})
    if "Close" not in df.columns and "Adj Close" in df.columns:
        df = df.rename(columns={"Adj Close": "Close"})

    df["Close"] = (
        df["Close"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace(" ", "", regex=False)
    )

    df = df.dropna(subset=["Close"]).reset_index(drop=True)
    df["Close"] = df["Close"].astype(float)

    df = df.sort_values("Date").reset_index(drop=True)
    return df
