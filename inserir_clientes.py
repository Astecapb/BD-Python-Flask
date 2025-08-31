#!/usr/bin/env python3
import psycopg2
from datetime import date

# ---------- Configuração (senha agora ASCII) ----------
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "user":     "postgres",
    "password": "post1234",          # troque se tiver acento
    "dbname":   "dbpos",
    "client_encoding": "utf8"     # força UTF-8
}

clientes = [
    ("Fernando Lima",  "fernando@email.com", "22233344455", date(1991, 1, 22)),
    ("Gabriela Rocha","gabriela@email.com", "33344455566", date(1994, 6, 14)),
    ("Henrique Alves","henrique@email.com", "44455566677", date(1989, 12, 9)),
    ("Isabela Torres","isabela@email.com",  "55544433322", date(1997, 4, 2)),
    ("João Mendes",   "joao@email.com",     "66677788899", date(1983, 7, 15)),
    ("Karen Dias",    "karen@email.com",    "77788899900", date(1996, 9, 20)),
    ("Lucas Pereira", "lucas@email.com",    "88899900011", date(1990, 10, 5)),
    ("Mariana Lopes", "mariana@email.com",  "99900011122", date(1987, 2, 28)),
    ("Pedro Santos",  "pedro@email.com",    "11100099988", date(1993, 3, 8)),
    ("Renata Freitas","renata@email.com",   "22211133344", date(1998, 12, 25))
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