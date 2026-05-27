import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# This line checks Streamlit Secrets first, then falls back to local Env variables
GEMINI = st.secrets.get("GEMINI") or os.getenv("GEMINI")

leader = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=GEMINI
)

chat = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=GEMINI
)

medical = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=GEMINI
)
