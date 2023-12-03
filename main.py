import openai
import streamlit as st

# from openai import OpenAI

st.title("Assistente Virtual com IA Generativa")

# Set OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "text-davinci-003"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Digite sua pergunta..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        # Display assistant response in chat message container
        formatted_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])

        # Generate response using OpenAI
        response = openai.Completion.create(
            model=st.session_state["openai_model"],
            prompt=formatted_prompt,
            max_tokens=1024,
            temperature=0.7
        )

        full_response = response.choices[0].text.strip()
        if full_response.startswith("bot:") or full_response.startswith("assistant:") or full_response.startswith("Robô:"):
            full_response = full_response.split(":", 1)[1].strip()
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

