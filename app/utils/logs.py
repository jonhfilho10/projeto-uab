from flask import session
from app.database.database import get_db


def registrar_log(acao, modulo, descricao):
    try:
        db = get_db()

        usuario_id = session.get("usuario_id")

        db.execute("""
            INSERT INTO logs (usuario_id, acao, modulo, descricao)
            VALUES (?, ?, ?, ?)
        """, (usuario_id, acao, modulo, descricao))

        db.commit()

    except Exception:
        pass
