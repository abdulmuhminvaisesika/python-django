from django.urls import path
from .views import TeacherCrudOperations

urlpatterns = [
    path('teachers/', TeacherCrudOperations.as_view(), name='teacher-list-create'),  # For GET all and POST
    path('teachers/<int:employee_id>/', TeacherCrudOperations.as_view(), name='teacher-detail'),  # For GET, PUT, DELETE by ID
]
