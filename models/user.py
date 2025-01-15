import bcrypt
from config.database import get_connection

def create_user(usename, password):
    connection = get_connection()
    if not connection:
        return False
    
    hasshed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, hasshed_password.decode('utf8'))               #chamando a variavel para hash de senha
        connection.commit()
        return True

    except Exception as e:
        print(f"Erro ao criar o usuário: {e}")
        return False
    finally:
        connection.close()


def register_user(username, password):
    if create_user(username, password):
        return True, "Usuário registrado com sucesso!"
    return False, "Falha ao registrar usuário"


def authenticate_user(username, password):
    connection = get_connection()
    if not connection:
        return False
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return True
        return False
    finally:
        connection.close()
                                   