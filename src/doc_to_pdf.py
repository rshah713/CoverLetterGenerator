from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER

# Step 1: Extract text from DOCX
def extract_text(docx_path):
    doc = Document(docx_path)
    lines = []
    for para in doc.paragraphs:
        lines.append(para.text)
    return lines

# Step 2: Write to PDF using ReportLab
def write_pdf(text_lines, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=LETTER)
    width, height = LETTER
    y = height - 50  # start from top

    for line in text_lines:
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line)
        y -= 14  # line spacing

    c.save()

# Run the conversion
lines = extract_text("template.docx")
write_pdf(lines, "output.pdf")
