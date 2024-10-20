from django.db import models

# Create your models here.


class Student_Task(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField(default=0, primary_key=True)
    chemistry=models.IntegerField(default=0)
    physics=models.IntegerField(default=0)
    maths=models.IntegerField(default=0)
    
    class_teacher=models.CharField(max_length=50)

    def total_marks(self):
        return self.chemistry+self.physics+self.maths
    def percentage(self):
        return (self.total_marks()/300)*100
    

    def __str__(self):
        return self.name


