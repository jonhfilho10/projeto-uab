import pandas as pd
from flask import send_file
from io import BytesIO

from flask import Blueprint, render_template, jsonify, request
from app.database.database import get_db
from app.utils.auth import login_required

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

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

@relatorios_bp.route("/api/exportar/alunos/pdf", methods=["GET"])
@login_required
def exportar_alunos_pdf():
    db = get_db()

    alunos = db.execute("""
        SELECT a.nome, a.cpf, a.telefone, a.status, m.nome AS modalidade
        FROM alunos a
        LEFT JOIN modalidades m ON m.id = a.modalidade_id
        ORDER BY a.nome ASC
    """).fetchall()

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph("Relatório de Participantes", styles["Title"]))
    elementos.append(Paragraph("Sistema de Gestão para Projeto Social Esportivo", styles["Normal"]))
    elementos.append(Spacer(1, 20))

    dados = [["Nome", "CPF", "Telefone", "Modalidade", "Status"]]

    for item in alunos:
        dados.append([
            item["nome"],
            item["cpf"],
            item["telefone"],
            item["modalidade"] or "-",
            item["status"]
        ])

    tabela = Table(dados, repeatRows=1)
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0056d6")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f4f7fb")]),
    ]))

    elementos.append(tabela)
    doc.build(elementos)

    buffer.seek(0)

    return send_file(
        buffer,
        download_name="relatorio_participantes.pdf",
        as_attachment=True,
        mimetype="application/pdf"
    )

@relatorios_bp.route("/api/exportar/modalidades/pdf", methods=["GET"])
@login_required
def exportar_modalidades_pdf():

    db = get_db()

    modalidades = db.execute("""
        SELECT
            m.nome,
            m.vagas,

            COUNT(a.id) AS total_participantes,

            (m.vagas - COUNT(a.id)) AS vagas_disponiveis,

            CASE
                WHEN m.vagas > 0
                THEN ROUND((COUNT(a.id) * 100.0) / m.vagas, 2)
                ELSE 0
            END AS percentual_ocupacao

        FROM modalidades m

        LEFT JOIN alunos a
            ON a.modalidade_id = m.id

        GROUP BY m.id

        ORDER BY m.nome ASC
    """).fetchall()

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elementos = []

    elementos.append(
        Paragraph(
            "Relatório de Modalidades",
            styles["Title"]
        )
    )

    elementos.append(
        Paragraph(
            "Sistema de Gestão para Projeto Social Esportivo",
            styles["Normal"]
        )
    )

    elementos.append(Spacer(1, 20))

    dados = [[
        "Modalidade",
        "Vagas",
        "Participantes",
        "Disponíveis",
        "Ocupação"
    ]]

    for item in modalidades:

        dados.append([

            item["nome"],
            str(item["vagas"]),
            str(item["total_participantes"]),
            str(item["vagas_disponiveis"]),
            f'{item["percentual_ocupacao"]}%'

        ])

    tabela = Table(
        dados,
        repeatRows=1
    )

    tabela.setStyle(TableStyle([

        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor("#0056d6")
        ),

        (
            "TEXTCOLOR",
            (0, 0),
            (-1, 0),
            colors.white
        ),

        (
            "GRID",
            (0, 0),
            (-1, -1),
            0.5,
            colors.HexColor("#dddddd")
        ),

        (
            "FONTNAME",
            (0, 0),
            (-1, 0),
            "Helvetica-Bold"
        ),

        (
            "FONTSIZE",
            (0, 0),
            (-1, -1),
            8
        ),

        (
            "ROWBACKGROUNDS",
            (0, 1),
            (-1, -1),
            [
                colors.white,
                colors.HexColor("#f4f7fb")
            ]
        ),

    ]))

    elementos.append(tabela)

    doc.build(elementos)

    buffer.seek(0)

    return send_file(
        buffer,
        download_name="relatorio_modalidades.pdf",
        as_attachment=True,
        mimetype="application/pdf"
    )