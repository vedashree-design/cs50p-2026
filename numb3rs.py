import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Match exactly 4 groups of 1-3 digits separated by dots
    if matches := re.search(r"^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$", ip):
        # Check each group is 0-255
        for group in matches.groups():
            if int(group) > 255:
                return False
        return True
    else:
            return False

if __name__ == "__main__":
    main()
