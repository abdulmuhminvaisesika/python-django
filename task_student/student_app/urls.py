from django.urls import path
from .views import Crud_All_Student,StudentTaskByRollno, StudentTopper ,StudentAvg


urlpatterns = [
    
    path('cutoff/', StudentTopper.as_view(), name='cutoff'), 
    path('toppers/', StudentTopper.as_view(), name='toppers'),
    path('failed/', StudentTopper.as_view(), name="failed"),
    path('avg/', StudentAvg.as_view(), name="avg"),
    path('subject_failed/', StudentAvg.as_view(), name="subject_failed"),
    path('teacher/', StudentAvg.as_view(), name="teacher"),
    path('perfomance/', StudentAvg.as_view(), name="perfomancer"),


    path('crud/<int:roll_no>/', StudentTaskByRollno.as_view(), name='student_task'),
    path('crud/', Crud_All_Student.as_view(),name="crud_on_all_student")
]