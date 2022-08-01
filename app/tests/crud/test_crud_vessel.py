import pytest  # noqa pylint: disable=unused-import


from app.crud import crud_vessel
from app.schemas.vessel import VesselCreate


def test_create_vessel(test_db):
    input_vessel = {"code": "string"}
    vessel = crud_vessel.create_vessel(test_db,
                                       VesselCreate(**input_vessel))
    assert vessel.code == input_vessel["code"]


def test_read_vessel(test_db):
    input_vessel = {"code": "string"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    vessel = crud_vessel.read_vessel(test_db, "string")

    assert vessel is not None


def test_read_vessel_not_found(test_db):
    vessel = crud_vessel.read_vessel(test_db, "string")

    assert vessel is None


def test_read_vessels(test_db):
    input_vessel = {"code": "string"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    vessel = crud_vessel.read_vessels(test_db)

    assert len(vessel) == 1


def test_read_vessels_empty(test_db):
    vessel = crud_vessel.read_vessels(test_db)

    assert vessel == []
