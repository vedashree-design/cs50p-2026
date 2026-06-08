import sys
import csv
from tabulate import tabulate

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if it's a CSV file
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try to open and print table
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
