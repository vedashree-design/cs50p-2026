import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
        pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
        if matches := re.search(pattern, s):
            h1, m1, mer1, h2, m2, mer2 = matches.groups()

            # Default minutes to 00 if None
            m1 = m1 or "00"
            m2 = m2 or "00"

            # Validate hours/minutes
            if not (1 <= int(h1) <= 12 and 1 <= int(h2) <= 12):
               raise ValueError
            if not (0 <= int(m1) <= 59 and 0 <= int(m2) <= 59):
               raise ValueError

            # Convert to 24-hour
            h1_24 = convert_24(int(h1), mer1)
            h2_24 = convert_24(int(h2), mer2)

            return f"{h1_24:02}:{m1} to {h2_24:02}:{m2}"
        else:
            raise ValueError

def convert_24(hour, meridian):
    if meridian == "AM":
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12

if __name__ == "__main__":
    main()
