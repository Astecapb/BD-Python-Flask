from app import db

class Produto(db.Model):
    __tablename__ = 'produtos'

    id_produto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(500), nullable=True)
    categoria = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {'id_produto': self.id_produto, 'nome': self.nome, 'preco':
            self.preco, 'descricao': self.descricao, 'categoria':self.categoria}