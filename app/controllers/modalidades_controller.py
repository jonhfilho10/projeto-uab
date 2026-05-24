from flask import Blueprint, render_template, jsonify, request
from app.database.database import get_db
from app.utils.auth import login_required
from app.utils.logs import registrar_log
from app.utils.respostas import resposta_sucesso, resposta_erro
from app.utils.validacoes import limpar_texto, validar_inteiro_positivo

modalidades_bp = Blueprint("modalidades", __name__)


@modalidades_bp.route("/modalidades")
@login_required
def modalidades():
    return render_template("modalidades/listar.html")


@modalidades_bp.route("/api/modalidades", methods=["GET"])
@login_required
def api_listar_modalidades():
    db = get_db()

    modalidades = db.execute("""
        SELECT 
            m.id,
            m.nome,
            m.descricao,
            m.vagas,
            m.criado_em,
            COUNT(a.id) AS total_participantes
        FROM modalidades m
        LEFT JOIN alunos a 
            ON a.modalidade_id = m.id 
            AND a.status = 'ativo'
        GROUP BY m.id
        ORDER BY m.nome ASC
    """).fetchall()

    lista = []

    for item in modalidades:
        vagas = item["vagas"] or 0
        total = item["total_participantes"] or 0
        disponiveis = vagas - total

        percentual = 0

        if vagas > 0:
            percentual = round((total / vagas) * 100, 2)

        lista.append({
            "id": item["id"],
            "nome": item["nome"],
            "descricao": item["descricao"],
            "vagas": vagas,
            "total_participantes": total,
            "vagas_disponiveis": disponiveis,
            "percentual_ocupacao": percentual,
            "criado_em": item["criado_em"]
        })

    return jsonify(lista)


@modalidades_bp.route("/api/modalidades", methods=["POST"])
@login_required
def api_criar_modalidade():
    dados = request.get_json() or {}

    nome = limpar_texto(dados.get("nome"))
    descricao = limpar_texto(dados.get("descricao"))
    vagas = dados.get("vagas", 0)

    if not nome:
        return resposta_erro(
            "O nome da modalidade é obrigatório.",
            400
        )

    if not descricao:
        return resposta_erro(
            "A descrição da modalidade é obrigatória.",
            400
        )

    if not validar_inteiro_positivo(vagas):
        return resposta_erro(
            "A quantidade de vagas deve ser maior que zero.",
            400
        )

    vagas = int(vagas)

    db = get_db()

    db.execute("""
        INSERT INTO modalidades (
            nome,
            descricao,
            vagas
        )
        VALUES (?, ?, ?)
    """, (
        nome,
        descricao,
        vagas
    ))

    db.commit()

    registrar_log(
        "CADASTRO",
        "MODALIDADE",
        f"Modalidade {nome} cadastrada no sistema."
    )

    return resposta_sucesso(
        "Modalidade cadastrada com sucesso."
    )


@modalidades_bp.route("/api/modalidades/<int:id>", methods=["PUT"])
@login_required
def api_editar_modalidade(id):
    dados = request.get_json() or {}

    nome = limpar_texto(dados.get("nome"))
    descricao = limpar_texto(dados.get("descricao"))
    vagas = dados.get("vagas", 0)

    if not nome:
        return resposta_erro(
            "O nome da modalidade é obrigatório.",
            400
        )

    if not descricao:
        return resposta_erro(
            "A descrição da modalidade é obrigatória.",
            400
        )

    if not validar_inteiro_positivo(vagas):
        return resposta_erro(
            "A quantidade de vagas deve ser maior que zero.",
            400
        )

    vagas = int(vagas)

    db = get_db()

    modalidade = db.execute(
        "SELECT id FROM modalidades WHERE id = ?",
        (id,)
    ).fetchone()

    if modalidade is None:
        return resposta_erro(
            "Modalidade não encontrada.",
            404
        )

    db.execute("""
        UPDATE modalidades
        SET nome = ?,
            descricao = ?,
            vagas = ?
        WHERE id = ?
    """, (
        nome,
        descricao,
        vagas,
        id
    ))

    db.commit()

    registrar_log(
        "UPDATE",
        "MODALIDADE",
        f"Modalidade {nome} atualizada no sistema."
    )

    return resposta_sucesso(
        "Modalidade atualizada com sucesso."
    )


@modalidades_bp.route("/api/modalidades/<int:id>", methods=["DELETE"])
@login_required
def api_excluir_modalidade(id):
    db = get_db()

    modalidade = db.execute(
        "SELECT id, nome FROM modalidades WHERE id = ?",
        (id,)
    ).fetchone()

    if modalidade is None:
        return resposta_erro(
            "Modalidade não encontrada.",
            404
        )

    alunos_vinculados = db.execute(
        "SELECT COUNT(*) AS total FROM alunos WHERE modalidade_id = ?",
        (id,)
    ).fetchone()

    if alunos_vinculados["total"] > 0:
        return resposta_erro(
            "Não é possível excluir esta modalidade, pois existem participantes vinculados.",
            400
        )

    db.execute(
        "DELETE FROM modalidades WHERE id = ?",
        (id,)
    )

    db.commit()

    registrar_log(
        "EXCLUSAO",
        "MODALIDADE",
        f"Modalidade {modalidade['nome']} excluída do sistema pelo usuário autenticado."
    )

    return resposta_sucesso(
        "Modalidade excluída com sucesso."
    )