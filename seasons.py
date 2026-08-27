from datetime import date
import sys
import inflect

def main():
    dob_str = input("Date of Birth: ")
    try:
        birth = date.fromisoformat(dob_str)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    if birth > today:
        sys.exit("Invalid date")
        
    minutes = (today - birth).days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    print(f"{words.capitalize()} minutes")

if __name__ == "__main__":
    main()