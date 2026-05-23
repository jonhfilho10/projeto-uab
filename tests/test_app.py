import pytest

from app import create_app


@pytest.fixture
def app():
    app = create_app()

    app.config.update({
        "TESTING": True
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_dashboard_redireciona_sem_login(client):
    response = client.get("/")

    assert response.status_code == 302


def test_api_dashboard_sem_login(client):
    response = client.get("/api/dashboard")

    assert response.status_code == 302


def test_login_page(client):
    response = client.get("/login")

    assert response.status_code == 200


def test_modalidades_sem_login(client):
    response = client.get("/modalidades")

    assert response.status_code == 302


def test_usuarios_sem_login(client):
    response = client.get("/usuarios")

    assert response.status_code == 302


def test_relatorios_sem_login(client):
    response = client.get("/relatorios")

    assert response.status_code == 302


def test_api_modalidades_sem_login(client):
    response = client.get("/api/modalidades")

    assert response.status_code == 302


def test_api_alunos_sem_login(client):
    response = client.get("/api/alunos")

    assert response.status_code == 302