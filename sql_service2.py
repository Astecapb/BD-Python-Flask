import datetime
from app.models import db, Cliente, Produto, Venda
from app.models.cliente import Cliente
from app.models.produto import Produto
from app.models.venda import Venda




class ClienteService:
    @staticmethod
    def criar_cliente(nome, email,cpf,data_nascimento):
        cliente = Cliente(nome=nome, email=email,cpf=cpf,data_nascimento=datetime.strptime(data_nascimento,"%Y-%m-%d").date())
        db.session.add(cliente)
        db.session.commit()
        return cliente

    @staticmethod
    def listar_clientes():
        return Cliente.query.all()

    @staticmethod
    def obter_clienter(id):
        return Cliente.query.get(id)

    @staticmethod
    def atualizar_cliente(id_cliente, nome, email,cpf,data_nascimento):
        cliente = Cliente.query.get(id_cliente)
        if cliente:
            cliente.nome = nome
            cliente.email = email
            cliente.cpf = cpf
            cliente.data_nascimento=datetime.strptime(data_nascimento,"%Y-%m-%d").date()
            db.session.add(cliente)
            db.session.commit()
        return cliente

    @staticmethod
    def deletar_cliente(id):
        cliente = Cliente.query.get(id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            return cliente

    @staticmethod
    def contar():
        return Cliente.query.count()
    ######################################################
    
class ProdutoService:
    @staticmethod
    def criar(nome, preco, estoque=0):
        produto = Produto(nome=nome, preco=preco, estoque=estoque)
        db.session.add(produto)
        db.session.commit()
        return produto

    @staticmethod
    def listar():
        return Produto.query.all()

    @staticmethod
    def buscar(id):
        return Produto.query.get(id)

    @staticmethod
    def atualizar(id, nome, preco, estoque):
        produto = Produto.query.get(id)
        if produto:
            produto.nome = nome
            produto.preco = preco
            produto.estoque = estoque
            db.session.commit()
        return produto

    @staticmethod
    def deletar(id):
        produto = Produto.query.get(id)
        if produto:
            db.session.delete(produto)
            db.session.commit()
###############################################################################

class VendaService:
    @staticmethod
    def criar(cliente_id, produto_id, quantidade, valor_total):
        venda = Venda(
            cliente_id=cliente_id,
            produto_id=produto_id,
            quantidade=quantidade,
            valor_total=valor_total
        )
        db.session.add(venda)
        db.session.commit()
        return venda

    @staticmethod
    def listar():
        return Venda.query.all()

    @staticmethod
    def buscar(id):
        return Venda.query.get(id)

    @staticmethod
    def atualizar(id, cliente_id, produto_id, quantidade, valor_total):
        venda = Venda.query.get(id)
        if venda:
            venda.cliente_id = cliente_id
            venda.produto_id = produto_id
            venda.quantidade = quantidade
            venda.valor_total = valor_total
            db.session.commit()
        return venda

    @staticmethod
    def deletar(id):
        venda = Venda.query.get(id)
        if venda:
            db.session.delete(venda)
            db.session.commit()
