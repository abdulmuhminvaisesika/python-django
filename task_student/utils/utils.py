# utils/utils.py


from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict


def calculate_total_marks(chemistry, physics, maths):
    """Calculate the total marks for a student."""
    return chemistry + physics + maths

def calculate_percentage(total_marks):
    """Calculate the percentage based on total marks."""
    return (total_marks / 300) * 100


def format_students_data(students, title="students"):
    """Format student data based on the provided queryset."""
    report = []
    
    for student in students:
        report.append({
            'name': student.name,
            'roll_no': student.roll_no,
            'chemistry': student.chemistry,
            'physics': student.physics,
            'maths': student.maths,
            'total_marks': student.total_marks_field,
            'percentage': student.percentage_field,
            'class_teacher': student.class_teacher
        })
    
    return Response({
        title: report
    })

#to calculate average mark of student
def calculate_average(students):
    total_students = len(students)
    if total_students == 0:
        return 0
    total_marks_sum = sum(student.total_marks_field for student in students)
    return total_marks_sum / total_students

def group_students_by_teacher(students):
    grouped_students = defaultdict(list)
    for student in students:
        grouped_students[student.class_teacher].append(student)
    return grouped_students

def filter_failed_students(students, subject=None, pass_mark=35):
    if subject:
        return [student for student in students if getattr(student, subject) < pass_mark]
    return [student for student in students if student.chemistry < pass_mark or student.physics < pass_mark or student.maths < pass_mark]
