import os
import sys
from random import randint, choice
from app import create_app,db
from app.models.cliente import Cliente
from app.models.produto import Produto
from app.models.venda import Venda

# garantir que roda dentro do contexto do app
app = create_app()
with app.app_context():
    # ---- 1. Clientes ----
    for i in range(1, 11):
        cli = Cliente(nome=f"Cliente {i}", email=f"cli{i}@mail.com")
        db.session.add(cli)
    db.session.commit()

    # ---- 2. Produtos ----
    for i in range(1, 31):
        prod = Produto(
            nome=f"Produto {i}",
            preco=round(randint(10, 1000) + 0.99, 2),
            estoque=randint(1, 100)
        )
        db.session.add(prod)
    db.session.commit()

    # ---- 3. Vendas ----
    clientes = Cliente.query.all()
    produtos = Produto.query.all()
    for i in range(20):
        c = choice(clientes)
        p = choice(produtos)
        qtd = randint(1, 5)
        total = round(float(p.preco) * qtd, 2)
        venda = Venda(
            cliente_id=c.id,
            produto_id=p.id,
            quantidade=qtd,
            valor_total=total
        )
        db.session.add(venda)
    db.session.commit()

    print("Seed concluído!")
    print(f"- {len(clientes)} clientes")
    print(f"- {len(produtos)} produtos")
    print(f"- {len(Venda.query.all())} vendas")