# Project Documentation: Task Student API
## Project Name: Task Student
### Structure:

* Main Modules:
1. `student_app` - Manages student-related data and CRUD operations.

2. `teacher_app` - Manages teacher-related data and performance tracking.

3. `department_app` - Manages department data, including departmental hierarchy.

4. `school_app` - Manages school-related information, such as school entities.

   
> Each module contains specific API views for CRUD operations and retrieval functions to perform various tasks.



## Project Documentation: task_student
### Project Overview

The task_student project is designed to manage and automate student, teacher, department, and school-related data. It utilizes Django REST Framework for building APIs that perform CRUD operations on various models across different apps. The project structure ensures modularity and organized URL routing for each app.

## Project Setup

### 1. Create the Django Project
To start, create the Django project named task_student. Run:

```bash
django-admin startproject task_student
cd task_student
```
### 2. Install Dependencies
Ensure that you have Django, Django REST Framework, and any other necessary packages installed:

```bash
pip install django djangorestframework django-extensions
```
### 3. Create and Register Applications
Inside the task_student project folder, create the following applications:

```bash
python manage.py startapp student_app
python manage.py startapp teacher_app
python manage.py startapp department_app
python manage.py startapp school_app
```
### 4. Configure settings.py

In task_student/settings.py, register all the necessary applications, including Django’s built-in apps, REST framework, and the custom apps:


```bash
INSTALLED_APPS = [
    
    'rest_framework',
    'django_extensions',
    'student_app',
    'teacher_app',
    'department_app',
    'school_app'
]
```
## URL Configuration
### 5. Main Project urls.py Setup
Define the main URL patterns in task_student/urls.py, including each app’s URL configuration to organize API endpoints by app:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('student_app.urls')),
    path('teachers/', include('teacher_app.urls')),
    path('departments/', include('department_app.urls')),
    path('schools/', include('school_app.urls')),
]
```
> **6. Individual App** URLsEnsure each app (e.g., student_app, teacher_app, etc.) has its own urls.py file where you define specific URL routes for API endpoints related to each app’s functionality.




### Project Structure Overview

```
task_student
│   db.sqlite3
│   manage.py
│
├───department_app
│   │   admin.py, apps.py, models.py, serializers.py, tests.py, urls.py, views.py, __init__.py
│   └───migrations
│
├───school_app
│   │   admin.py, apps.py, models.py, serializers.py, tests.py, urls.py, views.py, __init__.py
│   └───migrations
│
├───scripts
│   │   demo.py
│
├───student_app
│   │   admin.py, apps.py, models.py, serializers.py, tests.py, urls.py, views.py, __init__.py
│   └───migrations
│
├───task_student
│   │   settings.py, urls.py, asgi.py, wsgi.py, __init__.py
│
└───teacher_app
    │   admin.py, apps.py, models.py, serializers.py, tests.py, urls.py, views.py, __init__.py
    └───migrations
```


# Student Module
 
### Key Features and API Endpoints
The main model in student_app is the Student_Task model, which includes the following fields:


The Student_Task model defines the fields and foreign key relationships. Here is a summary of the fields:


* Basic Fields:

    * name: The student’s name
    * roll_no: Primary key, auto-incrementing integer
    * chemistry, physics, maths: Subject scores, defaulted to 0

* Calculated Fields:

    * total_marks_field: Total marks of the student, calculated using a utility function
    * percentage_field: Percentage of total marks, calculated using a utility function
* Relationships:

    * teacher_id: Foreign key reference to the Teachers_Task model in teacher_app
* Date Fields:

    * created_on, updated_on: Track when each record was created and last updated
* `Save Logic`: On save, total marks and percentage are recalculated, and if teacher_id is set, the associated teacher’s performance is updated based on their students’ performance.
---
### Serializer (serializers.py)
Defines the serializer for Student_Task model, which specifies fields for API responses and incoming requests:

```python
from rest_framework import serializers
from .models import Student_Task

class StudentTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Task
        fields = ['name', 'roll_no', 'chemistry', 'physics', 'maths', 'total_marks_field', 'percentage_field', 'teacher_id', 'created_on', 'updated_on']
```
---
### Admin Registration
The Student_Task model is registered in Django's admin interface, allowing administrators to manage student records through the Django admin panel. This registration enables administrators to easily add, update, and delete student records within a user-friendly interface.


To register the model, the following code is included in admin.py:

```python
from django.contrib import admin
from .models import Student_Task

# Register your models here.
admin.site.register(Student_Task)
```

---
### Students API Endpoints


The student_app exposes the following API endpoints, each serving a specific function for managing or analyzing student data.

**Student Management Endpoints**
* POST `/students/` - Add New Student
    * Allows adding a new student to the database with details such as name, roll number, and marks.
* GET `/students/` - Get All Students
    * Retrieves a list of all students in the database.
* PUT `/students/<roll_no>/` - Update Student
    * Updates the details of a student by ID.
* DELETE `/students/<roll_no>/` - Delete Student
    * Deletes a specific student by ID.
  
**Performance and Analysis Endpoints**
* GET `/students/toppers/` - List First 5 Toppers
    * Retrieves the top 5 students based on total marks.
* GET `/students/cutoff/` - Students Above Cutoff
    * Lists students who scored above a specific cutoff mark(150).
* GET `/students/failed/` - List Failed Students
    * Lists students who failed (below passing threshold-35).
* GET `/students/avg/` - Students Below & Above Average
    * Categorizes students as below or above the average marks.
* GET  `/students/teacher/<teacher_id>/` - List Students by Class Teacher
    * Lists all students associated with a specific class teacher.

**Teacher Performance-Related Endpoints**
* GET `/students/performance/` - Get Performance of All Teachers
    * Calculates and returns performance data for all teachers based on student results.
* GET `/students/performance/<teacher_id>/` - Get Performance of Specific Teacher
    * Retrieves performance metrics for a specific teacher by teacher_id.
  


## Views Structure
The following view classes and methods are responsible for handling requests to the above endpoints:

### Class: Crud_All_Student
This class handles basic CRUD operations for Student_Task records.

Methods:
* get(self, request, roll_no=None): Retrieves all students or a specific student by roll_no.
* post(self, request): Creates new student records and updates associated teacher performance.
* put(self, request, roll_no): Updates an existing student record by roll_no.
* delete(self, request, roll_no=None): Deletes a specific student by roll_no or deletes all students.


### Class: StudentTopper
Methods:
* get(): Directs to specific methods based on URL paths.
* get_top5_students(): Retrieves top 5 students.
* students_with_cutoff(): Filters students above a cutoff score.
* failed_student(): Lists students failing below the threshold.
### Class: StudentAvg
Methods:
* get(): Directs to specific methods based on URL paths or teacher_id.
* student_less_greater_avg(): Divides students into below or above average groups.
* students_by_teacher(): Retrieves students associated with a specific teacher.
* performance_of_teacher(): Fetches performance metrics for a specific teacher, or for all teachers if no teacher_id is given.


## URL pattern
```python
from django.urls import path
from .views import Crud_All_Student, StudentTopper, StudentAvg

urlpatterns = [
    path('cutoff/', StudentTopper.as_view(), name='cutoff'), 
    path('toppers/', StudentTopper.as_view(), name='toppers'),
    path('failed/', StudentTopper.as_view(), name="failed"),
    path('<int:roll_no>/', Crud_All_Student.as_view(), name='student_task'),
    path('', Crud_All_Student.as_view(), name="crud_on_all_student"),
    path('avg/', StudentAvg.as_view(), name='student_less_greater_avg'),
    path('teacher/<int:teacher_id>/', StudentAvg.as_view(), name='students_by_teacher'),
    path('performance/<int:teacher_id>/', StudentAvg.as_view(), name='performance_of_teacher'),
    path('performance/', StudentAvg.as_view(), name='performance_of_all_teachers'),  
]
```
## utils/utils.py

```python
# utils/utils.py





def calculate_total_marks(chemistry, physics, maths):
    """Calculate the total marks for a student."""
    return chemistry + physics + maths

def calculate_percentage(total_marks):
    """Calculate the percentage based on total marks."""
    return (total_marks / 300) * 100




def calculate_average(students):
    """
    Calculate the average total marks for all students.
    """
    total_students = len(students)
    if total_students == 0:
        return 0
    total_marks_sum = sum(student.total_marks_field for student in students)
    return total_marks_sum / total_students


def calculate_performance(students):
    """
    Calculate the performance based on the average total marks of all students
    assigned to a specific teacher.
    """
    average_marks = calculate_average(students)

    if average_marks == 0:
        return 0  # No students or all students have 0 marks

    percentage_performance = (average_marks / 300) * 100
    return percentage_performance
```
### Explanation of Functions

1. calculate_total_marks(chemistry, physics, maths):

   * Takes individual subject marks as arguments and returns the total marks for a student.
2. calculate_percentage(total_marks):

   * Takes the total marks as an argument and calculates the percentage based on a total of 300 marks.
3. calculate_average(students):

    * Takes a list of student objects and calculates the average total marks. If there are no students, it returns 0.
4. calculate_performance(students):

   * Takes a list of student objects assigned to a specific teacher and calculates the performance percentage based on the average marks of those students.

> **Utility functions from utils/utils.py** are imported into the Student_Task model to calculate total marks, percentage, and teacher performance. During the save process, total marks and percentage are computed using calculate_total_marks and calculate_percentage. If a teacher is associated with the student, calculate_performance updates the teacher's performance based on their students' average marks. This approach ensures efficient calculations and data consistency.

## Teacher App 
### Fields:


* `employee_id`: Auto-incremented primary key.
* `name`: Name of the teacher.
* `performance`: A float representing the teacher's performance score.
* `department_ID`: Foreign key linking to the Department_Task model.
* `school_ID`: Foreign key linking to the School_Task model.
* `created_on`: Timestamp for when the record is created.
* `updated_on`: Timestamp for the last update to the record.
### Serializer: TeacherTaskSerializer
``` python
from rest_framework import serializers
from .models import Teachers_Task 
from school_app.models import School_Task
from department_app.models import Department_Task

class TeacherTaskSerializer(serializers.ModelSerializer):
    school_ID = serializers.PrimaryKeyRelatedField(queryset=School_Task.objects.all())
    department_ID = serializers.PrimaryKeyRelatedField(queryset=Department_Task.objects.all())

    class Meta:
        model = Teachers_Task
        fields = ['name', 'employee_id', 'performance', 'school_ID', 'department_ID', 'created_on', 'updated_on']
```
**Purpose:**
* Serializes the Teachers_Task model data for API responses and input validation.
### Admin Registration
``` python
from django.contrib import admin
from teacher_app.models import Teachers_Task

admin.site.register(Teachers_Task)
```

**Purpose:**

Registers the Teachers_Task model with the Django admin site for easy management.
### URLs
```python
from django.urls import path
from .views import TeacherCrudOperations

urlpatterns = [
    path('teachers/', TeacherCrudOperations.as_view(), name='teacher-list-create'),  # For GET all and POST
    path('teachers/<int:employee_id>/', TeacherCrudOperations.as_view(), name='teacher-detail'),  # For GET, PUT, DELETE by ID
]
```
**Routes:**
* `teachers/`: List all teachers or create a new teacher (GET/POST).
* `teachers/<int:employee_id>/`: Retrieve, update, or delete a specific teacher by their ID (GET/PUT/DELETE).
###  Views: TeacherCrudOperations

**Methods:**

* GET: Retrieve a specific teacher by ID or all teachers.
* POST: Create new teacher records and calculate their performance based on associated students.
* PUT: Update an existing teacher's information.
* DELETE: Remove a specific teacher or all teachers from the database.


## Department App 


**Fields:**
* department_ID: Auto-incremented primary key.
* department_name: Name of the department.
* department_HOD: Foreign key linking to the Teachers_Task model (Head of Department).
* school_ID: Foreign key linking to the School_Task model.
* created_on: Timestamp for when the record is created.
* updated_on: Timestamp for the last update to the record



### Serializer: DepartmentTaskSerializer

```python
from department_app.models import Department_Task
from rest_framework import serializers
from school_app.models import School_Task

class DepartmentTaskSerializer(serializers.ModelSerializer):
    school_ID = serializers.PrimaryKeyRelatedField(queryset=School_Task.objects.all())
    department_HOD = serializers.PrimaryKeyRelatedField(queryset=Department_Task.objects.all())

    class Meta:
        model = Department_Task
        fields = ['department_ID', 'department_name', 'department_HOD', 'school_ID', 'created_on', 'updated_on']
```
**Purpose:**
Serializes the Department_Task model data for API responses and input validation.

### Admin Registration
```python
from django.contrib import admin
from .models import Department_Task

admin.site.register(Department_Task)
```
**Purpose:**

Registers the Department_Task model with the Django admin site for easy management.

### URLs

```python
from django.urls import path
from .views import DepartmentCrudOperations

urlpatterns = [
    path('', DepartmentCrudOperations.as_view(), name='department-list-create'),  # For GET all departments and POST new department
    path('<int:department_ID>/', DepartmentCrudOperations.as_view(), name='department-detail'),  # For GET, PUT, DELETE specific department
]
```
**Routes:**
* `'departments'`: List all departments or create a new department (GET/POST).
* `departments/<int:department_ID>/`': Retrieve, update, or delete a specific department by its ID (GET/PUT/DELETE).


### Views: DepartmentCrudOperations
Methods:

* GET: Retrieve a specific department by ID or all departments.
* POST: Create new department records.
* PUT: Update an existing department's information.
* DELETE: Remove a specific department from the database.



## School App 


### Fields:

* school_name: Name of the school.
school_ID: Auto-incremented primary key.
* school_location: Location of the school.
* created_on: Timestamp for when the record is created.
* updated_on: Timestamp for the last update to the record.
### Serializer: SchoolTaskSerializer

```python
from rest_framework import serializers
from school_app.models import School_Task

class SchoolTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Task
        fields = ['school_name', 'school_ID', 'school_location', 'created_on', 'updated_on']
```
**Purpose:**

Serializes the School_Task model data for API responses and input validation.

### Admin Registration

```python
from django.contrib import admin
from .models import School_Task

admin.site.register(School_Task)
```
**Purpose:**

Registers the School_Task model with the Django admin site for easy management.

### URLs
```python
from django.urls import path
from .views import SchoolCrudOperations

urlpatterns = [
    path('', SchoolCrudOperations.as_view(), name='school-list-create'),  # For GET all schools and POST new school
    path('<int:school_ID>/', SchoolCrudOperations.as_view(), name='school-detail'),  # For GET, PUT, DELETE specific school
]
```
**Routes:**

* `schools/`: List all schools or create a new school (GET/POST).
* `schools/<int:school_ID>/`: Retrieve, update, or delete a specific school by its ID (GET/PUT/DELETE)

### Views: SchoolCrudOperations
Methods:

* GET: Retrieve a specific school by ID or all schools.
* POST: Create a new school record.
* PUT: Update an existing school's information.
* DELETE: Remove a specific school from the database.
