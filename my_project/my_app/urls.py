from django.urls import path
from .views import StudentView, StudentDetailView
 
urlpatterns=[
    path('',StudentView.as_view(),name='list_student'),
    path('student_details/<int:id>',StudentDetailView.as_view(),name='student_details'),
   
   
 
]