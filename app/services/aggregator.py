from pymongo import MongoClient
from app import db
from app.models.venda import Venda
from datetime import datetime, timedelta
from config import Config

class DataAggregator:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client[Config.MONGO_DB]
        self.collection = self.db['vendas_agregadas']
    
    def aggregate_vendas_diarias(self):
        """Agrega vendas por dia"""
        vendas = db.session.query(
            db.func.date(Venda.data_venda).label('data'),
            db.func.sum(Venda.valor_total).label('total_vendas'),
            db.func.count(Venda.id).label('quantidade_vendas')
        ).group_by(db.func.date(Venda.data_venda)).all()
        
        # Salvar no MongoDB
        for venda in vendas:
            self.collection.update_one(
                {'data': str(venda.data)},
                {'$set': {
                    'total_vendas': float(venda.total_vendas),
                    'quantidade_vendas': venda.quantidade_vendas,
                    'atualizado_em': datetime.now()
                }},
                upsert=True
            )
    
    def get_dashboard_data(self):
        """Retorna dados para dashboard"""
        return list(self.collection.find({}, {'_id': 0}))