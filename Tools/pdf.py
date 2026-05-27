from langchain.tools import tool
import fitz


@tool
def medicalTestAnalyzer(testResults: str) -> str:
    """
    Extracts blood test values from a PDF file path and returns abnormal findings.
    Input: PDF file path as a string.
    """

    normalRanges = {
        "Hemoglobin": (13, 17),
        "WBC": (4000, 11000),
        "Platelets": (150000, 450000),
        "Glucose": (70, 140),
        "Creatinine": (0.7, 1.3),
    }

    try:
        doc = fitz.open(testResults)

        text = ""
        for page in doc:
            text += page.get_text()

        doc.close()

        lines = [x.strip() for x in text.split("\n") if x.strip()]

        findings = []

        for i in range(len(lines) - 1):
            testName = lines[i]

            if testName not in normalRanges:
                continue

            try:
                value = float(lines[i + 1])
            except:
                continue

            low, high = normalRanges[testName]

            if value < low:
                findings.append(
                    f"{testName}: LOW ({value}) range={low}-{high}"
                )

            elif value > high:
                findings.append(
                    f"{testName}: HIGH ({value}) range={low}-{high}"
                )

        if not findings:
            return "status=normal"

        return " | ".join(findings)

    except Exception as e:
        return f"error={str(e)}"