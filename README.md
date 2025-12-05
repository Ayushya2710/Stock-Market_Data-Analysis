## Dataset

- Folder: `data/`
- Format: CSVs (`Date, Open, High, Low, Close, Adj Close, Volume`)
- Coverage: 2015‑01‑01 to 2025‑12‑11 (ticker dependent)
- Companies: Bajaj Finance, HDFC Bank, ICICI Bank, IHTL, INBA, Infosys, NEST, Reliance, SBI, Tata Motors

## Requirements

- Python 3.10+
- Git
- pip
- Dependencies listed in `requirements.txt`:
  - `pandas`
  - `matplotlib`
  - `openpyxl`

## Setup

```powershell
python -m venv venv
```

3. **Activate the environment**

   - Windows (PowerShell):

     ```powershell
     venv\Scripts\activate
     ```

   - macOS / Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install all dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the analysis script**

   ```bash
   python src/main.py
   ```

6. **Review the generated outputs**

   - `output/reports/yearly_min_max.txt` — yearly minimum/maximum closing prices with the dates they occurred.
   - `output/reports/price_variation.txt` — every trading day with a ±5 % (or greater) close relative to the prior valid trading day.
   - `output/graphs/<company>.png` — daily close-difference plots per company.

   The script resets both report files before each run and overwrites any existing graphs, so you always see results from the latest execution. The folders are tracked with `.gitkeep` placeholders, while the generated artifacts are ignored via `.gitignore`.

## Project structure

```
├─ data/                    # Input CSVs
├─ output/
│  ├─ graphs/               # Generated plots (png)
│  └─ reports/              # Text reports
├─ src/
│  ├─ main.py               # Entry point
│  ├─ analyzer.py           # Reporting logic
│  ├─ file_reader.py        # CSV ingestion / cleaning
│  └─ graph.py              # Plot generation
├─ requirements.txt
└─ README.md
```

