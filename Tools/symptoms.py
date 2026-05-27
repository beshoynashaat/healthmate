from langchain.tools import tool

mockDB = {
    "headache": ["Tension headache", "Migraine", "Dehydration", "Stress"],
    "back pain": ["Muscle strain", "Poor posture", "Herniated disc"],
    "fever": ["Common cold", "Influenza", "Infection"],
    "cough": ["Bronchitis", "Allergies", "Common cold"],
    "sore throat": ["Strep throat", "Viral pharyngitis", "Dry air"]
}


def getMockSymptoms(query: str):
    query = query.lower()
    possibleConditions = []

    for symptom, conditions in mockDB.items():
        if symptom in query:
            possibleConditions.extend(conditions)

    if not possibleConditions:
        return "none"

    unique_conditions = list(set(possibleConditions))
    return ",".join(unique_conditions)


@tool
def symptomChecker(symptoms: str) -> str:
    """
    Returns possible conditions based on symptoms (raw output only).
    Input: symptom string like 'headache and fever'
    """

    try:
        result = getMockSymptoms(symptoms)
        return f"conditions={result}"

    except Exception as e:
        return f"error={str(e)}"