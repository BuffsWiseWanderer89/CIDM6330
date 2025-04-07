from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

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
