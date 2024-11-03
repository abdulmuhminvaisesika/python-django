from django.db import models
from django.apps import apps





class School_Task(models.Model):
    school_ID = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=50)
    school_location = models.CharField(max_length=50)
    department_ID = models.ManyToManyField('department_app.Department_Task', blank=True)

    is_active = models.BooleanField(default=True) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)






    def save(self, *args, **kwargs):
        # Track if the `is_active` field changes
        if self.pk is not None:  # Only check if the instance already exists
            old_instance = School_Task.objects.get(pk=self.pk)
            if old_instance.is_active != self.is_active:
                # Lazy-load related models to avoid circular import issues
                Teachers_Task = apps.get_model('teacher_app', 'Teachers_Task')
                Student_Task = apps.get_model('student_app', 'Student_Task')

                # Update the `is_active` status of teachers in this school
                Teachers_Task.objects.filter(school_ID=self).update(is_active=self.is_active)

                # Update the `is_active` status of students associated with teachers in this school
                Student_Task.objects.filter(teacher_id__school_ID=self).update(is_active=self.is_active)

        # Call the parent class's save method to save the instance
        super(School_Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.school_name
