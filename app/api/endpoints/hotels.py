from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Hotel

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/hotels", response_model=list[dict])
def read_hotels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    hotels = db.query(Hotel).offset(skip).limit(limit).all()
    return [{"id": h.id, "name": h.name, "address": h.address, "city": h.city, "country": h.country} for h in hotels]


@router.post("/hotels", response_model=dict)
def create_hotel(hotel: dict, db: Session = Depends(get_db)):
    db_hotel = Hotel(**hotel)
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return {"id": db_hotel.id, "name": db_hotel.name}