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
# NORMAL URINE TEST DATA
# =========================
normal_data = [
    ["Test", "Value", "Normal Range"],
    ["Color", "Yellow", "Yellow"],
    ["Appearance", "Clear", "Clear"],
    ["pH", 6.0, "4.5 - 8.0"],
    ["Specific Gravity", 1.020, "1.005 - 1.030"],
    ["Protein", "Negative", "Negative"],
    ["Glucose", "Negative", "Negative"],
    ["Ketones", "Negative", "Negative"],
    ["RBC", "0-2 /HPF", "0-2 /HPF"],
    ["WBC", "0-5 /HPF", "0-5 /HPF"],
]

# =========================
# MIXED URINE TEST DATA
# =========================
mixed_data = [
    ["Test", "Value", "Normal Range"],

    # ABNORMAL COLOR
    ["Color", "Dark Yellow", "Yellow"],

    # CLOUDY
    ["Appearance", "Cloudy", "Clear"],

    # LOW pH
    ["pH", 4.0, "4.5 - 8.0"],

    # HIGH SPECIFIC GRAVITY
    ["Specific Gravity", 1.040, "1.005 - 1.030"],

    # POSITIVE PROTEIN
    ["Protein", "Positive", "Negative"],

    # POSITIVE GLUCOSE
    ["Glucose", "Positive", "Negative"],

    # POSITIVE KETONES
    ["Ketones", "Positive", "Negative"],

    # HIGH RBC
    ["RBC", "10-15 /HPF", "0-2 /HPF"],

    # HIGH WBC
    ["WBC", "15-20 /HPF", "0-5 /HPF"],
]

# =========================
# CREATE FILES
# =========================
create_pdf(
    "Dummy tests/normal_urine_test.pdf",
    "Normal Urine Test Report",
    normal_data
)

create_pdf(
    "Dummy tests/mixed_urine_test.pdf",
    "Mixed Urine Test Report",
    mixed_data
)

print("Dummy urine test PDFs created successfully")