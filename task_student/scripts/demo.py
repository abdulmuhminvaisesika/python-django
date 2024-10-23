
from student_app.models import Student_Task, Teacher_Task
from utils.utils import calculate_average



def update_teacher_performance():
    # Define the maximum possible score per student
    max_score = 300  # 100 for chemistry, 100 for physics, and 100 for maths

    teachers = Teacher_Task.objects.all()
    for teacher in teachers:
        # Get students taught by the teacher
        students = Student_Task.objects.filter(teacher_id=teacher)
        # Calculate average performance
        average_performance = calculate_average(students)
        
        # If there are no students, set performance to 0
        if average_performance == 0:
            performance_percentage = 0
        else:
            # Convert average performance to percentage
            performance_percentage = (average_performance / max_score) * 100
        
        # Update teacher's performance field
        teacher.perfomance = performance_percentage
        teacher.save()
        
        print(f"Teacher {teacher.name}'s performance updated to {performance_percentage:.2f}%")

def run():
    update_teacher_performance()
