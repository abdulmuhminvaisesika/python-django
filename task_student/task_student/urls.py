from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('student_app.urls')),
    path('teachers/', include('teacher_app.urls')),
    path('departments/', include('department_app.urls')),
    path('schools/', include('school_app.urls')),
]
