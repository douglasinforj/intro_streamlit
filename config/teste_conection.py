from database import get_connection

def test_connection():
    try:
        connection = get_connection()

        if connection.is_connected():
            print("Conexão bem sucedida ao banco de dados!")

            #informação de servidor
            db_info = connection.get_server_info()
            print(f"Versão do servidor de Dados: {db_info}")

        #fechando conexão
        connection.close()
        print("conexão encerrada com sucesso.")
    except Exception as e:
        print(f"Erro ao testar a conexão: {e}")

# Executa o teste
if __name__=="__main__":
    test_connection()