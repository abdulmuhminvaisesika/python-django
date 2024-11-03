from django.urls import path
from .views import SchoolCrudOperations, SchoolUnderTask, SchoolStatusView

urlpatterns = [
    path('', SchoolCrudOperations.as_view(), name='school-list-create'),  # For GET all schools and POST new school
    path('<int:school_ID>/', SchoolCrudOperations.as_view(), name='school-detail'),  # For GET, PUT, DELETE specific school
    path('teacher/<int:school_ID>/', SchoolUnderTask.as_view(), name='school-teacher'),
    path('student/<int:school_ID>/', SchoolUnderTask.as_view(), name='school-student'),


    path('<str:status>/', SchoolStatusView.as_view(), name='school-status'),

    

]
