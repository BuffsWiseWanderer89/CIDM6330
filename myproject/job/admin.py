from django.db import models
from django.contrib import admin
from .models import Department, Employee

from job.models import Employee, Department

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'birthdate', 'cv')
    list_filter = ('department',)
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')
