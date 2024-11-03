from django.urls import path
from .views import DepartmentCrudOperations, DepartmentUnderTask, DepartmentStatusView, DepartmentsBySchoolView

urlpatterns = [
    path('', DepartmentCrudOperations.as_view(), name='department-list-create'),  # For GET all departments and POST new department
    path('<int:department_ID>/', DepartmentCrudOperations.as_view(), name='department-detail'),  # For GET, PUT, DELETE specific department
    path('teacher/<int:department_ID>/', DepartmentUnderTask.as_view(), name='department-teacher'),
    path('student/<int:department_ID>/', DepartmentUnderTask.as_view(), name='department-student'),
    path('<str:status>/', DepartmentStatusView.as_view(), name='department-status'),
    path('departments-by-school/<int:school_id>/', DepartmentsBySchoolView.as_view(), name='departments-by-school'),

]
