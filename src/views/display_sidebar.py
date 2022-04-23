import streamlit as st
from utils.translate_words import translate_words


def display_sidebar():
    with st.sidebar:
        language = st.radio(
            "Language/Idioma",
            ("English/Inglês", "Portuguese/Português")
        )

    if language == "English/Inglês":
        language = "English"
    else:
        language = "Portuguese"
    
    return language
