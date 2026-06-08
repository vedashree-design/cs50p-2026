import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if it's a Python file
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # Try to open and count lines
    try:
        with open(sys.argv[1], "r") as file:
            count = 0 # start adding from here
            for line in file:
                stripped = line.lstrip()
                if stripped == "" or stripped.startswith("#"):
                   continue
                count += 1
    except FileNotFoundError:
         sys.exit("File does not exist")

    print(count)

if __name__ == "__main__":
    main()
