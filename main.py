from fastapi import FastAPI, Depends, HTTPException
from models import User
from repository.base import Repository
from repository.in_memory import InMemoryRepository
from repository.csv_repo import CSVRepository
from repository.sqlmodel_repo import SQLModelRepository
from repository.db import get_session
from sqlmodel import Session
import os

app = FastAPI()

def get_repository(session: Session = Depends(get_session)) -> Repository:
    repo_type = os.getenv("REPO_TYPE", "in_memory")
    if repo_type == "csv":
        return CSVRepository(filename="users.csv", model=User)
    elif repo_type == "sqlmodel":
        return SQLModelRepository(model=User, session=session)
    return InMemoryRepository()

@app.post("/users/", response_model=User)
def create_user(user: User, repo: Repository = Depends(get_repository)):
    return repo.create(user)

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, repo: Repository = Depends(get_repository)):
    user = repo.read(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User, repo: Repository = Depends(get_repository)):
    updated_user = repo.update(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, repo: Repository = Depends(get_repository)):
    repo.delete(user_id)
    return {"message": "User deleted"}

@app.get("/users/", response_model=list[User])
def list_users(repo: Repository = Depends(get_repository)):
    return repo.list_all()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI User API!"}