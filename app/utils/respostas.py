from flask import jsonify


def resposta_sucesso(mensagem="", dados=None, status=200):

    return jsonify({
        "success": True,
        "mensagem": mensagem,
        "dados": dados
    }), status


def resposta_erro(mensagem="Erro interno do sistema.", status=400):

    return jsonify({
        "success": False,
        "mensagem": mensagem
    }), status
