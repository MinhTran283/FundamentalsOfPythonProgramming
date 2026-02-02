from pathlib import Path


def main():
    #with open("data.txt", "a", encoding="utf-8") as f:
    #    f.write("New contentadfa\n")
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            content = f.read()

        print(content)
    except FileNotFoundError:
        print("File not found – check the path.")
    except PermissionError:
        print("No permission to read the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    #f = open("data.txt", "a")
    #f.write("Hello\n")

if __name__ == "__main__":
    main()

