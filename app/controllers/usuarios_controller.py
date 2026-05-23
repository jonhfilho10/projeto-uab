from flask import Blueprint, render_template, jsonify, request, session
from app.database.database import get_db
from app.utils.auth import admin_required

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios")
@admin_required
def usuarios():
    return render_template("usuarios/listar.html")


@usuarios_bp.route("/api/usuarios", methods=["GET"])
@admin_required
def api_listar_usuarios():
    db = get_db()

    usuarios = db.execute("""
        SELECT id, nome, email, perfil, status, criado_em
        FROM usuarios
        ORDER BY nome ASC
    """).fetchall()

    lista = []

    for item in usuarios:
        lista.append({
            "id": item["id"],
            "nome": item["nome"],
            "email": item["email"],
            "perfil": item["perfil"],
            "status": item["status"],
            "criado_em": item["criado_em"]
        })

    return jsonify(lista)


@usuarios_bp.route("/api/usuarios", methods=["POST"])
@admin_required
def api_criar_usuario():
    dados = request.get_json()

    nome = dados.get("nome", "").strip()
    email = dados.get("email", "").strip()
    senha = dados.get("senha", "").strip()
    perfil = dados.get("perfil", "atendente").strip()
    status = dados.get("status", "ativo").strip()

    if not nome:
        return jsonify({"success": False, "mensagem": "O nome do usuário é obrigatório."}), 400

    if not email:
        return jsonify({"success": False, "mensagem": "O e-mail do usuário é obrigatório."}), 400

    if not senha:
        return jsonify({"success": False, "mensagem": "A senha do usuário é obrigatória."}), 400

    db = get_db()

    email_existente = db.execute(
        "SELECT id FROM usuarios WHERE email = ?",
        (email,)
    ).fetchone()

    if email_existente:
        return jsonify({"success": False, "mensagem": "Já existe um usuário cadastrado com este e-mail."}), 400

    db.execute("""
        INSERT INTO usuarios (nome, email, senha, perfil, status)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, email, senha, perfil, status))

    db.commit()

    return jsonify({"success": True, "mensagem": "Usuário cadastrado com sucesso."})


@usuarios_bp.route("/api/usuarios/<int:id>", methods=["PUT"])
@admin_required
def api_editar_usuario(id):
    dados = request.get_json()

    nome = dados.get("nome", "").strip()
    email = dados.get("email", "").strip()
    perfil = dados.get("perfil", "atendente").strip()
    status = dados.get("status", "ativo").strip()

    if not nome:
        return jsonify({"success": False, "mensagem": "O nome do usuário é obrigatório."}), 400

    if not email:
        return jsonify({"success": False, "mensagem": "O e-mail do usuário é obrigatório."}), 400

    db = get_db()

    usuario = db.execute(
        "SELECT id FROM usuarios WHERE id = ?",
        (id,)
    ).fetchone()

    if usuario is None:
        return jsonify({"success": False, "mensagem": "Usuário não encontrado."}), 404

    email_existente = db.execute(
        "SELECT id FROM usuarios WHERE email = ? AND id <> ?",
        (email, id)
    ).fetchone()

    if email_existente:
        return jsonify({"success": False, "mensagem": "Já existe outro usuário cadastrado com este e-mail."}), 400

    db.execute("""
        UPDATE usuarios
        SET nome = ?, email = ?, perfil = ?, status = ?
        WHERE id = ?
    """, (nome, email, perfil, status, id))

    db.commit()

    return jsonify({"success": True, "mensagem": "Usuário atualizado com sucesso."})


@usuarios_bp.route("/api/usuarios/<int:id>", methods=["DELETE"])
@admin_required
def api_excluir_usuario(id):
    if session.get("usuario_id") == id:
        return jsonify({
            "success": False,
            "mensagem": "Você não pode excluir o próprio usuário logado."
        }), 400

    db = get_db()

    usuario = db.execute(
        "SELECT id FROM usuarios WHERE id = ?",
        (id,)
    ).fetchone()

    if usuario is None:
        return jsonify({"success": False, "mensagem": "Usuário não encontrado."}), 404

    db.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    db.commit()

    return jsonify({"success": True, "mensagem": "Usuário excluído com sucesso."})