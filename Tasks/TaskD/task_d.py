from datetime import datetime, date
from typing import List

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

def read_data(filename: str) -> List[list]:
    """
    Reads the CSV file and returns the rows as lists (without header).
    """
    rows = []

    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline()  # bỏ dòng header
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            rows.append(parts)

    return rows

from datetime import datetime, date
from typing import List, Dict


def group_by_day(rows: List[list]) -> Dict[date, dict]:
    """
    Groups hourly CSV rows by date and sums consumption and production (Wh).
    """
    daily = {}

    for row in rows:
        # row[0] = timestamp, e.g. "2025-10-13T09:00:00"
        timestamp = row[0]

        # STEP 3 logic (đã hiểu): string -> datetime -> date
        dt = datetime.fromisoformat(timestamp)
        d = dt.date()

        # Nếu ngày chưa tồn tại, tạo mới
        if d not in daily:
            daily[d] = {
                "cons": [0, 0, 0],
                "prod": [0, 0, 0],
            }

        # Cộng dồn consumption (Wh)
        daily[d]["cons"][0] += int(row[1])
        daily[d]["cons"][1] += int(row[2])
        daily[d]["cons"][2] += int(row[3])

        # Cộng dồn production (Wh)
        daily[d]["prod"][0] += int(row[4])
        daily[d]["prod"][1] += int(row[5])
        daily[d]["prod"][2] += int(row[6])

    return daily


def wh_to_kwh_str(value_wh: int) -> str:
    """
    Converts Wh to kWh and formats it with two decimals and a comma.
    """
    value_kwh = value_wh / 1000
    return f"{value_kwh:.2f}".replace(".", ",")


def main() -> None:
    """
    Main function: reads data, computes daily totals,
    and prints the weekly report.
    """
    rows = read_data("week42.csv")
    daily = group_by_day(rows)

    print("Week 42 electricity consumption and production (kWh, by phase)\n")

    print(
        f"{'Day':<10} {'Date':<12}"
        f"{'Consumption [kWh]':<28}"
        f"{'Production [kWh]'}"
    )
    print(
        f"{'':<10} {'(dd.mm.yyyy)':<12}"
        f"{'v1':>6}{'v2':>8}{'v3':>8}"
        f"{'v1':>10}{'v2':>8}{'v3':>8}"
    )
    print("-" * 78)

    for d in sorted(daily):
        weekday = WEEKDAYS[d.weekday()]
        date_str = d.strftime("%d.%m.%Y")

        cons = daily[d]["cons"]
        prod = daily[d]["prod"]

        print(
            f"{weekday:<10} {date_str:<12}"
            f"{wh_to_kwh_str(cons[0]):>6}"
            f"{wh_to_kwh_str(cons[1]):>8}"
            f"{wh_to_kwh_str(cons[2]):>8}"
            f"{wh_to_kwh_str(prod[0]):>10}"
            f"{wh_to_kwh_str(prod[1]):>8}"
            f"{wh_to_kwh_str(prod[2]):>8}"
        )


if __name__ == "__main__":
    main()