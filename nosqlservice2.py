from pymongo import MongoClient
from datetime import datetime
from flask import Blueprint, jsonify
from sql_service2 import ClienteService
from pymongo import MongoClient
from sqlalchemy import func
from datetime import datetime
from config import Config
from app import db
from app.models.cliente import Cliente
from app.models.produto import Produto
from app.models.venda   import Venda


bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard/total-clientes', methods=['GET'])
def total_clientes():
    total = ClienteService.contar()
    nosql = NoSQLService()
    nosql.salvar_total_clientes(total)
    return jsonify({'total_clientes': nosql.buscar_total_clientes()})


# MongoDB - Relatórios

@bp.route("/dashboard/total_clientes", methods=["GET"])
def dashboard_total_clientes():
    total = obter_dashboard_total()
    return jsonify({"total_clientes": total})



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