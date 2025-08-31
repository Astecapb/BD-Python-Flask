from datetime import datetime
from pymongo import MongoClient
from sqlalchemy import func
from config import Config
from app.models import Cliente, Produto, Venda
from app import db


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

    # -----------------------------------------------------------
    # Dashboard consolidado
    # -----------------------------------------------------------
    def atualizar_dashboard(self):
        if not self.mongo_connected:
            print("[MongoDB] atualizar_dashboard ignorado (sem conexão)")
            return

        total_clientes = Cliente.query.count()
        total_produtos = Produto.query.count()
        total_vendas   = Venda.query.count()

        top_produto = (
            db.session.query(
                Venda.id_produto,
                func.sum(Venda.quantidade).label('qtd')
            )
            .group_by(Venda.id_produto)
            .order_by(func.sum(Venda.quantidade).desc())
            .first()
        )

        prod_dict = None
        if top_produto:
            p = Produto.query.get(top_produto.id_produto)
            if p:
                prod_dict = {
                    'id': p.id_produto,
                    'nome': p.nome,
                    'qtd_vendida': int(top_produto.qtd)
                }

        doc = {
            '_id': 'dashboard',
            'total_clientes': total_clientes,
            'total_produtos': total_produtos,
            'total_vendas': total_vendas,
            'produto_mais_vendido': prod_dict,
            'atualizado_em': datetime.utcnow()
        }

        self.dashboard_collection.replace_one(
            {'_id': 'dashboard'}, doc, upsert=True
        )

    def obter_dashboard(self):
        """Retorna o documento dashboard do MongoDB."""
        if not self.mongo_connected:
            return None
        return self.dashboard_collection.find_one({'_id': 'dashboard'})

    # -----------------------------------------------------------
    # CRUD genérico
    # -----------------------------------------------------------
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