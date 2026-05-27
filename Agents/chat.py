import os
from langchain_core.prompts import ChatPromptTemplate
from configuration import chat


def loadPrompt(file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "..", "prompts", file)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


safePrompt = ChatPromptTemplate.from_template(
    loadPrompt("safe.jinja")
)


def runChatAgent(user_input: str):

    formatted_prompt = safePrompt.format_messages(
        user_input=user_input
    )

    response = chat.invoke(formatted_prompt)

    return response.content