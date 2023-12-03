import streamlit as st
from modules.chat import display_chat, handle_user_input
from utils.config import initialize_session_state

st.title("Assistente Virtual com IA Generativa")

initialize_session_state()

display_chat()

handle_user_input()
