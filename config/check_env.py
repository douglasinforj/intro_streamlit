import os
from dotenv import load_dotenv

# Caminho absoluto para o .env
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

# Variáveis esperadas
expected_vars = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME", "DB_PORT"]

# Imprimir variáveis
print("Verificando variáveis do .env:")
for var in expected_vars:
    value = os.getenv(var)
    if value is not None:
        print(f"(OK) {var}: {value}")
    else:
        print(f"[ERRO] {var}: Variável não encontrada ou não carregada")
