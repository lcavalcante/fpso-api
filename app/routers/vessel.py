from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import deps
from app.crud import crud_equipment, crud_vessel
from app.schemas.equipment import EquipmentCreate
from app.schemas.vessel import Vessel, VesselCreate

router = APIRouter(
    prefix="/vessel",
    tags=["vessel"])

@router.get("/", response_model=list[Vessel])
def get_vessels(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,):
    vessels = crud_vessel.read_vessels(db, skip=skip, limit=limit)
    return vessels


@router.post("/", response_model=Vessel)
def post_vessel(vessel: VesselCreate, db: Session = Depends(deps.get_db),):
    db_vessel = crud_vessel.read_vessel(db, code=vessel.code)
    if db_vessel:
        raise HTTPException(status_code=400, detail="Vessel already registered")
    return crud_vessel.create_vessel(db, vessel)


@router.get("/{vessel_code}", response_model=Vessel)
def get_vessel(vessel_code: str, db: Session = Depends(deps.get_db),):
    vessel = crud_vessel.read_vessel(db, code=vessel_code)
    return vessel


@router.post("/{vessel_code}/equipment")
def post_vesssel_equipment(
        vessel_code: str,
        equipment: EquipmentCreate,
        db: Session = Depends(deps.get_db)):
    db_equipment = crud_equipment.read_equipment(db, equipment.code)
    if db_equipment:
        raise HTTPException(status_code=400, detail="Equipment already registered")
    return crud_equipment.create_vessel_equipment(db, equipment, vessel_code=vessel_code)
