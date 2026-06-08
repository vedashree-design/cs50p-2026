# plates.py
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Length 2-6
    if not 2 <= len(s) <= 6:
        return False

    # Rule 2: First 2 must be letters
    if not s[0:2].isalpha():
        return False

    # Rule 3 & 4: Check rest of string
    for i in range(len(s)):
        if s[i].isdigit():
            # First number can't be 0
            if s[i] == "0":
                return False
            # Everything after must also be digits
            if not s[i:].isdigit():
                    return False
            break
        # Rule 4: No punctuation
        elif not s[i].isalpha():
            return False

    return True

if __name__ == "__main__":
   main()
