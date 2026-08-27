from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 24)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.image("shirtificate.png", x=10, y=80, w=190)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 140, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
    