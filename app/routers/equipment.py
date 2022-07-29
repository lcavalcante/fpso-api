from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import deps
from app.crud import crud_equipment
from app.schemas.equipment import Equipment

router = APIRouter(
    prefix="/equipment",
    tags=["equipment"])


@router.get("/", response_model=list[Equipment])
def get_equipments(db: Session = Depends(deps.get_db),
                   skip: int = 0,
                   limit: int = 100,):
    equipments = crud_equipment.read_equipments(db, skip=skip, limit=limit)
    return equipments


@router.get("/{equipment_code}", response_model=Equipment)
def get_equipment(equipment_code: str, db: Session = Depends(deps.get_db)):
    equipment = crud_equipment.read_equipment(db, code=equipment_code)
    return equipment
