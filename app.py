import streamlit as st 
from views.home_views import home
from views.app1_views import app1
from views.app2_views import app2
from views.login_views import login
from views.register_views import register

#inicializando estado autenticação
if "authenticated" not in st.session_state:
    st.session_state.authenticated  = False
    st.session_state.username = ""
    st.session_state.show_register = False #adiciona controle para alterarnar login e registro



#função que gerencia login e registro
def auth_page():
    if st.session_state.show_register:
        register()  # Renderiza a view de registro
        st.button("Já tem uma conta? Faça login", on_click=lambda: set_show_register(False))
    else:
        login()     #Renderiza login
        st.button("Não tem uma conta? Registre-se", on_click=lambda: set_show_register(True))   

def set_show_register(value):                    # Alterna entre login e registro
    st.session_state.show_register = value
    st.rerun()                                # não funciona: st.experimental_rerun()



# Verifica a autenticação
if not st.session_state.authenticated:
    auth_page()                                  #Renderiza login ou registro
else:
    #Barra Lateral de navegação:
    st.sidebar.title(f"Bem Vindo, {st.session_state.username}")
    page = st.sidebar.radio("Navegação", ["Home", "App1", "App2"])      #botão de navegação
    logout_button = st.sidebar.button("Logout")

    #botão de logout
    if logout_button:
        st.session_state.authenticated =False
        st.session_state.username = ""
        st.rerun()                                # não funciona: st.experimental_rerun()


    # Renderiza páginas, confome a escolha no botão radio
    if page == "Home":
        home()
    elif page == "App1":
        app1()
    elif page == "App2":
        app2
