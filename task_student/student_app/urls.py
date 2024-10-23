from django.urls import path
from .views import Crud_All_Student,StudentTaskByRollno, StudentTopper ,StudentAvg


urlpatterns = [
    
    path('cutoff/', StudentTopper.as_view(), name='cutoff'), 
    path('toppers/', StudentTopper.as_view(), name='toppers'),
    path('failed/', StudentTopper.as_view(), name="failed"),
    path('avg/', StudentAvg.as_view(), name="avg"),

    path('teacher/<int:teacher_id>/', StudentAvg.as_view(), name='students_by_teacher'),

    path('perfomance/<int:teacher_id>/', StudentAvg.as_view(), name="perfomance"),

    #used for perform crud operation based on roll number
    path('crud/<int:roll_no>/', StudentTaskByRollno.as_view(), name='student_task'),
    
    #this path used for post and get,delete all the students
    path('crud/', Crud_All_Student.as_view(),name="crud_on_all_student")
]