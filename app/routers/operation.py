from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import deps
from app.crud import crud_operation
from app.schemas.message import Message
from app.schemas.operation import Operation, OperationCreate

router = APIRouter(
    prefix="/operation",
    tags=["operation"])


@router.get("/", response_model=list[Operation])
def get_operations(db: Session = Depends(deps.get_db),
                   skip: int = 0,
                   limit: int = 100,):
    equipments = crud_operation.read_operations(db, skip=skip, limit=limit)
    return equipments


@router.get("/{operation_id}",
            responses={404: {"model": Message}},
            response_model=Operation)
def get_operation(operation_id: int, db: Session = Depends(deps.get_db)):
    operation = crud_operation.read_operation(db, id=operation_id)
    if operation is None:
        return JSONResponse(status_code=404,
                            content={"error": "Operation not found"})
    return operation


@router.get("/code/{equipment_code}",
            response_model=list[Operation])
def get_operation_by_code(equipment_code: str,
                          db: Session = Depends(deps.get_db)):
    operations = (crud_operation
                  .read_operations_equipment_code(db, code=equipment_code))
    return operations


@router.get("/name/{equipment_name}",
            response_model=list[Operation])
def get_operation_by_name(equipment_name: str,
                          db: Session = Depends(deps.get_db)):
    operations = (crud_operation
                  .read_operations_equipment_name(db, name=equipment_name))
    return operations


@router.get("/vessel/{vessel_code}",
            response_model=list)
def get_operations_vessel(vessel_code: str,
                          db: Session = Depends(deps.get_db)):
    operations = (crud_operation
                  .read_operations_vessel(db, vessel_code=vessel_code))
    return operations


@router.get("/cost/vessel/{vessel_code}",
            responses={400: {"model": Message}},
            response_model=float)
def get_operation_cost_vessel(vessel_code: str,
                              agg: str = "avg",
                              db: Session = Depends(deps.get_db)):
    operations = (crud_operation
                  .read_operations_vessel(db, vessel_code=vessel_code))
    cost = 0.0
    if agg == "avg":
        for op in operations:
            cost += int(op.cost)
        return cost / len(operations)
    else:
        return JSONResponse(status_code=400,
                            content={"error": "unsuported cost aggregator"})


@router.post("/",
             response_model=Operation,
             status_code=201)
def post_operation(operation: OperationCreate,
                   db: Session = Depends(deps.get_db),):
    return crud_operation.create_operation_equipment(db, operation)
