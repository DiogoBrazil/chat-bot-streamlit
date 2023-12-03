import openai
import streamlit as st
from modules.chat import display_chat, handle_user_input
from utils.config import initialize_session_state


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title("Assistente Virtual com IA Generativa")

local_css("style.css")

initialize_session_state()

display_chat()

handle_user_input()
