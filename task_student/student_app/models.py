# Django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Local Imports
from utils.utils import calculate_percentage, calculate_performance
from teacher_app.models import Teachers_Task

class Student_Task(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.AutoField(primary_key=True)
    
    
    total_marks_field = models.IntegerField(default=0)  
    percentage_field = models.FloatField(default=0.0)   
    teacher_id = models.ForeignKey('teacher_app.Teachers_Task', on_delete=models.DO_NOTHING, null=True, blank=True)
    department_ID = models.ForeignKey('department_app.Department_Task', on_delete=models.DO_NOTHING, null=True, blank=True)
    school_ID = models.ForeignKey('school_app.School_Task', on_delete=models.DO_NOTHING, null=True, blank=True, related_name="students")

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def save(self, *args, **kwargs):
        # Calculate total marks and percentage
        self.percentage_field = calculate_percentage(self.total_marks_field)

        if self.teacher_id:
            try:
                teacher = Teachers_Task.objects.get(employee_id=self.teacher_id.employee_id)

                # Set department if not provided; retrieve the first related department if multiple
                if not self.department_ID:
                    self.department_ID = teacher.department_ID.all().first()
                
                # Set school if not provided
                if not self.school_ID:
                    self.school_ID = teacher.school_ID
            except Teachers_Task.DoesNotExist:
                raise ValueError("The specified teacher does not exist.")
            

        # Update teacher's performance if active
        if self.teacher_id and self.is_active:
            active_students = Student_Task.objects.filter(teacher_id=self.teacher_id, is_active=True)
            performance = calculate_performance(active_students)
            Teachers_Task.objects.filter(employee_id=self.teacher_id.employee_id).update(performance=performance)

        super(Student_Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# class CustomUserManager(BaseUserManager):
#     def create_user(self, roll_no, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(roll_no=roll_no, username=username, **extra_fields)
#         user.set_password(password)  # Hashes password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, roll_no, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(roll_no, username, password, **extra_fields)

# class CustomStudentUser(AbstractBaseUser):

#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=128)  # Store hashed password
#     name = models.CharField(max_length=50)
#     roll_no = models.AutoField(primary_key=True)
    
    
#     total_marks_field = models.IntegerField(default=0)  
#     percentage_field = models.FloatField(default=0.0)   
#     teacher_id = models.ForeignKey('teacher_app.Teachers_Task', on_delete=models.DO_NOTHING, null=True, blank=True)
#     department_ID = models.ForeignKey('department_app.Department_Task', on_delete=models.DO_NOTHING, null=True, blank=True)
#     school_ID = models.ForeignKey('school_app.School_Task', on_delete=models.DO_NOTHING, null=True, blank=True)

#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)

#     is_active = models.BooleanField(default=True)


    
#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['first_name']

#     def save(self, *args, **kwargs):
#         # Calculate total marks and percentage
#         self.percentage_field = calculate_percentage(self.total_marks_field)

#         if self.teacher_id:
#             try:
#                 teacher = Teachers_Task.objects.get(employee_id=self.teacher_id.employee_id)

#                 # Set department if not provided; retrieve the first related department if multiple
#                 if not self.department_ID:
#                     self.department_ID = teacher.department_ID.all().first()
                
#                 # Set school if not provided
#                 if not self.school_ID:
#                     self.school_ID = teacher.school_ID
#             except Teachers_Task.DoesNotExist:
#                 raise ValueError("The specified teacher does not exist.")
            

#         # Update teacher's performance if active
#         if self.teacher_id and self.is_active:
#             active_students = Student_Task.objects.filter(teacher_id=self.teacher_id, is_active=True)
#             performance = calculate_performance(active_students)
#             Teachers_Task.objects.filter(employee_id=self.teacher_id.employee_id).update(performance=performance)


#         # Ensure password is hashed before saving
#         if self.password and not self.password.startswith('pbkdf2_sha256$'):
#             self.set_password(self.password)
#         super(CustomStudentUser, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         """Returns True if the user has a specific permission"""
#         return True

#     def has_module_perms(self, app_label):
#         """Returns True if the user has permissions for a specific app"""
#         return True
