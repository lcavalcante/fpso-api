from fastapi import FastAPI

from app.routers import vessel, equipment

app = FastAPI()


app.include_router(vessel.router)
app.include_router(equipment.router)


@app.get("/")
async def healthz():
    """docstring for root"""
    return {"status": "ok"}
