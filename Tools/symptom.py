from langchain.tools import tool

mockDB = {
    "headache":    ["Tension headache", "Migraine", "Dehydration", "Stress"],
    "back pain":   ["Muscle strain", "Poor posture", "Herniated disc"],
    "fever":       ["Common cold", "Influenza", "Infection"],
    "cough":       ["Bronchitis", "Allergies", "Common cold"],
    "sore throat": ["Strep throat", "Viral pharyngitis", "Dry air"]
}

def getMockSymptoms(query: str):
    query = query.lower()
    possibleConditions = []
    for symptom, conditions in mockDB.items():
        if symptom in query:
            possibleConditions.extend(conditions)
    if not possibleConditions:
        return "No specific conditions found in the trivia database for these symptoms."
    unique_conditions = list(set(possibleConditions))
    return f"Based on your symptoms, possible conditions include: {', '.join(unique_conditions)}."

@tool
def symptomChecker(symptoms: str) -> str:
    """
    Provides potential medical conditions based on user-reported symptoms.
    Input: a plain string describing the symptoms (e.g. 'headache and fever').
    """
    disclaimer = "DISCLAIMER: This is a mock tool for educational purposes only. Not medical advice.\n\n"
    return disclaimer + getMockSymptoms(symptoms)