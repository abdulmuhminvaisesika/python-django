


from school_app.models import School_Task
from department_app.models import Department_Task
from teacher_app.models import Teachers_Task
from utils.utils import calculate_performance  
from student_app.models import Student_Task


def add_schools():
    school_names = [
        'Greenwood High School',
        'Riverdale Academy',
        'Sunnydale School',
        'Lakeside International School',
        'Maple Leaf School'
    ]

    school_locations = [
        'New York', 
        'Los Angeles', 
        'Chicago', 
        'pakisthan', 
        'india'
    ]

    for i in range(5):
        school = School_Task(
            school_name=school_names[i],  # Use names from the list
            school_ID=1000 + i,  # Assign a unique school ID starting from 100
            school_location=school_locations[i]  # Assign the location from the list
        )
        school.save()  # Save the school instance to the database
        print(f'Added {school}')


def add_departments():
    # Predefined department names and HOD names
    department_names = ['BBA', 'MBA HR', 'MCA', 'BTech', 'MTech']
    hod_names = ['Frank White', 'Grace Hall', 'Henry Adams', 'Ivy Taylor', 'Jack Lee']
    
    # Fetch existing schools
    schools = School_Task.objects.filter(school_ID__gte=1000)[:10]
    
    for i in range(10):  # Loop to create 10 departments
        if i < len(schools):  # Ensure there's a school to link to
            school = schools[i]
            department = Department_Task(
                department_name=department_names[i],
                department_HOD=hod_names[i],
                school_ID=school  # Link to the school
            )
            department.save()  # Save the department instance to the database
            print(f'Added {department}')  # Print confirmation

def view_all_departments():
    teachers = Teachers_Task.objects.all() 
    for teacher in teachers:
        print(teacher.name, teacher.employee_id, teacher.school_ID,teacher.performance, teacher.department_ID)

def assign_students_to_teachers():
    # Get all students and teachers
    students = list(Student_Task.objects.all())
    teachers = list(Teachers_Task.objects.all())

    num_students = len(students)
    num_teachers = len(teachers)
    
    # Check to make sure there are students and teachers
    if num_students == 0 or num_teachers == 0:
        print("No students or teachers available.")
        return

    # Distribute students to teachers
    teacher_index = 0
    for i, student in enumerate(students):
        student.teacher_id = teachers[teacher_index]  # Assign the teacher
        student.save()

        # Update teacher_index to cycle through teachers
        teacher_index = (teacher_index + 1) % num_teachers

    print(f"Assigned {num_students} students to {num_teachers} teachers.")


def assign_teachers_to_hod():
    try:
        # Get all departments
        departments = Department_Task.objects.all()

        # Loop through each department
        for department in departments:
            # Get the teacher with the matching department_ID
            try:
                teacher_hod = Teachers_Task.objects.filter(department_ID=department.department_ID).first()
                
                if teacher_hod:
                    # Assign the teacher as the HOD
                    department.teacher_HOD = teacher_hod
                    department.save()  # Save the updated department
                    print(f"Assigned {teacher_hod.name} as the HOD of {department.department_name}.")
                else:
                    print(f"No teacher found for department {department.department_name}.")
                    
            except Teachers_Task.DoesNotExist:
                print(f"No teacher found for department {department.department_name} (ID: {department.department_ID}).")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def update_department_HOD():
    # Get all teachers
    teachers = Teachers_Task.objects.all()

    # Create a mapping of teacher names to their instances
    teacher_map = {teacher.name: teacher for teacher in teachers}

    # Fetch all departments
    departments = Department_Task.objects.all()

    # Update department_HOD for each department based on the teacher's name
    for department in departments:
        # If a matching teacher name exists, set the department_HOD
        if department.department_HOD in teacher_map:
            department.department_HOD = teacher_map[department.department_HOD]
            department.save()

    print("Updated department_HOD fields with corresponding teachers.")


def run():
    update_department_HOD()
       

