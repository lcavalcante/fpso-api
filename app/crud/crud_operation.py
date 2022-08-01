from sqlalchemy.orm import Session

from app.models.operation import Operation
from app.models.equipment import Equipment
from app.schemas.operation import OperationCreate


def read_operation(db: Session, id: int):
    return db.query(Operation).filter(Operation.id == id).first()


def read_operations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Operation).offset(skip).limit(limit).all()


def read_operations_equipment_code(db: Session, code: str):
    return db.query(Operation).filter(Operation.code == code).all()


def read_operations_equipment_name(db: Session, name: str):
    return (db.query(Operation)
              .join(Equipment)
              .filter(Equipment.name == name)
              .all())


def read_operations_vessel(db: Session, vessel_code: str):
    return (db.query(Operation)
              .join(Equipment)
              .filter(Equipment.vessel_code == vessel_code)
              .all())


def create_operation_equipment(db: Session,
                               operation: OperationCreate,):
    db_operation = Operation(**operation.dict())
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return db_operation
