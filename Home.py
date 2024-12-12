import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Bem vindo!",
    page_icon="👋",
)

# Exibe a logomarca na barra lateral, acima de tudo
st.sidebar.image("data/logo1.png", width=200)

# Mensagem principal na página
st.write("# Welcome to Streamlit! 👋")

# Mensagem na barra lateral
st.sidebar.success("Selecione uma aplicação acima")

# Texto adicional
st.markdown(
    """
  Nova versão do aplicativo de renda variável
"""
)
