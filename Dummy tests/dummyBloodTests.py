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
# NORMAL TEST DATA
# =========================
normal_data = [
    ["Test", "Value", "Normal Range"],
    ["Hemoglobin", 15.0, "13 - 17"],
    ["WBC", 7000, "4000 - 11000"],
    ["Platelets", 250000, "150000 - 450000"],
    ["Glucose", 100, "70 - 140"],
    ["Creatinine", 1.0, "0.7 - 1.3"],
]

# =========================
# MIXED TEST DATA
# =========================
mixed_data = [
    ["Test", "Value", "Normal Range"],

    # LOW
    ["Hemoglobin", 10.5, "13 - 17"],

    # NORMAL
    ["WBC", 8000, "4000 - 11000"],

    # HIGH
    ["Platelets", 500000, "150000 - 450000"],

    # HIGH
    ["Glucose", 180, "70 - 140"],

    # NORMAL
    ["Creatinine", 1.0, "0.7 - 1.3"],
]

# =========================
# CREATE FILES
# =========================
create_pdf(
    "Dummy tests/normal_blood_test.pdf",
    "Normal Blood Test Report",
    normal_data
)

create_pdf(
    "Dummy tests/mixed_blood_test.pdf",
    "Mixed Blood Test Report",
    mixed_data
)

print("Dummy PDFs created successfully")