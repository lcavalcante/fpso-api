from pydantic import BaseModel

from app.schemas.equipment import Equipment


class VesselBase(BaseModel):
    code: str


class VesselCreate(VesselBase):
    pass

class Vessel(VesselBase):
    equipments: list[Equipment] = []

    class Config:
        orm_mode = True
