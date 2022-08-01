import json
import pytest  # noqa pylint: disable=unused-import


from app.crud import crud_equipment


def test_get_equipment(test_app, monkeypatch):
    test_response_payload = {"name": "compressor",
                             "code": "5310B9D7",
                             "vessel_code": "MV102",
                             "active": True,
                             "location": "Brazil"}

    def mock_read_equipment(db_session, code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_equipment, "read_equipment", mock_read_equipment)

    response = test_app.get("/equipment/5310B9D7")
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_equipments(test_app, monkeypatch):
    test_response_payload = [{"name": "compressor",
                              "code": "5310B9D7",
                              "vessel_code": "MV102",
                              "active": True,
                              "location": "Brazil"}]

    def mock_read_equipments(db_session, skip, limit):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_equipment,
                        "read_equipments",
                        mock_read_equipments)

    response = test_app.get("/equipment/")
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_equipment_not_found(test_app, monkeypatch):

    def mock_read_equipment(db_session, code):  # noqa
        return None

    monkeypatch.setattr(crud_equipment,
                        "read_equipment",
                        mock_read_equipment)

    response = test_app.get("/equipment/FOO")
    assert response.status_code == 404


def test_put_equipment_inactivate_string(test_app, monkeypatch):
    test_request_payload = "5310B9D7"
    test_response_payload = {"name": "compressor",
                             "code": "5310B9D7",
                             "active": False,
                             "vessel_code": "MV102",
                             "location": "Brazil"}

    def mock_update_equipment_inactive(db_session, code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_equipment,
                        "update_equipment_inactive",
                        mock_update_equipment_inactive)

    response = test_app.put("/equipment/inactivate",
                            data=json.dumps(test_request_payload))
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_put_equipment_inactivate_list(test_app, monkeypatch):
    test_request_payload = ["5310B9D7", "5310B9D8"]
    eq1 = {"name": "compressor",
           "code": "5310B9D7",
           "active": False,
           "vessel_code": "MV102",
           "location": "Brazil"}
    eq2 = {"name": "compressor",
           "code": "5310B9D8",
           "active": False,
           "vessel_code": "MV102",
           "location": "Brazil"}
    test_response_payload = [eq1, eq2]

    def mock_update_equipments_inactive(db_session, code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_equipment,
                        "update_equipments_inactive",
                        mock_update_equipments_inactive)

    response = test_app.put("/equipment/inactivate",
                            data=json.dumps(test_request_payload))
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_put_equipment_inactivate_string_idempotency(test_app, monkeypatch):
    test_request_payload = "5310B9D7"
    test_response_payload = {"name": "compressor",
                             "code": "5310B9D7",
                             "active": False,
                             "vessel_code": "MV102",
                             "location": "Brazil"}

    def mock_update_equipment_inactive(db_session, code):  # noqa
        return test_response_payload

    monkeypatch.setattr(crud_equipment,
                        "update_equipment_inactive",
                        mock_update_equipment_inactive)

    response = test_app.put("/equipment/inactivate",
                            data=json.dumps(test_request_payload))
    assert response.status_code == 200
    assert response.json() == test_response_payload
