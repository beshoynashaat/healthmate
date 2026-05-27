from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

# =========================
# Helper to build PDF
# =========================
def create_pdf(filename, title, data):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph(title, styles["Title"]))
    elements.append(Spacer(1, 20))

    table = Table(data, colWidths=[180, 120, 150])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(table)
    doc.build(elements)

# =========================
# NORMAL LFT DATA
# =========================
normal_data = [
    ["Test", "Value", "Normal Range"],
    ["ALT (SGPT)", 32, "7 - 56 U/L"],
    ["AST (SGOT)", 28, "10 - 40 U/L"],
    ["ALP", 90, "44 - 147 U/L"],
    ["Total Bilirubin", 0.8, "0.1 - 1.2 mg/dL"],
    ["Direct Bilirubin", 0.2, "0.0 - 0.3 mg/dL"],
    ["Albumin", 4.5, "3.5 - 5.0 g/dL"],
    ["Total Protein", 7.0, "6.0 - 8.3 g/dL"],
]

# =========================
# MIXED LFT DATA
# =========================
mixed_data = [
    ["Test", "Value", "Normal Range"],

    # HIGH ALT
    ["ALT (SGPT)", 95, "7 - 56 U/L"],

    # HIGH AST
    ["AST (SGOT)", 80, "10 - 40 U/L"],

    # NORMAL ALP
    ["ALP", 110, "44 - 147 U/L"],

    # HIGH BILIRUBIN
    ["Total Bilirubin", 2.5, "0.1 - 1.2 mg/dL"],

    # HIGH DIRECT BILIRUBIN
    ["Direct Bilirubin", 0.8, "0.0 - 0.3 mg/dL"],

    # LOW ALBUMIN
    ["Albumin", 2.9, "3.5 - 5.0 g/dL"],

    # NORMAL TOTAL PROTEIN
    ["Total Protein", 6.8, "6.0 - 8.3 g/dL"],
]

# =========================
# CREATE FILES
# =========================
create_pdf(
    "Dummy tests/normal_liver_function_test.pdf",
    "Normal Liver Function Test Report",
    normal_data
)

create_pdf(
    "Dummy tests/mixed_liver_function_test.pdf",
    "Mixed Liver Function Test Report",
    mixed_data
)

print("Dummy Liver Function Test PDFs created successfully")