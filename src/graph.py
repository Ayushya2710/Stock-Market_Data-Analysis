import os
from pathlib import Path

import matplotlib.pyplot as plt


def plot_daily_diff(company_name, df, out_folder):
    out_folder = Path(out_folder)

    df = df.sort_values("Date").reset_index(drop=True)
    df["Diff"] = df["Close"].diff()

    os.makedirs(out_folder, exist_ok=True)

    plt.figure(figsize=(12, 5))
    plt.plot(df["Date"], df["Diff"], linewidth=1.5)
    plt.title(f"Daily Price Change - {company_name.upper()}", fontsize=14, fontweight="bold")
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price Change (₹)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    output_path = out_folder / f"{company_name}.png"
    plt.savefig(output_path, dpi=160)
    plt.close()

    return output_path
