import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import os

# Option A: The Streamlit Way (Recommended)
api_key = st.secrets["GOOGLE_API_KEY"]

GEMINI = os.getenv("GEMINI")

leader = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=GEMINI
)

chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=GEMINI
)

medical = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=GEMINI
)