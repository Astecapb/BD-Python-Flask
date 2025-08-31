from app.models import Cliente, Produto, Venda
from sqlalchemy import func
from app import db

class ClienteService:
    @staticmethod
    def criar(nome, email): c = Cliente(nome=nome, email=email); db.session.add(c); db.session.commit(); return c
    @staticmethod
    def listar(): return Cliente.query.all()
    @staticmethod
    def buscar(id): return Cliente.query.get_or_404(id)
    @staticmethod
    def atualizar(id, **k): c = Cliente.query.get_or_404(id); [setattr(c, k, v) for k, v in k.items()]; db.session.commit(); return c
    @staticmethod
    def deletar(id): c = Cliente.query.get_or_404(id); db.session.delete(c); db.session.commit()
    @staticmethod
    def contar(): return Cliente.query.count()

class ProdutoService:
    @staticmethod
    def criar(nome, preco, estoque): p = Produto(nome=nome, preco=preco, estoque=estoque); db.session.add(p); db.session.commit(); return p
    @staticmethod
    def listar(): return Produto.query.all()
    @staticmethod
    def buscar(id): return Produto.query.get_or_404(id)
    @staticmethod
    def atualizar(id, **k): p = Produto.query.get_or_404(id); [setattr(p, k, v) for k, v in k.items()]; db.session.commit(); return p
    @staticmethod
    def deletar(id): p = Produto.query.get_or_404(id); db.session.delete(p); db.session.commit()
    @staticmethod
    def contar(): return Produto.query.count()

class VendaService:
    @staticmethod
    def criar(cliente_id, produto_id, quantidade, valor_total): v = Venda(**locals()); db.session.add(v); db.session.commit(); return v
    @staticmethod
    def listar(): return Venda.query.all()
    @staticmethod
    def buscar(id): return Venda.query.get_or_404(id)
    @staticmethod
    def atualizar(id, **k): v = Venda.query.get_or_404(id); [setattr(v, k, v) for k, v in k.items()]; db.session.commit(); return v
    @staticmethod
    def deletar(id): v = Venda.query.get_or_404(id); db.session.delete(v); db.session.commit()
    @staticmethod
    def contar(): return Venda.query.count()