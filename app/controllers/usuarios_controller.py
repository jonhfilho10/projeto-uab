from flask import Blueprint, render_template, jsonify, request, session
from app.database.database import get_db
from app.utils.auth import admin_required
from app.utils.respostas import resposta_sucesso, resposta_erro
from app.utils.logs import registrar_log
from app.utils.validacoes import limpar_texto, validar_email

usuarios_bp = Blueprint("usuarios", __name__)

PERFIS_VALIDOS = ["administrador", "atendente", "cliente"]
STATUS_VALIDOS = ["ativo", "inativo"]


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
    dados = request.get_json() or {}

    nome = limpar_texto(dados.get("nome"))
    email = limpar_texto(dados.get("email")).lower()
    senha = limpar_texto(dados.get("senha"))
    perfil = limpar_texto(dados.get("perfil", "atendente"))
    status = limpar_texto(dados.get("status", "ativo"))

    if not nome:
        return resposta_erro("O nome do usuário é obrigatório.", 400)

    if not email:
        return resposta_erro("O e-mail do usuário é obrigatório.", 400)

    if not validar_email(email):
        return resposta_erro("E-mail inválido.", 400)

    if not senha:
        return resposta_erro("A senha do usuário é obrigatória.", 400)

    if perfil not in PERFIS_VALIDOS:
        return resposta_erro("Perfil de usuário inválido.", 400)

    if status not in STATUS_VALIDOS:
        return resposta_erro("Status de usuário inválido.", 400)

    db = get_db()

    email_existente = db.execute(
        "SELECT id FROM usuarios WHERE email = ?",
        (email,)
    ).fetchone()

    if email_existente:
        return resposta_erro(
            "Já existe um usuário cadastrado com este e-mail.",
            400
        )

    db.execute("""
        INSERT INTO usuarios (
            nome,
            email,
            senha,
            perfil,
            status
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        nome,
        email,
        senha,
        perfil,
        status
    ))

    db.commit()

    registrar_log(
        "CADASTRO",
        "USUARIOS",
        f"Usuário {nome} cadastrado no sistema."
    )

    return resposta_sucesso("Usuário cadastrado com sucesso.")


@usuarios_bp.route("/api/usuarios/<int:id>", methods=["PUT"])
@admin_required
def api_editar_usuario(id):
    dados = request.get_json() or {}

    nome = limpar_texto(dados.get("nome"))
    email = limpar_texto(dados.get("email")).lower()
    perfil = limpar_texto(dados.get("perfil", "atendente"))
    status = limpar_texto(dados.get("status", "ativo"))

    if not nome:
        return resposta_erro("O nome do usuário é obrigatório.", 400)

    if not email:
        return resposta_erro("O e-mail do usuário é obrigatório.", 400)

    if not validar_email(email):
        return resposta_erro("E-mail inválido.", 400)

    if perfil not in PERFIS_VALIDOS:
        return resposta_erro("Perfil de usuário inválido.", 400)

    if status not in STATUS_VALIDOS:
        return resposta_erro("Status de usuário inválido.", 400)

    db = get_db()

    usuario = db.execute(
        "SELECT id FROM usuarios WHERE id = ?",
        (id,)
    ).fetchone()

    if usuario is None:
        return resposta_erro("Usuário não encontrado.", 404)

    email_existente = db.execute(
        "SELECT id FROM usuarios WHERE email = ? AND id <> ?",
        (email, id)
    ).fetchone()

    if email_existente:
        return resposta_erro(
            "Já existe outro usuário cadastrado com este e-mail.",
            400
        )

    db.execute("""
        UPDATE usuarios
        SET nome = ?,
            email = ?,
            perfil = ?,
            status = ?
        WHERE id = ?
    """, (
        nome,
        email,
        perfil,
        status,
        id
    ))

    db.commit()

    registrar_log(
        "UPDATE",
        "USUARIOS",
        f"Usuário {nome} alterado no sistema."
    )

    return resposta_sucesso("Usuário atualizado com sucesso.")


@usuarios_bp.route("/api/usuarios/<int:id>", methods=["DELETE"])
@admin_required
def api_excluir_usuario(id):
    if session.get("usuario_id") == id:
        return resposta_erro(
            "Você não pode excluir o próprio usuário logado.",
            400
        )

    db = get_db()

    usuario = db.execute(
        "SELECT id, nome FROM usuarios WHERE id = ?",
        (id,)
    ).fetchone()

    if usuario is None:
        return resposta_erro("Usuário não encontrado.", 404)

    db.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (id,)
    )

    db.commit()

    registrar_log(
        "EXCLUSAO",
        "USUARIOS",
        f"Usuário {usuario['nome']} excluído do sistema pelo administrador autenticado."
    )

    return resposta_sucesso("Usuário excluído com sucesso.")