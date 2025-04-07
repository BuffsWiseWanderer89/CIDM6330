from datetime import datetime
from fastapi import Depends, FastAPI
from repository.db import get_session
from repository.sqlmodel_repo import SQLModelRepository
from pydantic import BaseModel
from models import User, Photo
from sqlmodel import Session

app = FastAPI()

# In-memory storage (temporary, for api tesing purposes)
users_db = []
photos_db = []

### **Create a User Model**

class UserModel(BaseModel):
    username: str
    user_id : int
    role: str
    email: str

@app.post("/users", response_model=UserModel)
def create_user(user: UserModel):
    return user

  ### **Create Photo Model**

class PhotoModel(BaseModel):
    photo_id: int
    imag_url: str
    location: str
    timestamp: datetime
    user_id: int
    user: UserModel

@app.post("/photos", response_model=PhotoModel)
def create_photo(photo: PhotoModel):
    return photo

def get_user_repo(session: Session = Depends(get_session)):
    return SQLModelRepository(User, session)

@app.get("/users")
def list_users(repo: SQLModelRepository = Depends(get_user_repo)):
    return repo.list_all()