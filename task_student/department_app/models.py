from django.db import models

class Department_Task(models.Model):
    department_ID = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    department_HOD = models.ForeignKey('teacher_app.Teachers_Task', on_delete=models.DO_NOTHING, null=True, blank=True)
    school_ID = models.ForeignKey('school_app.School_Task', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name