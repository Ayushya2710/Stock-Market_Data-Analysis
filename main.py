import os
from pathlib import Path

from file_reader import load_stock_data
from analyzer import yearly_min_max, detect_5_percent_variations
from graph import plot_daily_diff

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "output" / "reports"
GRAPHS_DIR = BASE_DIR / "output" / "graphs"

CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

def process_company_file(file_path: Path):
    company_name = file_path.stem

    print(f"{CYAN}Processing: {company_name}{RESET}")

    df = load_stock_data(file_path)

    yearly_min_max(company_name, df, REPORTS_DIR / "yearly_min_max.txt")
    detect_5_percent_variations(
        company_name,
        df,
        REPORTS_DIR / "price_variation.txt",
    )

    graph_path = plot_daily_diff(company_name, df, GRAPHS_DIR)

    print(f"{GREEN}Graph saved: {graph_path}{RESET}")


def main():
    print("=== Stock Market Analysis Started ===\n")

    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(GRAPHS_DIR, exist_ok=True)

    (REPORTS_DIR / "yearly_min_max.txt").write_text("")
    (REPORTS_DIR / "price_variation.txt").write_text("")

    data_files = [
        path
        for path in DATA_DIR.iterdir()
        if path.suffix.lower() in (".csv", ".xlsx")
    ]

    if not data_files:
        print("No CSV/XLSX files found under the data directory.")
        return

    for file_path in sorted(data_files):
        process_company_file(file_path)

    print("\n=== Analysis Completed Successfully ===")


if __name__ == "__main__":
    main()
