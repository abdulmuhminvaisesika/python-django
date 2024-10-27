from django.db import models

class Teachers_Task(models.Model):
    employee_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)
    performance = models.FloatField(default=0.0)
    
    department_ID = models.ForeignKey('department_app.Department_Task', on_delete=models.DO_NOTHING, null=True, blank=True)
    school_ID = models.ForeignKey('school_app.School_Task', on_delete=models.DO_NOTHING, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    
    def __str__(self):
        return self.name
