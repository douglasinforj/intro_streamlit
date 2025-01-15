from models.user import authenticate_user, create_user

def login_user(username, password):
    if authenticate_user(username, password):
        return True, "Login realizado com sucesso!"
    return False, "Usuário ou senha incorretos"

def register_user(username, password):
    if create_user(username, password):
        return True, "Usuário registrado com sucesso!"
    return False, "Falha ao registrar usuário!"

