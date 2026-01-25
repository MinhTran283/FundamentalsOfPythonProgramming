from datetime import datetime

def main():
    file_name = "reservations.txt"

    with open(file_name, "r", encoding="utf-8") as f:
        line = f.read().strip()

    reservation = line.split("|")

    reservation_number = int(reservation[0])
    booker = reservation[1]

    date_obj = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    date_fi = date_obj.strftime("%d.%m.%Y")

    time_obj = datetime.strptime(reservation[3], "%H:%M").time()
    time_fi = time_obj.strftime("%H.%M")

    hours = int(reservation[4])
    hourly_price = float(reservation[5])
    paid = reservation[6] == "True"

    location = reservation[7]
    phone = reservation[8]
    email = reservation[9]

    total_price = hours * hourly_price

    hourly_price_fi = f"{hourly_price:.2f}".replace(".", ",")
    total_price_fi = f"{total_price:.2f}".replace(".", ",")

    print(f"Reservation number: {reservation_number}")
    print(f"Booker: {booker}")
    print(f"Date: {date_fi}")
    print(f"Start time: {time_fi}")
    print(f"Number of hours: {hours}")
    print(f"Hourly price: {hourly_price_fi} €")
    print(f"Total price: {total_price_fi} €")
    print(f"Paid: {'Yes' if paid else 'No'}")
    print(f"Location: {location}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

if __name__ == "__main__":
    main()
