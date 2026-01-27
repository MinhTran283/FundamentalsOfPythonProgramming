from datetime import datetime

def print_reservation_number(reservation: list) -> None:
    """Prints the reservation number"""
    number = int(reservation[0])
    print(f"Reservation number: {number}")

def print_booker(reservation: list) -> None:
    """Prints the booker's name"""
    print(f"Booker: {reservation[1]}")

def print_date(reservation: list) -> None:
    """Prints the reservation date in Finnish format"""
    date_obj = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    print(f"Date: {date_obj.strftime('%d.%m.%Y')}")

def print_start_time(reservation: list) -> None:
    """Prints the start time"""
    time_obj = datetime.strptime(reservation[3], "%H:%M").time()
    print(f"Start time: {time_obj.strftime('%H.%M')}")

def print_hours(reservation: list) -> None:
    """Prints number of hours"""
    hours = int(reservation[4])
    print(f"Number of hours: {hours}")

def print_hourly_rate(reservation: list) -> None:
    """Prints hourly rate"""
    rate = float(reservation[5])
    rate_fi = f"{rate:.2f}".replace(".", ",")
    print(f"Hourly price: {rate_fi} €")

def print_total_price(reservation: list) -> None:
    """Prints total price"""
    hours = int(reservation[4])
    rate = float(reservation[5])
    total = hours * rate
    total_fi = f"{total:.2f}".replace(".", ",")
    print(f"Total price: {total_fi} €")

def print_paid(reservation: list) -> None:
    """Prints payment status"""
    paid = reservation[6] == "True"
    print(f"Paid: {'Yes' if paid else 'No'}")

def print_venue(reservation: list) -> None:
    """Prints venue"""
    print(f"Location: {reservation[7]}")

def print_phone(reservation: list) -> None:
    """Prints phone number"""
    print(f"Phone: {reservation[8]}")

def print_email(reservation: list) -> None:
    """Prints email"""
    print(f"Email: {reservation[9]}")

def main() -> None:
    """Reads reservation data and prints it using functions"""
    with open("reservations.txt", "r", encoding="utf-8") as f:
        reservation = f.read().strip().split("|")

    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_rate(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_venue(reservation)
    print_phone(reservation)
    print_email(reservation)

if __name__ == "__main__":
    main()
