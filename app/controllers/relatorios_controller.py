import pandas as pd
from flask import send_file
from io import BytesIO

from flask import Blueprint, render_template, jsonify, request
from app.database.database import get_db
from app.utils.auth import login_required

relatorios_bp = Blueprint("relatorios", __name__)


@relatorios_bp.route("/relatorios")
@login_required
def relatorios():
    return render_template("relatorios/index.html")


@relatorios_bp.route("/api/relatorios/alunos", methods=["GET"])
@login_required
def api_relatorio_alunos():
    modalidade_id = request.args.get("modalidade_id")
    status = request.args.get("status")

    db = get_db()

    sql = """
        SELECT 
            a.id,
            a.nome,
            a.cpf,
            a.telefone,
            a.endereco,
            a.status,
            a.criado_em,
            m.nome AS modalidade_nome
        FROM alunos a
        LEFT JOIN modalidades m ON m.id = a.modalidade_id
        WHERE 1 = 1
    """

    parametros = []

    if modalidade_id:
        sql += " AND a.modalidade_id = ?"
        parametros.append(modalidade_id)

    if status:
        sql += " AND a.status = ?"
        parametros.append(status)

    sql += " ORDER BY a.nome ASC"

    alunos = db.execute(sql, parametros).fetchall()

    lista = []

    for item in alunos:
        lista.append({
            "id": item["id"],
            "nome": item["nome"],
            "cpf": item["cpf"],
            "telefone": item["telefone"],
            "endereco": item["endereco"],
            "status": item["status"],
            "modalidade": item["modalidade_nome"] or "-",
            "criado_em": item["criado_em"]
        })

    return jsonify(lista)


@relatorios_bp.route("/api/relatorios/modalidades", methods=["GET"])
@login_required
def api_relatorio_modalidades():
    db = get_db()

    modalidades = db.execute("""
        SELECT 
            m.id,
            m.nome,
            m.descricao,
            m.vagas,
            COUNT(a.id) AS total_participantes
        FROM modalidades m
        LEFT JOIN alunos a ON a.modalidade_id = m.id
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
            "percentual_ocupacao": percentual
        })

    return jsonify(lista)

@relatorios_bp.route("/api/exportar/alunos", methods=["GET"])
@login_required
def exportar_alunos_excel():
    db = get_db()

    alunos = db.execute("""
        SELECT 
            a.nome,
            a.cpf,
            a.telefone,
            a.endereco,
            a.status,
            m.nome AS modalidade
        FROM alunos a
        LEFT JOIN modalidades m ON m.id = a.modalidade_id
        ORDER BY a.nome ASC
    """).fetchall()

    lista = []

    for item in alunos:
        lista.append({
            "Nome": item["nome"],
            "CPF": item["cpf"],
            "Telefone": item["telefone"],
            "Endereço": item["endereco"],
            "Status": item["status"],
            "Modalidade": item["modalidade"] or "-"
        })

    df = pd.DataFrame(lista)

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Participantes")

    output.seek(0)

    return send_file(
        output,
        download_name="relatorio_participantes.xlsx",
        as_attachment=True
    )


@relatorios_bp.route("/api/exportar/modalidades", methods=["GET"])
@login_required
def exportar_modalidades_excel():
    db = get_db()

    modalidades = db.execute("""
        SELECT 
            m.nome,
            m.descricao,
            m.vagas,
            COUNT(a.id) AS participantes
        FROM modalidades m
        LEFT JOIN alunos a ON a.modalidade_id = m.id
        GROUP BY m.id
        ORDER BY m.nome ASC
    """).fetchall()

    lista = []

    for item in modalidades:
        lista.append({
            "Modalidade": item["nome"],
            "Descrição": item["descricao"],
            "Vagas": item["vagas"],
            "Participantes": item["participantes"]
        })

    df = pd.DataFrame(lista)

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Modalidades")

    output.seek(0)

    return send_file(
        output,
        download_name="relatorio_modalidades.xlsx",
        as_attachment=True
    )