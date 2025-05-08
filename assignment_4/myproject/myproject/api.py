from datetime import date

from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from ninja import Schema, Field
from ninja import UploadedFile, File

from job.models import User

# this is an input schema for the user model

class UserModelIn(Schema):
    username: str = Field(..., max_length=100)
    user_id: int = Field(..., gt=0)
    role: str = Field(..., max_length=50)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    profilepic: UploadedFile = File(...)

class UserModelOut(Schema):
    username: str = Field(..., max_length=100)
    user_id: int = Field(..., gt=0)
    role: str = Field(..., max_length=50)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    profilepic: str = Field(...)

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@api.get("/add)")
def add(request, a: int, b: int):
    return {"result": a + b}


@api.post("/users")
def create_user(request, user: UserModelIn, profilepic: UploadedFile = File(...)):
    worker_info = user.dict()
    worker = User(**worker_info)
    user = user.objects.create(worker)
    user.profilepic.save(profilepic.name, profilepic)

    return user

@api.get("/users/{user_id}", response=UserModelOut)
def get_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    return user

@api.get("/users", response=list[UserModelOut])
def list_users(request):
    users = User.objects.all()
    return users

@api.put("/users/{user_id}")
def update_user(request, user_id: int, payload: UserModelIn):
    user = get_object_or_404(User, id=user_id)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return {"success": True, "user": user}

@api.delete("/users/{user_id}")
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True}