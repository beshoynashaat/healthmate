import streamlit as st
import time
import os
import sys

# =========================================
# PATH FIX FOR STREAMLIT CLOUD
# =========================================
# This ensures that Agents can import configuration.py correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# =========================================
# IMPORT YOUR AGENTS
# =========================================
try:
    from Agents.leader import leaderRouter
    # from Agents.medical import medical_agent  # Uncomment when ready
except ImportError as e:
    st.error(f"Mapping Error: Could not find Agent files. {e}")

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="HealthMate AI",
    page_icon="🩺",
    layout="wide"
)

# =========================================
# CUSTOM CSS (MODERN GLASSMORPHISM)
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
.metric-box { background: rgba(255,255,255,0.08); padding: 20px; border-radius: 20px; text-align: center; }
.agent-box {
    background-color: rgba(6,182,212,0.15); padding: 10px; border-radius: 10px;
    border-left: 5px solid #06b6d4; margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR NAVIGATION
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
    st.markdown('<p style="font-size: 22px; color: #d1d5db;">Next Generation Medical Intelligence</p>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="metric-box"><h3>📊 BMI</h3><h2>24.1</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-box"><h3>❤️ Heart Rate</h3><h2>76 BPM</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-box"><h3>🧠 AI Score</h3><h2>91%</h2></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="metric-box"><h3>⚕ Status</h3><h2>Good</h2></div>', unsafe_allow_html=True)

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="glass-card"><h2>🤖 Multi-Agent System</h2><p>Smart routing between specialized Medical Agents.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card"><h2>📄 Medical PDF Analysis</h2><p>Upload reports and detect abnormal values instantly.</p></div>', unsafe_allow_html=True)

# =========================================
# CHAT ASSISTANT (MODEL INTEGRATED)
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
            with st.spinner("AI Agent Processing..."):
                try:
                    # CALLING YOUR ACTUAL AGENT
                    response = leaderRouter(user_input)
                except Exception as e:
                    response = f"Agent Error: {str(e)}"

            full_response = ""
            placeholder = st.empty()
            for char in response:
                full_response += char
                time.sleep(0.01)
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)

            st.markdown(f'<div class="agent-box"><b>Agent Used:</b> HealthMate Leader Agent</div>', unsafe_allow_html=True)

        st.session_state.messages.append({"role": "assistant", "content": response})

# =========================================
# BMI CALCULATOR (WORKING)
# =========================================
elif page == "BMI Calculator":
    st.title("📊 BMI Calculator")
    col1, col2 = st.columns(2)
    with col1: weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
    with col2: height = st.number_input("Height (m)", min_value=0.5, value=1.75)

    if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.markdown(f'<div class="glass-card"><h2>Your BMI: {bmi:.2f}</h2></div>', unsafe_allow_html=True)
        if bmi < 18.5: st.warning("Underweight")
        elif bmi < 25: st.success("Normal Weight ✅")
        else: st.error("Overweight")

# =========================================
# OTHER PAGES (STRUCTURED)
# =========================================
elif page == "Drug Information":
    st.title("💊 Drug Information")
    drug_name = st.text_input("Enter Drug Name")
    if st.button("Search"):
        # Integration point: call your drug agent here
        st.info(f"Feature coming soon: Detailed analysis for {drug_name}")

elif page == "Symptom Checker":
    st.title("🩺 Symptom Checker")
    symptoms = st.text_area("Describe how you feel...")
    if st.button("Analyze"):
        # Integration point: call your symptom agent here
        st.success("Leader agent is evaluating symptoms.")

elif page == "Medical Test Analyzer":
    st.title("📄 Medical Test Analyzer")
    uploaded_file = st.file_uploader("Upload Lab Report", type=["pdf", "txt"])
    if uploaded_file:
        st.success("File uploaded. Ready for AI Analysis.")

elif page == "User Profile":
    st.title("👤 User Profile")
    st.text_input("Full Name")
    st.number_input("Age", min_value=1)
    if st.button("Save Profile"):
        st.balloons()
        st.success("Profile Updated!")

# =========================================
# FOOTER
# =========================================
st.write("---")
st.caption("⚡ HealthMate AI ©️ 2026 | Developed by Beshoy Nashaat")
