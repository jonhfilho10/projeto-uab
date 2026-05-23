from flask import Flask, render_template, jsonify
import time

from app.database.database import init_db, close_db, get_db
from app.controllers.auth_controller import auth_bp
from app.controllers.modalidades_controller import modalidades_bp
from app.controllers.alunos_controller import alunos_bp
from app.utils.auth import login_required
from app.controllers.usuarios_controller import usuarios_bp
from app.controllers.relatorios_controller import relatorios_bp


def create_app():
    app = Flask(__name__)

    app.secret_key = "chave_secreta_projeto_social"

    app.teardown_appcontext(close_db)

    with app.app_context():
        init_db()

    @app.route("/")
    @login_required
    def dashboard():
        return render_template("dashboard.html")

    @app.route("/api/dashboard")
    @login_required
    def api_dashboard():
        time.sleep(1)

        db = get_db()

        alunos_ativos = db.execute("""
            SELECT COUNT(*) AS total
            FROM alunos
            WHERE status = 'ativo'
        """).fetchone()["total"]

        alunos_inativos = db.execute("""
            SELECT COUNT(*) AS total
            FROM alunos
            WHERE status = 'inativo'
        """).fetchone()["total"]

        modalidades = db.execute("""
            SELECT COUNT(*) AS total
            FROM modalidades
        """).fetchone()["total"]

        total_alunos = db.execute("""
            SELECT COUNT(*) AS total
            FROM alunos
        """).fetchone()["total"]

        ocupacao_modalidades = db.execute("""
            SELECT 
                m.nome,
                m.vagas,
                COUNT(a.id) AS total_participantes
            FROM modalidades m
            LEFT JOIN alunos a ON a.modalidade_id = m.id
            GROUP BY m.id
            ORDER BY m.nome ASC
        """).fetchall()

        lista_ocupacao = []

        for item in ocupacao_modalidades:
            vagas = item["vagas"] or 0
            total = item["total_participantes"] or 0

            percentual = 0
            if vagas > 0:
                percentual = round((total / vagas) * 100, 2)

            lista_ocupacao.append({
                "modalidade": item["nome"],
                "vagas": vagas,
                "participantes": total,
                "percentual": percentual
            })

        dados = {
            "alunos_ativos": alunos_ativos,
            "alunos_inativos": alunos_inativos,
            "modalidades": modalidades,
            "total_alunos": total_alunos,
            "ocupacao_modalidades": lista_ocupacao
        }

        return jsonify(dados)

    app.register_blueprint(auth_bp)
    app.register_blueprint(modalidades_bp)
    app.register_blueprint(alunos_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(relatorios_bp)
    return app