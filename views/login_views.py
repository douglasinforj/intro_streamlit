import streamlit as st 
from controllers.auth_controller import login_user

def login():
    st.title("Login")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type='password')
    login_button = st.button("Entrar")

    if login_button:
        authenticated, message = login_user(username, password)
        if authenticated:
            st.session_state.authenticated =True
            st.session_state.username = username
            st.success(message)
            st.st.rerun()
        else:
            st.error(message)