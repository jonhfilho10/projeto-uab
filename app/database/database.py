import sqlite3
from flask import g

DATABASE = "app/database/projeto_social.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            perfil TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'ativo',
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS modalidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            vagas INTEGER NOT NULL DEFAULT 0,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE,
            telefone TEXT,
            endereco TEXT,
            modalidade_id INTEGER,
            status TEXT NOT NULL DEFAULT 'ativo',
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (modalidade_id) REFERENCES modalidades(id)
        )
    """)


    usuario_admin = db.execute(
        "SELECT id FROM usuarios WHERE email = ?",
        ("jonhfilho@gmail.com",)
    ).fetchone()

    if usuario_admin is None:
        db.execute("""
            INSERT INTO usuarios (nome, email, senha, perfil, status)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "João Filho Borges Leite",
            "jonhfilho@gmail.com",
            "123456",
            "administrador",
            "ativo"
        ))

    db.commit()