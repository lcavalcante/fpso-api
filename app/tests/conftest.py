from _pytest.fixtures import pytest_fixture_setup
import pytest
from starlette.testclient import TestClient
from app.db.session import Base, SessionLocal, engine

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    Base.metadata.drop_all(bind=engine)
