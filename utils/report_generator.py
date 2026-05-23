from fpdf import FPDF

def generate_pdf_report(summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0,10,summary)
    pdf.output("financial_report.pdf")