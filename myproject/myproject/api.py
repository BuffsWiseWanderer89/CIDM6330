from datetime import datetime
from typing import Optional

from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from ninja import Schema
from ninja import UploadedFile, File

from job.models import Employee


class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: Optional[int] = None
    birthdate: Optional[datetime] = None

class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: Optional[int] = None
    birthdate: Optional[datetime] = None

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

@api.post("/employees", response=EmployeeOut)
def create_employee(request, employee: EmployeeIn, cv: UploadedFile = File(...)):
    worker = Employee.objects.create(**employee.dict())
    worker.cv.save(cv.name, cv)
    return worker

@api.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

@api.get("/employees", response=list[EmployeeOut])
def list_employees(request):
    employees = Employee.objects.all()
    return employees

@api.put("/employees/{employee_id}")
def update_employee(request, employee_id: int, payload: EmployeeIn):
    employee = get_object_or_404(Employee, id=employee_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value) #for each attribute in the employee instance, set the value to the value from the employee object
    employee.save()
    return {"success": True}

@api.delete("/employees/{employee_id}")
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True, "employee": employee}