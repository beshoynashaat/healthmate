import os
from langchain_core.prompts import ChatPromptTemplate
from configuration import leader


def loadPrompt(file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "..", "prompts", file)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


leaderPrompt = ChatPromptTemplate.from_template(
    loadPrompt("leader.jinja")
)


def leaderRouter(userInput):

    from Agents.calc import runCalcAgent
    from Agents.medical import runMedicalAgent
    from Agents.chat import runChatAgent

    formatted_prompt = leaderPrompt.format_messages(
        user_input=userInput
    )

    decision = leader.invoke(formatted_prompt).content.strip().upper()

    responses = []

    if "CALC" in decision:
        responses.append(runCalcAgent(userInput))

    if "MEDICAL" in decision:
        responses.append(runMedicalAgent(userInput))

    if "CHAT" in decision and not responses:
        responses.append(runChatAgent(userInput))

    if not responses:
        responses.append(runChatAgent(userInput))

    return "\n\n".join(responses)