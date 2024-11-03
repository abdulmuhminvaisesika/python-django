#Django Imports
from django.urls import path

#local Imports
from .views import TeacherCrudOperations, TeacherUnderTask, TeacherStatusView

urlpatterns = [
    path('', TeacherCrudOperations.as_view(), name='teacher-list-create'),  # For GET all and POST
    path('<int:employee_id>/', TeacherCrudOperations.as_view(), name='teacher-detail'),  # For GET, PUT, DELETE by ID
    path('students/<int:employee_id>/',TeacherUnderTask.as_view(), name='teacher-student'),
    path('performance/<int:employee_id>/', TeacherUnderTask.as_view(), name='teacher-performance'),
    path('performance/', TeacherUnderTask.as_view(), name='teacher-performance-all'),
    path('best_perfomer/', TeacherUnderTask.as_view(), name='teacher-best-performer'),
    path('<str:status>/', TeacherStatusView.as_view(), name='school-status'),

]
