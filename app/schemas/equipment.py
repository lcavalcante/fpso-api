from pydantic import BaseModel


class EquipmentBase(BaseModel):
    name: str
    code: str
    location: str


class EquipmentCreate(EquipmentBase):
    pass


class Equipment(EquipmentBase):
    active: bool
    vessel_code: str

    class Config:
        orm_mode = True
