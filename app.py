import streamlit as st
from views.home_views import home
from views.app1_views import app1
from views.app2_views import app2
from views.login_views import login
from views.register_views import register
from streamlit_js_eval import streamlit_js_eval

# Funções JavaScript (agora usando streamlit_js_eval diretamente)
def get_cookie(cookie_name):
    return streamlit_js_eval(js_expressions="document.cookie.split(';').find(row => row.trim().startsWith('" + cookie_name + "=" + "'))?.split('=')[1]")

def set_cookie(cookie_name, cookie_value, days):
    streamlit_js_eval(js_expressions="let date = new Date(); date.setTime(date.getTime() + (" + str(days) + "*24*60*60*1000)); document.cookie = '" + cookie_name + "=" + cookie_value + "; expires=' + date.toUTCString() + '; path=/'")

def delete_cookie(cookie_name):
    streamlit_js_eval(js_expressions="document.cookie = '" + cookie_name + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;'")


def set_show_register(value):
    st.session_state.show_register = value
    st.rerun()

def auth_page():
    if st.session_state.show_register:
        register()
        if st.button("Já tem uma conta? Faça login"):
            set_show_register(False)
    else:
        if login(): # Modificação crucial aqui!
            # Lógica de cookies MOVIDA para cá, APÓS o login() retornar True
            set_cookie("authenticated", "True", 30)
            set_cookie("username", st.session_state.username, 30)
            st.rerun() #redireciona para a pagina principal
        if st.button("Não tem uma conta? Registre-se"):
            set_show_register(True)


# Inicializando estado de autenticação (verifica os cookies PRIMEIRO)
if "authenticated" not in st.session_state:
    auth_cookie = get_cookie("authenticated")
    if auth_cookie == "True":
        st.session_state.authenticated = True
        st.session_state.username = get_cookie("username")
    else:
        st.session_state.authenticated = False
        st.session_state.username = ""
    st.session_state.show_register = False

# Verifica a autenticação DEPOIS de verificar os cookies
if not st.session_state.authenticated:
    auth_page()
else:
    st.sidebar.title(f"Bem Vindo, {st.session_state.username}")
    page = st.sidebar.radio("Navegação", ["Home", "App1", "App2"])
    logout_button = st.sidebar.button("Logout")

    if logout_button:
        st.session_state.authenticated = False
        st.session_state.username = ""
        delete_cookie("authenticated")
        delete_cookie("username")
        st.rerun()

    if page == "Home":
        home()
    elif page == "App1":
        app1()
    elif page == "App2":
        app2()

