from django.db import models

class Department_Task(models.Model):
    department_ID = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    department_HOD = models.OneToOneField('teacher_app.Teachers_Task', on_delete=models.SET_NULL, null=True, blank=True ,related_name='departments')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.department_name