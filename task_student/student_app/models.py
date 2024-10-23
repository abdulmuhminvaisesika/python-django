from django.db import models
from utils.utils import calculate_total_marks, calculate_percentage , calculate_performance
class Student_Task(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=1, primary_key=True)
    chemistry = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    
    total_marks_field = models.IntegerField(default=0)  
    percentage_field = models.FloatField(default=0.0)   
    teacher_id = models.ForeignKey('Teacher_Task', on_delete=models.DO_NOTHING, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_marks_field = calculate_total_marks(self.chemistry, self.physics, self.maths)
        self.percentage_field = calculate_percentage(self.total_marks_field)
        super(Student_Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



#teacher model
class Teacher_Task(models.Model):
    name = models.CharField(max_length=50)
    employee_id = models.IntegerField(default=0, primary_key=True)
    perfomance = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        students=Student_Task.objects.filter(teacher_id=self.employee_id)  
        self.perfomance=calculate_performance(students)

        super(Teacher_Task, self).save(*args, **kwargs)
    def __str__(self):
        return self.name