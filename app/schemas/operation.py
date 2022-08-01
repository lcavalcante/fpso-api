from pydantic import BaseModel


class OperationBase(BaseModel):
    type: str
    cost: str
    code: str


class OperationCreate(OperationBase):
    pass


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True
