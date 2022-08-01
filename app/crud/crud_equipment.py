from sqlalchemy.orm import Session

from app.models.equipment import Equipment
from app.schemas.equipment import EquipmentCreate


def read_equipment(db: Session, code: str):
    return db.query(Equipment).filter(Equipment.code == code).first()


def read_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Equipment).offset(skip).limit(limit).all()


def read_equipments_vessel(db: Session, vessel_code: str,):
    db_equipments = (db
                     .query(Equipment)
                     .filter(Equipment.vessel_code == vessel_code)
                     .all())
    return db_equipments


def read_active_equipments_vessel(db: Session, vessel_code: str,):
    db_equipments = (db
                     .query(Equipment)
                     .filter(Equipment.vessel_code == vessel_code)
                     .all())
    return list(filter(lambda eq: eq.active, db_equipments))


def create_equipment_vessel(db: Session,
                            equipment: EquipmentCreate,
                            vessel_code: str):
    db_equipment = Equipment(**equipment.dict(), vessel_code=vessel_code)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


def update_equipment_inactive(db: Session, code: str):
    db_equipment = db.query(Equipment).filter(Equipment.code == code).first()
    if db_equipment:
        db_equipment.active = False
        db.commit()
        db.refresh(db_equipment)
    return db_equipment


def update_equipments_inactive(db: Session, codes: list[str]):
    db_equipments = db.query(Equipment).filter(Equipment.code.in_(codes)).all()
    for equipment in db_equipments:
        equipment.active = False
    db.commit()
    return db_equipments
