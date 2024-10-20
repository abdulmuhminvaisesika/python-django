from django.urls import path
from .views import StudentAdd,StudentTopper,StudentAvg


urlpatterns = [
    path('add/', StudentAdd.as_view(), name='student_add'),
    path('list/', StudentAdd.as_view(), name='student_list'),
    path('update/<int:roll_no>/', StudentAdd.as_view(), name='student_update'),
    path('delete/<int:roll_no>/', StudentAdd.as_view(), name='student_delete'),
    path('cutoff/', StudentTopper.as_view(), name='cutoff'), 
    path('toppers/', StudentTopper.as_view(), name='toppers'),
    path('failed/', StudentTopper.as_view(), name="failed"),
    path('avg/', StudentAvg.as_view(), name="avg"),
    path('subject_failed/', StudentAvg.as_view(), name="subject_failed"),
    path('teacher/', StudentAvg.as_view(), name="teacher"),
    path('perfomance/', StudentAvg.as_view(), name="perfomancer"),
]