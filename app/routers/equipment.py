from fastapi import APIRouter

router = APIRouter()


@router.get("/equipment")
def read_equipments():
    return  {"name": "compressor",
             "code": "5310B9D7",
             "location": "Brazil"} 


@router.get("/equipment/{equipment_id}")
def read_equipment():
    return  {"name": "compressor",
             "code": "5310B9D7",
             "location": "Brazil"} 
