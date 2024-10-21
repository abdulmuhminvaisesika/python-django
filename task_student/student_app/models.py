from django.db import models
from utils.utils import calculate_total_marks, calculate_percentage

class Student_Task(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0, primary_key=True)
    chemistry = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    class_teacher = models.CharField(max_length=50)
    
    total_marks_field = models.IntegerField(default=0)  
    percentage_field = models.FloatField(default=0.0)   

    def save(self, *args, **kwargs):
        self.total_marks_field = calculate_total_marks(self.chemistry, self.physics, self.maths)
        self.percentage_field = calculate_percentage(self.total_marks_field)
        super(Student_Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
