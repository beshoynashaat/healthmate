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
# NORMAL KIDNEY FUNCTION TEST DATA
# =========================
normal_data = [
    ["Test", "Value", "Normal Range"],
    ["Creatinine", 1.0, "0.7 - 1.3 mg/dL"],
    ["Blood Urea Nitrogen (BUN)", 14, "7 - 20 mg/dL"],
    ["Uric Acid", 5.2, "3.5 - 7.2 mg/dL"],
    ["Sodium", 140, "135 - 145 mmol/L"],
    ["Potassium", 4.2, "3.5 - 5.0 mmol/L"],
    ["Chloride", 102, "96 - 106 mmol/L"],
    ["Calcium", 9.4, "8.5 - 10.5 mg/dL"],
    ["eGFR", 95, "> 90 mL/min/1.73m²"],
]

# =========================
# MIXED KIDNEY FUNCTION TEST DATA
# =========================
mixed_data = [
    ["Test", "Value", "Normal Range"],

    # HIGH CREATININE
    ["Creatinine", 2.1, "0.7 - 1.3 mg/dL"],

    # HIGH BUN
    ["Blood Urea Nitrogen (BUN)", 35, "7 - 20 mg/dL"],

    # HIGH URIC ACID
    ["Uric Acid", 8.5, "3.5 - 7.2 mg/dL"],

    # LOW SODIUM
    ["Sodium", 130, "135 - 145 mmol/L"],

    # HIGH POTASSIUM
    ["Potassium", 5.8, "3.5 - 5.0 mmol/L"],

    # NORMAL CHLORIDE
    ["Chloride", 101, "96 - 106 mmol/L"],

    # LOW CALCIUM
    ["Calcium", 7.9, "8.5 - 10.5 mg/dL"],

    # LOW eGFR
    ["eGFR", 48, "> 90 mL/min/1.73m²"],
]

# =========================
# CREATE FILES
# =========================
create_pdf(
    "Dummy tests/normal_kidney_function_test.pdf",
    "Normal Kidney Function Test Report",
    normal_data
)

create_pdf(
    "Dummy tests/mixed_kidney_function_test.pdf",
    "Mixed Kidney Function Test Report",
    mixed_data
)

print("Dummy Kidney Function Test PDFs created successfully")