import streamlit as st
from utils.translate_words import translate_words


def display_title(language):
    st.title(translate_words("title", language))
