import streamlit as st 
from controllers.auth_controller import register_user


def register():
    st.title("Registro")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    register_button = st.button("Registrar")

    if register_button:
        success, message = register_user(username, password)
        if success:
            st.success(message)
        else:
            st.error(message)