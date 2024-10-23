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






