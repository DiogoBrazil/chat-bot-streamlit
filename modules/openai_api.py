import openai
from utils.config import get_model_name
import streamlit as st


def get_openai_response(prompt):

    formatted_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages if m["role"] != "assistant" or m == st.session_state.messages[-1]])

    response = openai.Completion.create(
        model=get_model_name(),
        prompt=formatted_prompt,
        max_tokens=1024,
        temperature=0.7
    )

    full_response = response.choices[0].text.strip()
    if full_response.startswith(("Bot:", "bot:", "assistant:", "Robô:", "robô:", "Atendente:", "Resposta:", "R:")):
        full_response = full_response.split(":", 1)[1].strip()

    return full_response
