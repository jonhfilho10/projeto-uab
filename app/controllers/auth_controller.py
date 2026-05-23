from flask import Blueprint, render_template, request, jsonify, session
from app.database.database import get_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET"])
def login():
    return render_template("auth/login.html")


@auth_bp.route("/api/login", methods=["POST"])
def api_login():
    dados = request.get_json()

    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({
            "success": False,
            "titulo": "Acesso Negado",
            "mensagem": "E-mail e senha são obrigatórios."
        }), 400

    db = get_db()

    usuario = db.execute(
        "SELECT * FROM usuarios WHERE email = ? AND senha = ? AND status = 'ativo'",
        (email, senha)
    ).fetchone()

    if not usuario:
        return jsonify({
            "success": False,
            "titulo": "Acesso Negado",
            "mensagem": "E-mail ou senha inválidos."
        }), 401

    session["usuario_id"] = usuario["id"]
    session["usuario_nome"] = usuario["nome"]
    session["usuario_perfil"] = usuario["perfil"]

    return jsonify({
        "success": True,
        "redirect": "/"
    })


@auth_bp.route("/logout")
def logout():
    session.clear()
    return render_template("auth/login.html")