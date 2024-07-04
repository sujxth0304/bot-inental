import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai  # Ensure this is the correct library

# Load environment variables
load_dotenv()
key = os.getenv("GEMINI_API_KEY")
gen_ai.configure(api_key=key)
model = gen_ai.GenerativeModel('gemini-pro')

# Configure Streamlit page
st.set_page_config(
    page_title="ChatBot",
    page_icon=":brain:",
    layout="centered"
)

def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session if not already initialized
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Page title
st.title("bot-inental")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# User input
user_prompt = st.chat_input("Ask bot-inental...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
