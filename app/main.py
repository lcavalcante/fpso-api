from fastapi import FastAPI

from .routers import vessel, equipment

from .db.session import engine, Base

app = FastAPI()


app.include_router(vessel.router)
app.include_router(equipment.router)


@app.get("/")
async def root():
    """docstring for root"""
    return {"status": "ok"}
