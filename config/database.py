import mysql.connector
from mysql.connector import Error
from config.settings import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME,
            port = DB_PORT
        )
        
        return connection
        
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    
   