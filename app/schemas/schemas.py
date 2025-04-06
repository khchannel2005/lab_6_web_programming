from pydantic import BaseModel
from typing import List, Optional

class HotelBase(BaseModel):
    name: str
    address: str
    city: str
    country: str
    phone: Optional[str] = None
    email: Optional[str] = None


class HotelCreate(HotelBase):
    pass


class Hotel(HotelBase):
    id: int

    class Config:
        orm_mode = True


class RoomBase(BaseModel):
    room_type: str
    price: float


class RoomCreate(RoomBase):
    hotel_id: int


class Room(RoomBase):
    id: int
    hotel_id: int

    class Config:
        orm_mode = True