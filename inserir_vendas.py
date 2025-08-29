from app import create_app, db
from app.models import Venda, Cliente, Produto
import random
from datetime import datetime

app = create_app()

with app.app_context():
    clientes = Cliente.query.all()
    produtos = Produto.query.all()

    if not clientes or not produtos:
        print("⚠️ É necessário ter clientes e produtos cadastrados antes de inserir vendas.")
    else:
        vendas = []
        for i in range(20):
            cliente = random.choice(clientes)
            produto = random.choice(produtos)
            quantidade = random.randint(1, 5)

            venda = Venda(
                id_cliente=cliente.id_cliente,
                id_produto=produto.id_produto,
                quantidade=quantidade
            )
            vendas.append(venda)

        db.session.add_all(vendas)
        db.session.commit()
        print("✅ 20 vendas inseridas com sucesso!")
