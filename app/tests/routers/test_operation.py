import json
import pytest  # noqa pylint: disable=unused-import

from app.crud import crud_operation
from app.models.operation import Operation


def test_post_operation(test_app, monkeypatch):
    test_request_payload = {"code": "5310B9D7", "type": "x", "cost": "1"}
    test_response_payload = {"type": "x",
                             "cost": "1",
                             "code": "5310B9D7",
                             "id": 4}

    def mock_create_operation_equipment(db_session, payload):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "create_operation_equipment",
                        mock_create_operation_equipment)
    response = test_app.post("/operation/",
                             data=json.dumps(test_request_payload))

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_post_opeartion_invalid_json(test_app):
    response = test_app.post("/operation/",
                             data=json.dumps({"title": "something"}))
    assert response.status_code == 422


def test_get_operations(test_app, monkeypatch):
    test_response_payload = [{"type": "x",
                              "cost": "1",
                              "code": "5310B9D7",
                              "id": 4}]

    def mock_read_operations(db_session, skip, limit):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operations",
                        mock_read_operations)
    response = test_app.get("/operation",)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_operation(test_app, monkeypatch):
    test_response_payload = {"type": "x",
                             "cost": "1",
                             "code": "5310B9D7",
                             "id": 4}

    def mock_read_operation(db_session, id):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operation",
                        mock_read_operation)
    response = test_app.get("/operation/4",)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_operation_empty(test_app, monkeypatch):
    test_response_payload = None

    def mock_read_operation(db_session, id):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operation",
                        mock_read_operation)
    response = test_app.get("/operation/4",)

    assert response.status_code == 404


def test_get_operation_by_code(test_app, monkeypatch):
    test_response_payload = [{"type": "x",
                              "cost": "1",
                              "code": "5310B9D7",
                              "id": 4}]

    def mock_read_operations_equipment_code(db_session, code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operations_equipment_code",
                        mock_read_operations_equipment_code)
    response = test_app.get("/operation/code/5310B9D7",)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_operation_by_name(test_app, monkeypatch):
    test_response_payload = [{"type": "x",
                              "cost": "1",
                              "code": "5310B9D7",
                              "id": 4}]

    def mock_read_operations_equipment_name(db_session, name):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operations_equipment_name",
                        mock_read_operations_equipment_name)
    response = test_app.get("/operation/name/x",)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_operations_vessel(test_app, monkeypatch):
    test_response_payload = [{"type": "x",
                              "cost": "1",
                              "code": "5310B9D7",
                              "id": 4}]

    def mock_read_operations_vessel(db_session, vessel_code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operations_vessel",
                        mock_read_operations_vessel)
    response = test_app.get("/operation/vessel/name",)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_operation_cost_vessel(test_app, monkeypatch):
    test_op1 = {"type": "x",
                "cost": "1",
                "code": "5310B9D7",
                "id": 4}
    test_op2 = {"type": "x",
                "cost": "3",
                "code": "5310B9D7",
                "id": 5}
    test_response_payload = [Operation(**test_op1), Operation(**test_op2)]

    def mock_read_operations_vessel(db_session, vessel_code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operations_vessel",
                        mock_read_operations_vessel)
    response = test_app.get("/operation/cost/vessel/name",)

    assert response.status_code == 200
    assert response.json() == 2.0


def test_get_operation_cost_vessel_invalid_agg(test_app, monkeypatch):
    test_response_payload = [{"type": "x",
                              "cost": "1",
                              "code": "5310B9D7",
                              "id": 4},
                             {"type": "x",
                              "cost": "3",
                              "code": "5310B9D7",
                              "id": 5}]

    def mock_read_operations_vessel(db_session, vessel_code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_operation,
                        "read_operations_vessel",
                        mock_read_operations_vessel)
    response = test_app.get("/operation/cost/vessel/name?agg=foo",)

    assert response.status_code == 400
