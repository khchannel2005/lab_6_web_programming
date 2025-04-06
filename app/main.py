from fastapi import FastAPI
from app.api.endpoints import hotels

app = FastAPI()

app.include_router(hotels.router, prefix="/api", tags=["hotels"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hotel API!"}