def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    text = input("Text: ")
    print(convert(text))

main()
