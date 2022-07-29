from sqlalchemy.orm import Session

from app.models.vessel import Vessel
from app.schemas.vessel import VesselCreate


def get_vessel(db: Session, code: str):
    return db.query(Vessel).filter(Vessel.code == code).first()


def get_vessels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vessel).offset(skip).limit(limit).all()


def create_vessel(db: Session, vessel: VesselCreate):
    db_vessel = Vessel(**vessel.dict())
    db.add(db_vessel)
    db.commit()
    db.refresh(db_vessel)
    return db_vessel
