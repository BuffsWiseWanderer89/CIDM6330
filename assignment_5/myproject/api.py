from datetime import date

from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from ninja import Schema, Field
from ninja import UploadedFile, File

from job.models import User

from job.tasks import send_welcome_email, generate_user_report


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

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@api.post("/users")
def create_user(request, user: UserModelIn, profilepic: UploadedFile = File(...)):
    worker_info = user.dict()
    worker = User(**worker_info)
    user_instance = User.objects.create(**worker_info)
    user_instance.profilepic.save(profilepic.name, profilepic)
    return user_instance

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


# Extend API Beyond CRUD to perform a few operations design
# to be performed on the user model
@api.post("/users/send-welcome/{user_id}")
def trigger_welcome_email(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    send_welcome_email.delay(user.email)
    return {"message": f"Welcome email sent to {user.email} (queued)"}

@api.post("/users/generate-report")
def trigger_user_report(request):
    task = generate_user_report.delay()
    return {"message": "User report generation started.", "task_id": task.id}

