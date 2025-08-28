from app import db

class Pedido(db.Model):
        __tablename__ = 'pedidos'
        id_pedido = db.Column(db.Integer, primary_key=True)
        id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
        data_pedido = db.Column(db.Date, nullable=False)
    
        def __repr__(self):
            return f'<Pedido {self.id_pedido}>'