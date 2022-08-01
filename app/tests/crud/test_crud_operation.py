from crud import crud_operation
import pytest
from schemas.operation import OperationCreate  # noqa pylint: disable=unused-import


from app.crud import crud_equipment, crud_vessel
from app.schemas.equipment import EquipmentCreate
from app.schemas.vessel import VesselCreate


def test_create_operation(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_op = {"code": "eqcode",
                "type": "replacement",
                "cost": "10000"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op = crud_operation.create_operation_equipment(test_db,
                                                   OperationCreate(**input_op))

    assert op.code == input_op["code"]


def test_read_operation(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_op = {"code": "eqcode",
                "type": "replacement",
                "cost": "10000"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_create = (crud_operation.
                 create_operation_equipment(test_db,
                                            OperationCreate(**input_op)))
    op_read = crud_operation.read_operation(test_db, op_create.id)

    assert op_create == op_read


def test_read_operations(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_op = {"code": "eqcode",
                "type": "replacement",
                "cost": "10000"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_create = (crud_operation.
                 create_operation_equipment(test_db,
                                            OperationCreate(**input_op)))
    op_read = crud_operation.read_operations(test_db,)

    assert op_create in op_read


def test_read_operations_equipment_code(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_op = {"code": "eqcode",
                "type": "replacement",
                "cost": "10000"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_create = (crud_operation.
                 create_operation_equipment(test_db,
                                            OperationCreate(**input_op)))
    op_read = crud_operation.read_operations_equipment_code(test_db, "eqcode")

    assert op_create in op_read


def test_read_operations_equipment_name(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "eqname",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_op = {"code": "eqcode",
                "type": "replacement",
                "cost": "10000"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_create = (crud_operation.
                 create_operation_equipment(test_db,
                                            OperationCreate(**input_op)))
    op_read = crud_operation.read_operations_equipment_name(test_db, "eqname")

    assert op_create in op_read


def test_read_operations_vessel(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "eqname",
                        "code": "eqcode",
                        "location": "Brazil"}
    input_op = {"code": "eqcode",
                "type": "replacement",
                "cost": "10000"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_create = (crud_operation.
                 create_operation_equipment(test_db,
                                            OperationCreate(**input_op)))
    op_read = crud_operation.read_operations_vessel(test_db, "string")

    assert op_create in op_read


def test_read_operations_vessel_empty(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "eqname",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_read = crud_operation.read_operations_vessel(test_db, "fail")

    assert op_read == []


def test_read_operations_equipment_code_empty(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "compressor",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_read = crud_operation.read_operations_equipment_code(test_db, "fail")

    assert op_read == []


def test_read_operations_equipment_name_empty(test_db):
    input_vessel = {"code": "string"}
    input_eq = {"name": "eqname",
                        "code": "eqcode",
                        "location": "Brazil"}
    crud_vessel.create_vessel(test_db,
                              VesselCreate(**input_vessel))
    crud_equipment.create_equipment_vessel(test_db,
                                           EquipmentCreate(**input_eq),
                                           "string")
    op_read = crud_operation.read_operations_equipment_name(test_db, "fail")

    assert op_read == []
