import openai
from PIL import Image
import streamlit as st
from modules.chat import display_chat, handle_user_input
from utils.config import initialize_session_state

openai.api_key = st.secrets["OPENAI_API_KEY"]

url = "https://api.whatsapp.com/send?phone=69999749201&text=Ol%C3%A1%2C+Gostaria+de+reportar+uma+inconsist%C3%AAncia+nas+respostas+de+sua+aplica%C3%A7%C3%A3o%21+"
texto_link = 'Reportar Inconstência na resposta'


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title("💬 Chatbot")
st.caption('''🚀 Este é um chatbot que utiliza IA Generativa para responder perguntas. 
                Pergunte à vontade mas lembre-se que ele pode apresentar inconsistências nas respostas, por isso é importante avaliar cada uma. 
                Caso queira informar as inonsistências ocorridas clique no link abaixo.
            ''')
st.markdown(f"[{texto_link}]({url})")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Olá! Como posso ajudá-lo?"}
    ]

local_css("static/css/style.css")

initialize_session_state()

display_chat()

handle_user_input()
