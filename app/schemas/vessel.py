from pydantic import BaseModel


class VesselBase(BaseModel):
    title: str
    description: str | None = None


class VesselCreate(VesselBase):
    pass


class Vessel(VesselBase):
    code: str

    class Config:
        orm_mode = True
