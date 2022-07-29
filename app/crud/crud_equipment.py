from sqlalchemy.orm import Session

from app.models.equipment import Equipment
from app.schemas.equipment import EquipmentCreate


def read_equipment(db: Session, code: str):
    return db.query(Equipment).filter(Equipment.code == code).first()


def read_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Equipment).offset(skip).limit(limit).all()


def create_vessel_equipment(db: Session, equipment: EquipmentCreate, vessel_code: str):
    db_equipment = Equipment(**equipment.dict(), vessel_code=vessel_code)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment
