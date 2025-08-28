#!/usr/bin/env python3
import psycopg2
from datetime import date

# ---------- Configuração (senha agora ASCII) ----------
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "user":     "postgres",
    "password": "admin",          # troque se tiver acento
    "dbname":   "dbpos",
    "client_encoding": "utf8"     # força UTF-8
}

clientes = [
    ("Ana Silva",      "ana@email.com",   "12345678901", date(1990, 5, 12)),
    ("Bruno Costa",    "bruno@email.com", "98765432100", date(1985, 8, 25)),
    ("Carla Souza",    "carla@email.com", "11122233344", date(1992, 3, 17)),
    ("Diego Oliveira", "diego@email.com", "55566677788", date(1988, 11, 30)),
    ("Elaine Martins", "elaine@email.com","99988877766", date(1995, 7, 4))
]

create_table_sql = """
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    cpf VARCHAR(11) UNIQUE,
    data_nascimento DATE
);
"""

insert_sql = """
INSERT INTO clientes (nome, email, cpf, data_nascimento)
VALUES (%s, %s, %s, %s)
ON CONFLICT (cpf) DO NOTHING;
"""

def main():
    conn = cur = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute(create_table_sql)

        for nome, email, cpf, data_nascimento in clientes:
            cur.execute(insert_sql, (nome, email, cpf, data_nascimento))

        conn.commit()
        print("✅ 5 clientes inseridos com sucesso!")

    except Exception as e:
        print("❌ Erro:", e)
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()