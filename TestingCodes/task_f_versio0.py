def main():
    try:
        while True:
            print("Choose a report type:")
            print("1) Daily summary for a date range")
            print("2) Monthly summary for one month")
            print("3) Full year 2025 summary")
            print("4) Exit the program")
            report_type = input("Your choice: ")
            match report_type.strip():
                case "1":
                    start_date = input("Enter start date (dd.mm.yyyy): ")
                    end_date = input("Enter end date (dd.mm.yyyy): ")
                    print(start_date, end_date)
                case "2":
                    month_number = input("Enter month number (1–12): ")
                    print(month_number)
                case "3":
                    print("year 2025 report")
                case "4":
                    print("Thank you! Bye!")
                    break
                case _:
                    print("Unknown choice. Please, do a new selection.")
    except KeyboardInterrupt:
        print("\nYou pressed CTRL-C")

if __name__ == "__main__":
    main()