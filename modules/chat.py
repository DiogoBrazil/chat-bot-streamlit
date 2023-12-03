import streamlit as st
from modules.openai_api import get_openai_response
from utils.config import get_model_name


def display_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_input():
    prompt = st.chat_input("Digite sua pergunta...")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_openai_response(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            prompt = prompt.lower()
            keys_words = ["code", "script", "codigo", "código", "função", "funcao", "function", "def"]
            code = any(word in prompt for word in keys_words)
            if code:
                st.code(response)
            else:
                st.markdown(response)

