import streamlit as st
from views.home_views import home
from views.app1_views import app1
from views.app2_views import app2
from views.login_views import login
from views.register_views import register

# Inicializando estado de autenticação
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.show_register = False  # Adiciona controle para alternar login e registro

def set_show_register(value):  # Alterna entre login e registro
    st.session_state.show_register = value
    st.rerun()

# Função que gerencia login e registro
def auth_page():
    if st.session_state.show_register:
        register()  # Renderiza a view de registro
        if st.button("Já tem uma conta? Faça login"):
            set_show_register(False)
    else:
        login()  # Renderiza a view de login
        if st.button("Não tem uma conta? Registre-se"):
            set_show_register(True)

# Verifica a autenticação
if not st.session_state.authenticated:
    auth_page()  # Renderiza login ou registro
else:
    # Barra Lateral de navegação:
    st.sidebar.title(f"Bem Vindo, {st.session_state.username}")
    page = st.sidebar.radio("Navegação", ["Home", "App1", "App2"])  # Botão de navegação
    logout_button = st.sidebar.button("Logout")

    # Botão de logout
    if logout_button:
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.success("Logout efetuado com sucesso.") # Mensagem de feedback

        # Limpa os parâmetros da URL usando st.query_params
        st.rerun()

    # Renderiza páginas, conforme a escolha no botão radio
    if page == "Home":
        home()
    elif page == "App1":
        app1()
    elif page == "App2":
        app2()