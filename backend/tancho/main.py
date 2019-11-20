from fastapi import FastAPI
from pets.routes import pets_router
from config import config

DB_CLIENT = DB = None
app = FastAPI()


app.include_router(
    pets_router,
    prefix="/pets",
    tags=["pets"],
    responses={404: {"description": "Not found"}},
)


@app.on_event("startup")
async def app_startup():
    pass


@app.on_event("shutdown")
async def app_shutdown():
    config.close_db_client(DB_CLIENT)
