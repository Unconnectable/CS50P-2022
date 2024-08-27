from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name, in_path='shirtificate.png', out_path='shirtificate.pdf'):
        super().__init__(orientation='P', format='A4')
        self.name = name
        self.in_path = in_path
        self.out_path = out_path

    def create_pdf(self):
        self.add_page()
        self.set_font("Helvetica", 'B', 16)
        self.cell(0, 10, 'took CS50', ln=False, align='C')

        self.image(self.in_path, x=10, y=30)
        self.set_font("Helvetica", 'B', 16)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 100)
        self.cell(0, 10, self.name, ln=False, align='C')

        self.output(self.out_path)


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.create_pdf()


main()
