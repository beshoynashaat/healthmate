from langchain.tools import tool
import requests


@tool
def drugInfo(drugName: str) -> str:
    """
    Searches DailyMed for basic drug information.
    Input: drug name as a plain string, e.g. 'ibuprofen'.
    """

    disclaimer = "DISCLAIMER: For educational purposes only. Not medical advice."

    try:
        drugName = drugName.strip().lower()

        searchURL = (
            "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json"
            f"?drug_name={drugName}"
        )

        searchResponse = requests.get(searchURL, timeout=10).json()

        if not searchResponse.get("data"):
            return f"{disclaimer}\n\nNo DailyMed records found for '{drugName}'."

        brandName = searchResponse["data"][0].get("title", drugName)

        return f"""
{disclaimer}

Drug: {brandName}

Common Use:
Pain relief / fever reduction or symptom relief depending on the product.

Warnings:
- Do not exceed the recommended dose.
- Avoid if allergic to this drug or similar drugs.
- Ask a doctor if you have stomach, kidney, liver, heart disease, asthma, pregnancy, or take blood thinners.
- Stop use and seek medical help if you get rash, swelling, breathing trouble, severe stomach pain, or unusual bleeding.
"""

    except Exception as e:
        return f"{disclaimer}\n\nError retrieving drug info: {str(e)}"