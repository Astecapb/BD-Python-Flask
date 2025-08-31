import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app import create_app, db
from app.models.produto import Produto   # ajuste o import se necessário

produtos_seed = [
    {"nome": "Tablet Android 10\"",       "preco": 1599.00, "descricao": "Octa-core, 6 GB RAM, 128 GB SSD.",         "categoria": "Tablets"},
    {"nome": "Impressora Multifuncional", "preco": 799.00,  "descricao": "Jato de tinta, Wi-Fi, scanner integrado.", "categoria": "Impressoras"},
    {"nome": "HD Externo 2TB",            "preco": 399.00,  "descricao": "USB 3.2, portátil, case resistente.",      "categoria": "Armazenamento"},
    {"nome": "Câmera de Segurança Wi-Fi", "preco": 299.00,  "descricao": "1080p, visão noturna, app mobile.",        "categoria": "Segurança"},
    {"nome": "Estabilizador 1000VA",      "preco": 349.00,  "descricao": "Proteção contra surtos, 6 tomadas.",       "categoria": "Energia"},
    {"nome": "Console PlayStation 5",     "preco": 4599.00, "descricao": "SSD ultrarrápido, controle DualSense.",    "categoria": "Games"},
    {"nome": "Alexa Echo Dot 5ª Gen",     "preco": 349.00,  "descricao": "Assistente virtual com som premium.",      "categoria": "Smart Home"},
    {"nome": "Cooler para CPU RGB",       "preco": 199.00,  "descricao": "120 mm, heat pipes, compatível Intel/AMD.", "categoria": "Componentes"},
    {"nome": "Teclado sem fio Logitech",  "preco": 199.90,  "descricao": "Compacto, conexão 2.4 GHz + Bluetooth.",   "categoria": "Periféricos"},
    {"nome": "Cadeira de Escritório",     "preco": 699.00,  "descricao": "Ergonômica, malha respirável, regulagem completa.", "categoria": "Móveis"},
]

def seed():
    app = create_app()
    with app.app_context():
        db.create_all()
        if Produto.query.count() == 0:
            for p in produtos_seed:
                db.session.add(Produto(**p))
            db.session.commit()
            print("✅ 20 produtos inseridos com sucesso!")
        else:
            print("ℹ️  Tabela produtos já possui dados.")

if __name__ == "__main__":
    seed()