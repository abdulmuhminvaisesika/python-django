from django.urls import path
from .views import SchoolCrudOperations

urlpatterns = [
    path('', SchoolCrudOperations.as_view(), name='school-list-create'),  # For GET all schools and POST new school
    path('<int:school_ID>/', SchoolCrudOperations.as_view(), name='school-detail'),  # For GET, PUT, DELETE specific school
]
