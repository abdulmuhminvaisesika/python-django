
import random



#local imports
from student_app.models import Student_Task
from teacher_app.models import Teachers_Task
from school_app.models import School_Task

def update_students_info():
    # Fetch all students
    students = Student_Task.objects.all()
    
    updated_count = 0
    for student in students:
        if student.teacher_id:
            try:
                # Fetch teacher associated with the student
                teacher = Teachers_Task.objects.get(employee_id=student.teacher_id.employee_id)

                # Debug: print current student and teacher info
                print(f"Processing student {student.name} with teacher {teacher.name}")

                # Validate department_ID and school_ID before assignment
                if teacher.department_ID.exists() and teacher.school_ID:
                    # Assign department and school based on the teacher's department and school
                    student.department_ID.set(teacher.department_ID.all())  # Assuming this is a ManyToManyField
                    student.school_ID = teacher.school_ID
                    
                    # student.teacher_id is already a ForeignKey, so it can remain unchanged
                    
                    # Save updated student record
                    student.save()
                    updated_count += 1
                    print(f"Updated student {student.name} (Roll No: {student.roll_no})")
                else:
                    print(f"Teacher {teacher.name} lacks valid department or school info.")
            except Teachers_Task.DoesNotExist:
                print(f"Teacher with ID {student.teacher_id.employee_id} not found for student {student.name}")
            except TypeError as e:
                print(f"Type error while updating student {student.name}: {e}")
            except Exception as e:
                print(f"Unexpected error while updating student {student.name}: {e}")
    
    print(f"Total students updated: {updated_count}")



def update_students_schools():
    active_schools = School_Task.objects.filter(is_active=True)


    if not active_schools:
        print("No active schools found. Aborting update.")
        return
    
    for student in Student_Task.objects.all():

        random_school = random.choice(active_schools)
        student.school_ID = random_school
        student.save()
        print(f"Updated student {student.name} with school {random_school.school_name}")
    print('All students have been updated with random school IDs.')






def assign_departments_to_students():
    students = Student_Task.objects.all()  # Retrieve all students
    for student in students:
        school = student.school_ID  # Get the school associated with the student
        
        if school:  # Check if the school exists
            print(f"School: {school.school_ID}")  # Print the school name
            
            # Fetch departments associated with the school
            departments = school.department_ID.all()  # Assuming department_ID is a related name for departments

            if departments.exists():  # Check if there are any departments
                # Print all available departments
                for department in departments:
                    print(f"Department: {department.department_ID}")  # Ensure department_name exists in the model
                
                # Randomly select one department from the available departments
                selected_department = random.choice(departments)  # Randomly select one department
                
                # Assign the selected department to the student
                student.department_ID = selected_department  # Assign the ForeignKey
                student.save()  # Save the updated student
                
                print(f"Assigned department {selected_department.department_ID} to student {student.roll_no} in school {school.school_ID}")
            else:
                print(f"No departments found for school {school.school_name}")
        else:
            print(f"Student {student.name} has no associated school.")





def assign_teacher_to_students():
    students = Student_Task.objects.all()  # Get all students
    for student in students:
        department = student.department_ID  # Get the single department for the student
        school = student.school_ID  # Get the single school for the student
        if department and school:  # Ensure the student has a department
            # Find teachers associated with the student's department
            teachers = Teachers_Task.objects.filter(department_ID=department, school_ID=school)
            for teacher in teachers:
                print(f"Teacher: {teacher.employee_id}")  # Print the teacher's nam

            if teachers.exists():
                selected_teacher = teachers.first()  # Choose the first teacher for simplicity
                print(selected_teacher.employee_id)
                student.teacher_id = selected_teacher  # Assign the teacher to the student
                student.save()  # Save the updated student

                print(f"Assigned teacher {selected_teacher.name} to student {student.name} in department {department.department_name}")
            else:
                print(f"No teachers found for department {department.department_name}")
        else:
            print(f"Student {student.name} has no associated department")

# Run the update function
def run():
    assign_teacher_to_students()
