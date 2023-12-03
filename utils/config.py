import streamlit as st


def initialize_session_state():
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "text-davinci-003"
    if "messages" not in st.session_state:
        st.session_state.messages = []


def get_model_name():
    return st.session_state["openai_model"]
