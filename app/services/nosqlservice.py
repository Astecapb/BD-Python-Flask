from pymongo import MongoClient
from config import Config
from datetime import datetime

class NoSQLService:
    def __init__(self):
        self.mongo_connected = False
        try:
            self.client = MongoClient(
                Config.MONGO_URI,
                serverSelectionTimeoutMS=2000
            )
            self.client.server_info()              # ping
            self.mongo_db = self.client[Config.MONGO_DB]
            self.dashboard_collection = self.mongo_db[Config.MONGO_COLLECTION]
            self.mongo_connected = True
            print("[MongoDB] Conectado com sucesso")
        except Exception as e:
            print(f"[MongoDB] Aviso: não foi possível conectar: {e}")
            self.mongo_db = None
            self.dashboard_collection = None
            self.mongo_connected = False

    # CRUD genérico
    def registrar_documento(self, collection_name, filtro, valores):
        if self.mongo_connected:
            collection = self.mongo_db[collection_name]
            collection.update_one(
                filtro,
                {"$set": valores},
                upsert=True
            )
        else:
            print("[MongoDB] Registro ignorado (sem conexão)")

    def obter_documento(self, collection_name, filtro):
        if self.mongo_connected:
            collection = self.mongo_db[collection_name]
            return collection.find_one(filtro)
        return None

    # Helper específico
    def registrar_dashboard_total(self, total_clientes):
        self.registrar_documento(
            Config.MONGO_COLLECTION,
            {"_id": "total_clientes"},
            {"total": total_clientes, "atualizado_em": datetime.utcnow()}
        )