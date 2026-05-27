# %% 
from Agents.leader import leaderRouter

def chat(user_input: str) -> str:
    return leaderRouter(user_input)

# %% Test - T1 Multi-tool query
print(chat("What's my BMI, and for my back pain what OTC drug might help?"))

# %% Test - T2 Allergy check
print(chat("Is diphenhydramine safe for me?"))

# %% Test - Q1 Drug info
print(chat("Can I take ibuprofen for my headache?"))

# %% Normal Test
print(chat("Analyze this blood test: ./Dummy tests/normal_blood_test.pdf"))

# %% Abnormal Test
print(chat("Analyze this blood test: ./Dummy tests/mixed_blood_test.pdf"))

# %%