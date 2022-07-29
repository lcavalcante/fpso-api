from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.crud import crud_vessel
from app import deps

router = APIRouter(
    prefix="/vessel",
    tags=["vessel"])

@router.get("/")
def read_vessels(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,):
    vessels = crud_vessel.get_vessels(db, skip=skip, limit=limit)
    return vessels


@router.get("/{vessel_id}")
def read_vessel():
    return {"code": "MV102"}
