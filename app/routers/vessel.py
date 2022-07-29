from fastapi import APIRouter

router = APIRouter(
    prefix="/vessel",
    tags=["vessel"])


@router.get("/")
def read_vessels():
    return {"code": "MV102"}


@router.get("/{vessel_id}")
def read_vessel():
    return {"code": "MV102"}
