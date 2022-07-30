from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz():
    """
    tests if health_check is working
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
