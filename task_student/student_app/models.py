from django.db import models
from utils.utils import calculate_total_marks, calculate_percentage, calculate_performance
from teacher_app.models import Teachers_Task
class Student_Task(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.AutoField(primary_key=True)
    chemistry = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    
    total_marks_field = models.IntegerField(default=0)  
    percentage_field = models.FloatField(default=0.0)   
    teacher_id = models.ForeignKey('teacher_app.Teachers_Task', on_delete=models.DO_NOTHING, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def save(self, *args, **kwargs):
        # Calculate total marks and percentage
        self.total_marks_field = calculate_total_marks(self.chemistry, self.physics, self.maths)
        self.percentage_field = calculate_percentage(self.total_marks_field)

        # Calculate performance for associated teacher if teacher_id exists
        if self.teacher_id: 
            students = Student_Task.objects.filter(teacher_id=self.teacher_id_id)
            performance = calculate_performance(students)
            Teachers_Task.objects.filter(employee_id=self.teacher_id_id).update(performance=performance)

        super(Student_Task, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
