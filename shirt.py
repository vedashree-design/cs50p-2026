import sys
from PIL import Image, ImageOps

def main():
    # Check arg count
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check valid extensions
    valid_ext = [".jpg", ".jpeg", ".png"]
    input_ext = sys.argv[1].lower()
    output_ext = sys.argv[2].lower()

    if not any(input_ext.endswith(ext) for ext in valid_ext):
        sys.exit("Invalid input")
    if not any(output_ext.endswith(ext) for ext in valid_ext):
        sys.exit("Invalid output")

    # Check extensions match
    if input_ext.split(".")[-1]!= output_ext.split(".")[-1]:
        sys.exit("Input and output have different extensions")

    # Try to overlay shirt
    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])

        # Resize photo to match shirt size
        photo = ImageOps.fit(photo, shirt.size)

        # Paste shirt onto photo with transparency mask
        photo.paste(shirt, shirt)

        # Save result
        photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
