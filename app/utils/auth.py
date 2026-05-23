from functools import wraps
from flask import session, redirect, url_for, jsonify, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("auth.login"))

        if session.get("usuario_perfil") != "administrador":
            if request.path.startswith("/api/"):
                return jsonify({
                    "success": False,
                    "mensagem": "Acesso permitido somente para administradores."
                }), 403

            return redirect(url_for("dashboard", erro="sem_permissao"))

        return f(*args, **kwargs)

    return decorated_function