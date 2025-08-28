from datetime import datetime
from app import db
from sqlalchemy.sql import func

class Venda(db.Model):
    __tablename__ = "pedidos"

    id_pedido = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey("clientes.id_cliente"), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey("produtos.id_produto"), nullable=False)
    data_pedido = db.Column(db.DateTime, server_default=func.now())
    valor_total = db.Column(db.Float(10), nullable=False)

    # Relacionamentos (apenas aqui, para evitar conflito)
    cliente = db.relationship("Cliente", backref="pedidos")
    produto = db.relationship("Produto", backref="pedidos")

    def __repr__(self):
        return f"<Venda {self.id_pedido} - Cliente {self.id_cliente} - Produto {self.id_produto}>"

   
    def to_dict(self):
        return {
            'id_pedido': self.id_pedido,
            'id_cliente': self.id_cliente,
            'id_produto': self.id_produto,
            'quantidade': self.quantidade,
            'data_pedido': self.data_pedido.isoformat(),
            'valor_total': float(self.valor_total)
            
        }