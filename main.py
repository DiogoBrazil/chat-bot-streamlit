import openai
from PIL import Image
import streamlit as st
from modules.chat import display_chat, handle_user_input
from utils.config import initialize_session_state

openai.api_key = st.secrets["OPENAI_API_KEY"]


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


image_url = './static/images/img02.png'

image = Image.open(image_url)

image = image.resize((700, 200))

st.image(image, use_column_width=True)
st.title("Assistente Virtual com IA Generativa")

local_css("static/css/style.css")

initialize_session_state()

display_chat()

handle_user_input()
