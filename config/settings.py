import os
from dotenv import load_dotenv

# caminho para .env
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

#carrega .env
load_dotenv(dotenv_path=env_path)

#configurações para o banco
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT"))