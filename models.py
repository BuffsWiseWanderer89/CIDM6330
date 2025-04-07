from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    role: str
    email: str

class Photo(SQLModel, table=True):
    photo_id: Optional[int] = Field(default=None, primary_key=True)
    image_url: str
    location: str
    timestamp: datetime
    user_id: int = Field(foreign_key="user.user_id")
    