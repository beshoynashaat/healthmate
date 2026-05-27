import streamlit as st
import time
import os

# =========================================
# IMPORT YOUR AGENTS
# =========================================
# Ensure your working directory is set correctly for Streamlit Cloud
from Agents.leader import leaderRouter
# from Agents.medical import medical_agent  # If you have these separate
# from Agents.drug import drug_agent        # If you have these separate

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="HealthMate AI",
    page_icon="🩺",
    layout="wide"
)

# =========================================
# CUSTOM CSS (KEEPING YOUR MODERN STYLE)
# =========================================
st.markdown("""
<style>
.main { background: linear-gradient(135deg, #0f172a, #111827); color: white; }
section[data-testid="stSidebar"] { background-color: #111827; }
.stButton>button {
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color: white; border: none; border-radius: 15px;
    height: 50px; font-size: 16px; font-weight: bold; transition: 0.3s;
}
.stButton>button:hover { transform: scale(1.03); box-shadow: 0px 0px 20px rgba(6,182,212,0.5); }
.glass-card {
    background: rgba(255,255,255,0.08); border-radius: 20px; padding: 25px;
    backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 20px; box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
}
.big-title { font-size: 50px; font-weight: bold; color: #67e8f9; }
.subtitle { font-size: 22px; color: #d1d5db; }
.metric-box { background: rgba(255,255,255,0.08); padding: 20px; border-radius: 20px; text-align: center; }
.agent-box {
    background-color: rgba(6,182,212,0.15); padding: 10px; border-radius: 10px;
    border-left: 5px solid #06b6d4; margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR & NAVIGATION
# =========================================
st.sidebar.title("🩺 HealthMate AI")
st.sidebar.write("Smart Medical Multi-Agent System")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Chat Assistant", "BMI Calculator", "Drug Information", "Symptom Checker", "Medical Test Analyzer", "User Profile"]
)

# =========================================
# HOME PAGE
# =========================================
if page == "Home":
    st.markdown('<p class="big-title">⚡ HealthMate AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Next Generation Medical Intelligence</p>', unsafe_allow_html=True)
    
    # Dashboard Metrics (Static for UI, can be linked to User Profile later)
    c1, c2, c3, c4 = st.columns(4)
    metrics = [("📊 BMI", "24.1"), ("❤️ Heart Rate", "76 BPM"), ("🧠 AI Score", "91%"), ("⚕ Status", "Good")]
    for col, (label, val) in zip([c1, c2, c3, c4], metrics):
        col.markdown(f'<div class="metric-box"><h3>{label}</h3><h2>{val}</h2></div>', unsafe_allow_html=True)

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="glass-card"><h2>🤖 Multi-Agent System</h2><p>Powered by Gemini 2.5/3.5 Flash routing logic.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card"><h2>📄 Medical PDF Analysis</h2><p>Upload reports and detect abnormal values.</p></div>', unsafe_allow_html=True)

# =========================================
# CHAT ASSISTANT (INTEGRATED WITH YOUR MODELS)
# =========================================
elif page == "Chat Assistant":
    st.title("💬 AI Chat Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask HealthMate anything...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("HealthMate Leader Agent Routing..."):
                # CALL YOUR ACTUAL MODEL HERE
                try:
                    # leaderRouter processes the input and selects the agent
                    # Make sure leaderRouter returns a clean string response
                    response = leaderRouter(user_input)
                except Exception as e:
                    response = f"Error connecting to models: {str(e)}"

            # Stream the response for better UX
            full_response = ""
            placeholder = st.empty()
            for char in response:
                full_response += char
                time.sleep(0.01)
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)

            st.markdown('<div class="agent-box"><b>Agent Note:</b> Response generated via Leader Router</div>', unsafe_allow_html=True)

        st.session_state.messages.append({"role": "assistant", "content": response})

# =========================================
# BMI CALCULATOR
# =========================================
elif page == "BMI Calculator":
    st.title("📊 BMI Calculator")
    col1, col2 = st.columns(2)
    with col1: weight = st.number_input("Weight (kg)", min_value=1.0)
    with col2: height = st.number_input("Height (m)", min_value=0.5)

    if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.markdown(f'<div class="glass-card"><h2>Your BMI: {bmi:.2f}</h2></div>', unsafe_allow_html=True)
        if bmi < 18.5: st.warning("Underweight")
        elif bmi < 25: st.success("Normal Weight ✅")
        else: st.error("Overweight/Obese")

# =========================================
# FOOTER
# =========================================
st.write("---")
st.caption("⚡ HealthMate AI ©️ 2026 | Built by Beshoy Nashaat")
