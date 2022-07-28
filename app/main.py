from fastapi import FastAPI

app = FastAPI()


@app.get("/v1/vessel")
def get_vessels():
    return {"code": "MV102"}
 

@app.get("/v1/vessel/{vessel_id}")
def get_vessels_id():
    return {"code": "MV102"}


@app.get("/v1/equipment")
def get_equipments():
    return  {"name": "compressor",
             "code": "5310B9D7",
             "location": "Brazil"} 


@app.get("/v1/equipment/{equipment_id}")
def get_equipment_id():
    return  {"name": "compressor",
             "code": "5310B9D7",
             "location": "Brazil"} 
