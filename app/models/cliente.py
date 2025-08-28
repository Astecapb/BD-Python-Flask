from app import db
#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id_cliente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String (11), unique= True , nullable= True)
    data_nascimento=db.Column(db.Date , nullable=True)

    def to_dict(self):
        return {'id_cliente': self.id_cliente, 'nome': self.nome, 'email': self.email,'cpf':self.cpf,'data_nascimento':self.data_nascimento}
    
