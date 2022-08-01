import json
import pytest  # pylint: disable=unused-import


from app.crud import crud_equipment


def test_get_equipment(test_app, test_db, monkeypatch):
    test_response_payload = {"name": "compressor",
                             "code": "5310B9D7",
                             "vessel_code": "MV102",
                             "active": True,
                             "location": "Brazil"}
    vessel_request_payload = {"code": "MV102"}
    test_app.post("/vessel/", data=json.dumps(vessel_request_payload))

    def mock_read(db_session, code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_equipment, "read_equipment", mock_read)

    response = test_app.get("/equipment/5310B9D7")
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_equipments(test_app, test_db, monkeypatch):
    test_response_payload = [{"name": "compressor",
                              "code": "5310B9D7",
                              "vessel_code": "MV102",
                              "active": True,
                              "location": "Brazil"}]
    vessel_request_payload = {"code": "MV102"}
    test_app.post("/vessel/", data=json.dumps(vessel_request_payload))

    def mock_read(db_session, skip, limit):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_equipment, "read_equipments", mock_read)

    response = test_app.get("/equipment/")
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_equipment_not_found(test_app, monkeypatch):

    def mock_get(db_session, code):  # noqa
        return None

    monkeypatch.setattr(crud_equipment, "read_equipment", mock_get)

    response = test_app.get("/equipment/FOO")
    assert response.status_code == 404
