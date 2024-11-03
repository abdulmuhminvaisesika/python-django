#Django Imports
from django.urls import path

#Local Imports
from .views import Crud_All_Student, StudentTopper, StudentAvg, StudentStatusView

urlpatterns = [
    path('cutoff/', StudentTopper.as_view(), name='cutoff'), 
    path('toppers/', StudentTopper.as_view(), name='toppers'),
    path('failed/', StudentTopper.as_view(), name="failed"),
    path('<int:roll_no>/', Crud_All_Student.as_view(), name='student_task'),
    path('', Crud_All_Student.as_view(), name="crud_on_all_student"),
    path('avg/', StudentAvg.as_view(), name='student_less_greater_avg'),
    path('teacher/<int:teacher_id>/', StudentAvg.as_view(), name='students_by_teacher'),
    path('performance/<int:teacher_id>/', StudentAvg.as_view(), name='performance_of_teacher'),
    path('performance/', StudentAvg.as_view(), name='performance_of_all_teachers'),
    path('<str:status>/', StudentStatusView.as_view(), name='school-status'),

]
