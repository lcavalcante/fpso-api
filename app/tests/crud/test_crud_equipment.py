import pytest  # noqa pylint: disable=unused-import


from app.crud import crud_equipment, crud_vessel
from app.schemas.equipment import EquipmentCreate
from app.schemas.vessel import VesselCreate


def test_create_equipment(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))

    eq = crud_equipment.create_equipment_vessel(test_db,
                                                EquipmentCreate(**input_eq),
                                                "string")
    assert eq.code == input_eq["code"]
    assert eq.name == input_eq["name"]
    assert eq.location == input_eq["location"]
    assert eq.vessel_code == input_vessel["code"]


def test_read_equipment(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))

    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")

    eq = crud_equipment.read_equipment(test_db, "eqcode")
    assert eq is not None
    assert eq.active
    assert eq.vessel_code == input_vessel["code"]


def test_read_equipment_not_found(test_db):
    input_vessel = {"code": "string"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))

    eq = crud_equipment.read_equipment(test_db, "eqcode")
    assert eq is None


def test_read_equipments(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))

    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")

    eq = crud_equipment.read_equipments(test_db)
    assert len(eq) == 1


def test_read_equipments_empty(test_db):
    eq = crud_equipment.read_equipments(test_db)
    assert eq == []


def test_read_equipments_vessel(test_db):
    input_vessel = {"code": "string"}
    input_vessel2 = {"code": "string2"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel2))

    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")

    eq = crud_equipment.read_equipments_vessel(test_db, "string")
    assert len(eq) == 1
    assert eq[0].vessel_code == input_vessel["code"]


def test_read_equipments_vessel_empty(test_db):
    eq = crud_equipment.read_equipments_vessel(test_db, "code")
    assert eq == []


def test_read_active_equipments_vessel(test_db):
    input_vessel = {"code": "string"}
    input_vessel2 = {"code": "string2"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_eq2 = {"name": "compressor",
                         "code": "eqcode2",
                         "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel2))

    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq2),
                                           "string")
    crud_equipment.update_equipment_inactive(test_db, input_eq2["code"])
    eq = crud_equipment.read_active_equipments_vessel(test_db, "string")
    assert len(eq) == 1
    assert eq[0].code == input_eq["code"]


def test_update_equipment_inactive(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))

    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    crud_equipment.update_equipment_inactive(test_db, input_eq["code"])
    eq = crud_equipment.read_equipment(test_db, input_eq["code"])
    assert eq is not None
    assert not eq.active


def test_update_equipments_inactive(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_eq2 = {"name": "compressor",
                         "code": "eqcode2",
                         "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))

    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq2),
                                           "string")
    equipments = ["eqcode", "eqcode2"]
    crud_equipment.update_equipments_inactive(test_db, equipments)
    eq = crud_equipment.read_active_equipments_vessel(test_db, "string")
    assert eq == []
