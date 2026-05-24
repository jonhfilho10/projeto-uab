from flask import Blueprint, render_template, request, jsonify, session
from datetime import datetime, timedelta

from app.database.database import get_db
from app.utils.logs import registrar_log

auth_bp = Blueprint("auth", __name__)

tentativas_login = {}
MAX_TENTATIVAS = 5
TEMPO_BLOQUEIO_MINUTOS = 5


@auth_bp.route("/login", methods=["GET"])
def login():
    return render_template("auth/login.html")


@auth_bp.route("/api/login", methods=["POST"])
def api_login():
    dados = request.get_json() or {}

    email = dados.get("email", "").strip().lower()
    senha = dados.get("senha", "").strip()

    if not email or not senha:
        return jsonify({
            "success": False,
            "titulo": "Acesso Negado",
            "mensagem": "E-mail e senha são obrigatórios."
        }), 400

    agora = datetime.now()

    registro = tentativas_login.get(email)

    if registro and registro.get("bloqueado_ate"):
        if agora < registro["bloqueado_ate"]:
            return jsonify({
                "success": False,
                "titulo": "Acesso Bloqueado",
                "mensagem": "Muitas tentativas de login. Tente novamente em alguns minutos."
            }), 429

    db = get_db()

    usuario = db.execute("""
        SELECT *
        FROM usuarios
        WHERE email = ?
          AND senha = ?
          AND status = 'ativo'
    """, (email, senha)).fetchone()

    if not usuario:
        registro = tentativas_login.get(email, {
            "tentativas": 0,
            "bloqueado_ate": None
        })

        registro["tentativas"] += 1

        if registro["tentativas"] >= MAX_TENTATIVAS:
            registro["bloqueado_ate"] = agora + timedelta(
                minutes=TEMPO_BLOQUEIO_MINUTOS
            )
            registro["tentativas"] = 0

            registrar_log(
                "BLOQUEIO_LOGIN",
                "AUTENTICACAO",
                f"E-mail {email} bloqueado temporariamente por excesso de tentativas."
            )

            tentativas_login[email] = registro

            return jsonify({
                "success": False,
                "titulo": "Acesso Bloqueado",
                "mensagem": "Muitas tentativas de login. Tente novamente em alguns minutos."
            }), 429

        tentativas_login[email] = registro

        registrar_log(
            "LOGIN_FALHA",
            "AUTENTICACAO",
            f"Tentativa de login inválida para o e-mail {email}."
        )

        return jsonify({
            "success": False,
            "titulo": "Acesso Negado",
            "mensagem": "E-mail ou senha inválidos."
        }), 401

    tentativas_login.pop(email, None)

    session["usuario_id"] = usuario["id"]
    session["usuario_nome"] = usuario["nome"]
    session["usuario_perfil"] = usuario["perfil"]

    registrar_log(
        "LOGIN",
        "AUTENTICACAO",
        f"Usuário {email} realizou login com sucesso."
    )

    return jsonify({
        "success": True,
        "redirect": "/"
    })


@auth_bp.route("/logout")
def logout():
    usuario_nome = session.get("usuario_nome", "Usuário")

    registrar_log(
        "LOGOUT",
        "AUTENTICACAO",
        f"{usuario_nome} encerrou a sessão."
    )

    session.clear()

    return render_template("auth/login.html")