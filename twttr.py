# twttr.py
text = input("Input: ")
print("Output:", "".join([c for c in text if c.lower() not in "aeiou"]))
output = ""

for char in text:
    if char.lower() not in ["a", "e", "i", "o", "u"]:
        output += char

print("Output:", output)
