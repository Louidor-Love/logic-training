from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 12)
        self.cell(0, 10, "Plan de Estudio Salesforce Developer (Junior)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("DejaVu", "", 10)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()

# Agregar fuente ANTES de usarla
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans.ttf", uni=True)

pdf.add_page()