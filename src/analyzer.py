def _find_prev_trading_index(df, current_index):


    curr_date = df.loc[current_index, "Date"]

    for prev_index in range(current_index - 1, -1, -1):
        prev_date = df.loc[prev_index, "Date"]

        if prev_date.weekday() > 4:
            continue

        delta_days = (curr_date - prev_date).days

        if delta_days <= 3:
            return prev_index

        break

    return None


def yearly_min_max(company_name, df, out_file):
    """
    Writes a clean formatted yearly min/max price report.
    """

    df["Year"] = df["Date"].dt.year

    header = (
        f"\n========== {company_name.upper()} ==========\n"
        f"{'YEAR':<6} {'MIN':<10} {'MIN DATE':<12} "
        f"{'MAX':<10} {'MAX DATE':<12}\n"
        f"{'-'*60}\n"
    )

    lines = [header]

    for year, group in df.groupby("Year"):
        min_row = group.loc[group["Close"].idxmin()]
        max_row = group.loc[group["Close"].idxmax()]

        line = (
            f"{year:<6} "
            f"{min_row['Close']:<10.2f} {str(min_row['Date'].date()):<12} "
            f"{max_row['Close']:<10.2f} {str(max_row['Date'].date()):<12}"
        )

        lines.append(line)

    with open(out_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def detect_5_percent_variations(company_name, df, out_file):
    """
    Writes a clean formatted report for all ±5% daily moves.
    """

    header = (
        f"\n========== {company_name.upper()} (5% MOVES) ==========\n"
        f"{'DATE':<12} {'%CHG':<7} {'PREV':<10} {'CURR':<10}\n"
        f"{'-'*45}\n"
    )

    lines = [header]

    for i in range(1, len(df)):
        prev_index = _find_prev_trading_index(df, i)

        if prev_index is None:
            continue

        prev_close = df.loc[prev_index, "Close"]
        curr_close = df.loc[i, "Close"]

        if prev_close == 0:
            continue

        pct = ((curr_close - prev_close) / prev_close) * 100

        if abs(pct) >= 5:
            line = (
                f"{str(df.loc[i,'Date'].date()):<12} "
                f"{pct:<7.2f} "
                f"{prev_close:<10.2f} "
                f"{curr_close:<10.2f}"
            )
            lines.append(line)

    with open(out_file, "a") as f:
        f.write("\n".join(lines) + "\n")
