def main():
    try:
        print("This app asks your name and age. After asking we print your inputs.")
        print("You can interrupt this with keys CTRL-C")
        while True:
            name = input("Your name: ")
            age = int(input("Your age: "))
            print(f"Hi {name}! You are {age} years old.")
            selections = input("Do you want to continue? If not press q: ")
            if ( selections == "q"):
                print("Thank you! Bye!")
                break
    except KeyboardInterrupt:
        print("\nThank you! Bye!")

if __name__ == "__main__":
    main()