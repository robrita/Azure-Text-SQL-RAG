import streamlit as st


def show_home():
    st.set_page_config(
        page_title="Text to SQL and RAG",
        page_icon="🔀",
        # initial_sidebar_state="collapsed",
    )
    st.logo(
        "https://cdn-icons-png.flaticon.com/512/5151/5151840.png",
        link="https://ai.azure.com/",
    )
    st.title("🔀Text to SQL and RAG")
