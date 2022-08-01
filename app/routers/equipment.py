from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import deps
from app.crud import crud_equipment
from app.schemas.equipment import Equipment
from app.schemas.message import Message

router = APIRouter(
    prefix="/equipment",
    tags=["equipment"])


@router.get("/", response_model=list[Equipment])
def get_equipments(db: Session = Depends(deps.get_db),
                   skip: int = 0,
                   limit: int = 100,):
    equipments = crud_equipment.read_equipments(db, skip=skip, limit=limit)
    return equipments


@router.get("/{equipment_code}",
            responses={404: {"model": Message}},
            response_model=Equipment)
def get_equipment(equipment_code: str, db: Session = Depends(deps.get_db)):
    equipment = crud_equipment.read_equipment(db, code=equipment_code)
    if equipment is None:
        return JSONResponse(status_code=404,
                            content={"error": "Equipment not found"})
    return equipment


@router.put("/inactivate", response_model=list[Equipment] | Equipment)
def put_equipment_inactivate(codes: str | list[str],
                             db: Session = Depends(deps.get_db)):
    if type(codes) == list:
        equipments = crud_equipment.update_equipments_inactive(db, codes)
    else:
        equipments = crud_equipment.update_equipment_inactive(db, codes)

    return equipments
