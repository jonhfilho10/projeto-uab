from flask import Blueprint, render_template, jsonify, request
from app.database.database import get_db
from app.utils.auth import login_required

alunos_bp = Blueprint("alunos", __name__)


@alunos_bp.route("/alunos")
@login_required
def alunos():
    return render_template("alunos/listar.html")


@alunos_bp.route("/api/alunos", methods=["GET"])
@login_required
def api_listar_alunos():
    db = get_db()

    alunos = db.execute("""
        SELECT 
            a.id,
            a.nome,
            a.cpf,
            a.telefone,
            a.endereco,
            a.status,
            a.modalidade_id,
            a.criado_em,
            m.nome AS modalidade_nome
        FROM alunos a
        LEFT JOIN modalidades m ON m.id = a.modalidade_id
        ORDER BY a.nome ASC
    """).fetchall()

    lista = []

    for item in alunos:
        lista.append({
            "id": item["id"],
            "nome": item["nome"],
            "cpf": item["cpf"],
            "telefone": item["telefone"],
            "endereco": item["endereco"],
            "status": item["status"],
            "modalidade_id": item["modalidade_id"],
            "modalidade_nome": item["modalidade_nome"],
            "criado_em": item["criado_em"]
        })

    return jsonify(lista)


@alunos_bp.route("/api/alunos", methods=["POST"])
@login_required
def api_criar_aluno():
    dados = request.get_json()

    nome = dados.get("nome", "").strip()
    cpf = dados.get("cpf", "").strip()
    telefone = dados.get("telefone", "").strip()
    endereco = dados.get("endereco", "").strip()
    modalidade_id = dados.get("modalidade_id")
    status = dados.get("status", "ativo").strip()

    if not nome:
        return jsonify({"success": False, "mensagem": "O nome do participante é obrigatório."}), 400

    if not cpf:
        return jsonify({"success": False, "mensagem": "O CPF do participante é obrigatório."}), 400

    if not telefone:
        return jsonify({"success": False, "mensagem": "O telefone do participante é obrigatório."}), 400

    if not endereco:
        return jsonify({"success": False, "mensagem": "O endereço do participante é obrigatório."}), 400

    if not modalidade_id:
        return jsonify({"success": False, "mensagem": "A modalidade é obrigatória."}), 400

    db = get_db()

    cpf_existente = db.execute(
        "SELECT id FROM alunos WHERE cpf = ?",
        (cpf,)
    ).fetchone()

    if cpf_existente:
        return jsonify({
            "success": False,
            "mensagem": "Já existe um participante cadastrado com este CPF."
        }), 400

    modalidade = db.execute("""
        SELECT 
            m.id,
            m.nome,
            m.vagas,
            COUNT(a.id) AS total_participantes
        FROM modalidades m
        LEFT JOIN alunos a ON a.modalidade_id = m.id
        WHERE m.id = ?
        GROUP BY m.id
    """, (modalidade_id,)).fetchone()

    if modalidade is None:
        return jsonify({
            "success": False,
            "mensagem": "Modalidade não encontrada."
        }), 404

    if modalidade["total_participantes"] >= modalidade["vagas"]:
        return jsonify({
            "success": False,
            "mensagem": f"A modalidade {modalidade['nome']} já atingiu o limite de {modalidade['vagas']} participantes."
        }), 400

    db.execute("""
        INSERT INTO alunos (nome, cpf, telefone, endereco, modalidade_id, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, cpf, telefone, endereco, modalidade_id, status))

    db.commit()

    return jsonify({
        "success": True,
        "mensagem": "Participante cadastrado com sucesso."
    })


@alunos_bp.route("/api/alunos/<int:id>", methods=["PUT"])
@login_required
def api_editar_aluno(id):
    dados = request.get_json()

    nome = dados.get("nome", "").strip()
    cpf = dados.get("cpf", "").strip()
    telefone = dados.get("telefone", "").strip()
    endereco = dados.get("endereco", "").strip()
    modalidade_id = dados.get("modalidade_id")
    status = dados.get("status", "ativo").strip()

    if not nome:
        return jsonify({"success": False, "mensagem": "O nome do participante é obrigatório."}), 400

    if not cpf:
        return jsonify({"success": False, "mensagem": "O CPF do participante é obrigatório."}), 400

    if not telefone:
        return jsonify({"success": False, "mensagem": "O telefone do participante é obrigatório."}), 400

    if not endereco:
        return jsonify({"success": False, "mensagem": "O endereço do participante é obrigatório."}), 400

    if not modalidade_id:
        return jsonify({"success": False, "mensagem": "A modalidade é obrigatória."}), 400

    db = get_db()

    aluno = db.execute(
        "SELECT id FROM alunos WHERE id = ?",
        (id,)
    ).fetchone()

    if aluno is None:
        return jsonify({
            "success": False,
            "mensagem": "Participante não encontrado."
        }), 404

    cpf_existente = db.execute(
        "SELECT id FROM alunos WHERE cpf = ? AND id <> ?",
        (cpf, id)
    ).fetchone()

    if cpf_existente:
        return jsonify({
            "success": False,
            "mensagem": "Já existe outro participante cadastrado com este CPF."
        }), 400

    modalidade = db.execute("""
        SELECT 
            m.id,
            m.nome,
            m.vagas,
            COUNT(a.id) AS total_participantes
        FROM modalidades m
        LEFT JOIN alunos a 
            ON a.modalidade_id = m.id
            AND a.id <> ?
        WHERE m.id = ?
        GROUP BY m.id
    """, (id, modalidade_id)).fetchone()

    if modalidade is None:
        return jsonify({
            "success": False,
            "mensagem": "Modalidade não encontrada."
        }), 404

    if modalidade["total_participantes"] >= modalidade["vagas"]:
        return jsonify({
            "success": False,
            "mensagem": f"A modalidade {modalidade['nome']} já atingiu o limite de {modalidade['vagas']} participantes."
        }), 400

    db.execute("""
        UPDATE alunos
        SET nome = ?, cpf = ?, telefone = ?, endereco = ?, modalidade_id = ?, status = ?
        WHERE id = ?
    """, (nome, cpf, telefone, endereco, modalidade_id, status, id))

    db.commit()

    return jsonify({
        "success": True,
        "mensagem": "Participante atualizado com sucesso."
    })


@alunos_bp.route("/api/alunos/<int:id>", methods=["DELETE"])
@login_required
def api_excluir_aluno(id):
    db = get_db()

    aluno = db.execute(
        "SELECT id FROM alunos WHERE id = ?",
        (id,)
    ).fetchone()

    if aluno is None:
        return jsonify({
            "success": False,
            "mensagem": "Participante não encontrado."
        }), 404

    db.execute("DELETE FROM alunos WHERE id = ?", (id,))
    db.commit()

    return jsonify({
        "success": True,
        "mensagem": "Participante excluído com sucesso."
    })