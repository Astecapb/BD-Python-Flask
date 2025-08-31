from pymongo import MongoClient
from config import Config

try:
    client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")  # Força uma verificação
    print("✅ Conectado ao MongoDB!")
    print("📦 Bancos disponíveis:", client.list_database_names())
except Exception as e:
    print("❌ Erro ao conectar:", e)