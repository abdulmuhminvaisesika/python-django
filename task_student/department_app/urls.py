from django.urls import path
from .views import DepartmentCrudOperations

urlpatterns = [
    path('', DepartmentCrudOperations.as_view(), name='department-list-create'),  # For GET all departments and POST new department
    path('<int:department_ID>/', DepartmentCrudOperations.as_view(), name='department-detail'),  # For GET, PUT, DELETE specific department
]
