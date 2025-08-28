from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:post1234@localhost:5432/dbpos')

try:
    connection = engine.connect()
    print("Conexão bem-sucedida!")
    connection.close()
except Exception as e:
    print(f"Erro na conexão: {e}")