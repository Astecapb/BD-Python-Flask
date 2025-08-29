from datetime import datetime
from app import db
from sqlalchemy.sql import func

from app.models.produto import Produto

class Venda(db.Model):
    __tablename__ = "vendas"

    id_pedido = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey("clientes.id_cliente"), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey("produtos.id_produto"), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    data_pedido = db.Column(db.DateTime, server_default=func.now())
    valor_total = db.Column(db.Float(10), nullable=False)

    # Relacionamentos
    cliente = db.relationship("Cliente", backref="pedidos")
    produto = db.relationship("Produto", backref="pedidos")

    def __init__(self, id_cliente, id_produto, quantidade=1):
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.quantidade = quantidade

        # Buscar preço do produto diretamente
        produto = db.session.get(Produto, id_produto)
        if produto is None:
            raise ValueError(f"Produto {id_produto} não encontrado.")

        self.valor_total = produto.preco * quantidade  # preço * quantidade

    def __repr__(self):
        return f"<Venda {self.id_pedido} - Cliente {self.id_cliente} - Produto {self.id_produto} - Qtd {self.quantidade}>"

    def to_dict(self):
        return {
            'id_pedido': self.id_pedido,
            'id_cliente': self.id_cliente,
            'id_produto': self.id_produto,
            'quantidade': self.quantidade,
            'data_pedido': self.data_pedido.isoformat() if self.data_pedido else None,
            'valor_total': float(self.valor_total)
        }
