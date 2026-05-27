import re

from Tools.drugs import drugInfo
from Tools.symptoms import symptomChecker
from Tools.pdf import medicalTestAnalyzer


def _extract_pdf_path(user_input: str):
    match = re.search(r"([./\\\w\s()-]+\.pdf)", user_input, re.I)
    if not match:
        return None
    return match.group(1).strip()


def _extract_drug_name(user_input: str):
    known = ["ibuprofen", "diphenhydramine", "paracetamol", "acetaminophen", "aspirin", "naproxen"]
    lower = user_input.lower()

    for drug in known:
        if drug in lower:
            return drug

    if "back pain" in lower or "headache" in lower or "pain" in lower:
        return "ibuprofen"

    return None


def runMedicalAgent(user_input: str):
    pdf_path = _extract_pdf_path(user_input)
    if pdf_path:
        return medicalTestAnalyzer.invoke(pdf_path)

    drug = _extract_drug_name(user_input)
    if drug:
        return drugInfo.invoke(drug)

    return symptomChecker.invoke(user_input)