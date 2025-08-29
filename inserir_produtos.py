import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app import create_app, db
from app.models.produto import Produto   # ajuste o import se necessário

produtos_seed = [
    {"nome": "Mouse Gamer RGB",           "preco": 129.90,  "descricao": "Mouse óptico 12.000 DPI, iluminação RGB.", "categoria": "Periféricos"},
    {"nome": "Teclado Mecânico 60%",      "preco": 299.90,  "descricao": "Switch azul, retroiluminado, compacto.",   "categoria": "Periféricos"},
    {"nome": "Monitor 27\" 144Hz",        "preco": 1899.00, "descricao": "IPS Full HD 144 Hz, 1 ms, FreeSync.",      "categoria": "Monitores"},
    {"nome": "Headset Wireless",          "preco": 349.90,  "descricao": "7.1 surround, bateria 30 h, microfone flex.", "categoria": "Áudio"},
    {"nome": "Webcam Full HD",            "preco": 199.90,  "descricao": "1080p 30 fps, foco automático, plug-and-play.", "categoria": "Periféricos"},
    {"nome": "Cadeira Gamer",             "preco": 899.00,  "descricao": "Reclinável, apoio lombar, couro sintético.", "categoria": "Móveis"},
    {"nome": "Mousepad XXL",              "preco": 89.90,   "descricao": "900×400 mm, base antiderrapante, costura reforçada.", "categoria": "Acessórios"},
    {"nome": "SSD 1TB NVMe",              "preco": 499.90,  "descricao": "Leitura 3.500 MB/s, M.2 2280.",            "categoria": "Armazenamento"},
    {"nome": "Placa RTX 4060 8GB",        "preco": 2599.00, "descricao": "Ray tracing DLSS 3, HDMI + 3 DP.",         "categoria": "Placas de Vídeo"},
    {"nome": "Fonte 650W 80+ Gold",       "preco": 399.90,  "descricao": "Modular, 80 Plus Gold, ventilador silencioso.", "categoria": "Componentes"},
    {"nome": "Memória 16GB DDR4 3200",    "preco": 299.90,  "descricao": "Kit 2×8 GB, dissipador em alumínio.",      "categoria": "Memória"},
    {"nome": "Processador Ryzen 5 5600",  "preco": 899.00,  "descricao": "6 núcleos 12 threads, 3.5~4.4 GHz.",       "categoria": "Processadores"},
    {"nome": "Notebook Gamer 15.6\"",     "preco": 4599.00, "descricao": "i7 11800H, RTX 3050, 16 GB RAM, SSD 512 GB.", "categoria": "Notebooks"},
    {"nome": "Hub USB-C 7 portas",        "preco": 149.90,  "descricao": "USB-A 3.0, HDMI 4K, leitor SD, PD 100 W.", "categoria": "Acessórios"},
    {"nome": "Controle Xbox Series",      "preco": 299.90,  "descricao": "Wireless, Bluetooth, compatível PC/Android.", "categoria": "Games"},
    {"nome": "Fone Bluetooth JBL",        "preco": 249.90,  "descricao": "ANC, 40 h bateria, carregamento rápido.",  "categoria": "Áudio"},
    {"nome": "Roteador Wi-Fi 6",          "preco": 399.90,  "descricao": "AX1800, 4 antenas, app de gerenciamento.", "categoria": "Redes"},
    {"nome": "Smartwatch Samsung",        "preco": 1299.00, "descricao": "Tela AMOLED, GPS, monitor cardíaco, 5 ATM.", "categoria": "Wearables"},
    {"nome": "Pen Drive 128GB USB 3.2",   "preco": 69.90,   "descricao": "Leitura 150 MB/s, corpo em metal.",         "categoria": "Armazenamento"},
    {"nome": "Cabo HDMI 2.1 2m",          "preco": 49.90,   "descricao": "8K 60 Hz, 48 Gbps, trançado de nylon.",    "categoria": "Cabo"},
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