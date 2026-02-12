# Copyright (c) 2026 Minh Tran
# License: MIT

from datetime import datetime, date
from pathlib import Path
from typing import List, Dict


WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def read_data(filename: str) -> List[List]:
    """
    Reads a CSV file and returns rows as structured data.

    Each row contains:
    [date, consumption_v1, consumption_v2, consumption_v3,
     production_v1, production_v2, production_v3]
    """
    rows = []

    with open(filename, "r", encoding="utf-8") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(";")

            dt = datetime.fromisoformat(parts[0])
            day = dt.date()

            consumption = [int(parts[1]), int(parts[2]), int(parts[3])]
            production = [int(parts[4]), int(parts[5]), int(parts[6])]

            rows.append([day, consumption, production])

    return rows


def calculate_daily_totals(rows: List[List]) -> Dict[date, Dict[str, List[int]]]:
    """
    Calculates daily totals for consumption and production.

    Returns dictionary:
    {
        date: {
            "consumption": [v1, v2, v3],
            "production": [v1, v2, v3]
        }
    }
    """
    daily_totals: Dict[date, Dict[str, List[int]]] = {}

    for row in rows:
        day, consumption, production = row

        if day not in daily_totals:
            daily_totals[day] = {
                "consumption": [0, 0, 0],
                "production": [0, 0, 0],
            }

        for i in range(3):
            daily_totals[day]["consumption"][i] += consumption[i]
            daily_totals[day]["production"][i] += production[i]

    return daily_totals


def format_kwh(value_wh: int) -> str:
    """
    Converts Wh to kWh and formats using Finnish decimal comma.
    """
    value_kwh = value_wh / 1000
    return f"{value_kwh:.2f}".replace(".", ",")


def format_week_report(week_number: int, daily_totals: Dict[date, Dict[str, List[int]]]) -> str:
    """
    Formats one week's data into a report section string.
    """
    lines = []

    lines.append(f"Week {week_number} electricity consumption and production (kWh, by phase)")
    lines.append("")
    lines.append("Day      Date           Consumption [kWh]            Production [kWh]")
    lines.append("                        v1      v2      v3           v1      v2      v3")
    lines.append("-" * 75)

    for day in sorted(daily_totals.keys()):
        weekday = WEEKDAYS[day.weekday()]
        date_str = day.strftime("%d.%m.%Y")

        cons = daily_totals[day]["consumption"]
        prod = daily_totals[day]["production"]

        cons_str = [format_kwh(v) for v in cons]
        prod_str = [format_kwh(v) for v in prod]

        line = (
            f"{weekday:<9} {date_str:<14} "
            f"{cons_str[0]:>7} {cons_str[1]:>7} {cons_str[2]:>7}     "
            f"{prod_str[0]:>7} {prod_str[1]:>7} {prod_str[2]:>7}"
        )

        lines.append(line)

    lines.append("\n")
    return "\n".join(lines)


def write_report(content: str, filename: str) -> None:
    """
    Writes the final report to a text file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main() -> None:
    """
    Main function:
    Reads all weeks, computes summaries,
    and writes the final report to summary.txt.
    """
    base_path = Path(__file__).parent

    weeks = {
        41: base_path / "week41.csv",
        42: base_path / "week42.csv",
        43: base_path / "week43.csv",
    }

    full_report = []

    for week_number, path in weeks.items():
        rows = read_data(str(path))
        daily_totals = calculate_daily_totals(rows)
        report_section = format_week_report(week_number, daily_totals)
        full_report.append(report_section)

    final_text = "\n".join(full_report)

    write_report(final_text, str(base_path / "summary.txt"))

    print("Report successfully written to summary.txt")


if __name__ == "__main__":
    main()
