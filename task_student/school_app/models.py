from django.db import models

# Create your models here.


class School_Task(models.Model):
    school_name = models.CharField(max_length=50)
    school_ID = models.AutoField(primary_key=True)
    school_location = models.CharField(max_length=50)
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school_name