import streamlit as st
from Agents.leader import leaderRouter
from Memory.memory import USER, buildSystemPrompt

# Initialize chat history in Streamlit's own state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": buildSystemPrompt(USER)}
    ]

st.title("Healthmate AI")

# Display messages (skipping the system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("How can I help?"):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response via the Leader Router
    # You may need to update leaderRouter to accept the history if needed
    response = leaderRouter(prompt) 
    
    # Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
