from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz(test_app):
    """
    tests if health_check is working
    """
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
