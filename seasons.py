from datetime import date
import sys
import inflect

def get_minutes(birth_date):
    """Calculate minutes from birth date to today"""
    today = date.today()
    if birth_date > today:
        raise ValueError("Invalid date")
    return (today - birth_date).days * 24 * 60

def main():
    dob_str = input("Date of Birth: ")
    try:
        birth = date.fromisoformat(dob_str)
    except ValueError:
        sys.exit("Invalid date")

    try:
        minutes = get_minutes(birth)
    except ValueError:
        sys.exit("Invalid date")

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")

if __name__ == "__main__":
    main()
    