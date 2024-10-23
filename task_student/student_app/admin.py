from django.contrib import admin
from .models import Student_Task,Teacher_Task

# Register your models here.
admin.site.register(Student_Task)
admin.site.register(Teacher_Task)