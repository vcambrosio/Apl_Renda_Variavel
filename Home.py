import streamlit as st
st.set_page_config(
    page_title="Bem vindo!",
    page_icon="👋",
)
# Exibe a logomarca na barra lateral
st.logo("data\logo1.png", size="large")
st.write("# Welcome to Streamlit! 👋")
st.sidebar.success("Selecione uma aplicação acima")


st.markdown(
    """
  Nova versão do aplicativo de renda variavel
"""
)