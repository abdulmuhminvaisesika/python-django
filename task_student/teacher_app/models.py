#django imports
from django.db import models
from django.apps import apps  




class Teachers_Task(models.Model):
    employee_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)
    performance = models.FloatField(default=0.0)
    department_ID = models.ManyToManyField('department_app.Department_Task', blank=True, related_name='teachers')

    school_ID = models.ForeignKey('school_app.School_Task', on_delete=models.DO_NOTHING, null=True, blank=True, related_name="teachers")

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        # Check if `is_active` status has changed
        if self.pk is not None:  # Ensures this is an update and not a new creation
            old_instance = Teachers_Task.objects.get(pk=self.pk)
            if old_instance.is_active != self.is_active:
                # Lazy-load the Student_Task model to avoid circular import issues
                Student_Task = apps.get_model('student_app', 'Student_Task')

                # Update `is_active` status for students related to this teacher
                Student_Task.objects.filter(teacher_id=self).update(is_active=self.is_active)

        # Save the teacher instance
        super().save(*args, **kwargs)



    
    def __str__(self):
        return self.name
