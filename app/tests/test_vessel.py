import json
import pytest  # pylint: disable=unused-import

from app.crud import crud_vessel


def test_post_vessel(test_app, test_db, monkeypatch):
    test_request_payload = {"code": "MV102"}
    test_response_payload = {"code": "MV102", "equipments": []}

    def mock_post(db_session, payload):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_vessel, "create_vessel", mock_post)
    response = test_app.post("/vessel/", data=json.dumps(test_request_payload))

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_post_duplicated_vessel(test_app, test_db):
    test_request_payload = {"code": "MV102"}

    test_app.post("/vessel/", data=json.dumps(test_request_payload))
    response = test_app.post("/vessel/", data=json.dumps(test_request_payload))

    assert response.status_code == 400


def test_post_vessel_invalid_json(test_app):
    response = test_app.post("/vessel/",
                             data=json.dumps({"title": "something"}))
    assert response.status_code == 422


def test_get_vessel(test_app, test_db, monkeypatch):
    test_response_payload = {"code": "MV102", "equipments": []}

    def mock_get(db_session, code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_vessel, "read_vessel", mock_get)

    response = test_app.get("/vessel/MV102")
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_vessels(test_app, test_db, monkeypatch):
    test_response_payload = [{"code": "MV102", "equipments": []}]

    def mock_get(db_session, skip, limit):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_vessel, "read_vessels", mock_get)

    response = test_app.get("/vessel/")
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_vessel_not_found(test_app, test_db, monkeypatch):

    def mock_get(db_session, code):  # noqa
        return None

    monkeypatch.setattr(crud_vessel, "read_vessel", mock_get)

    response = test_app.get("/vessel/FOO")
    assert response.status_code == 404
