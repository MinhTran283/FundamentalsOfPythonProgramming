from datetime import datetime

def greet1():
    text = "123|Anna Virtanen|2025-12-31|10:00|2|19.95|True|Meeting Room A|0401234567|anna.virtanen@example.com".split("|")
    print("-----GREET1-----------")
    date = datetime.strptime(text[2], "%Y-%m-%d").date()
    print(date)

def greet2(reservation):
    text = reservation.split("|")
    print("-----GREET2-----------")
    #date = datetime.strptime(text[2], "%Y-%m-%d").date()
    print(text[1])

def date_conversation(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    return date

def main():
    print(greet1())
    line = "123|Anna Virtanen|2025-11-30|10:00|2|19.95|True|Meeting Room A|0401234567|anna.virtanen@example.com"
    greet2(line)
    reservation = line.split('|')
    print(reservation[2])
    print(date_conversation(reservation[2]))
    converted_date = date_conversation(reservation[2])
    print(converted_date)
    var1 = "word"
    var2 = "123"
    print("|", f"{var1:^8}", "|", f"{var2:>8}", "|")
    print("|", f"{var2:^8}", "|", f"{var1:>8}", "|")

if __name__ == "__main__":
    main()