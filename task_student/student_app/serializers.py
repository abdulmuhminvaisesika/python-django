from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Student_Task
from teacher_app.models import Teachers_Task

class StudentTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Task
        fields = [
            'roll_no', 'name', 
            'total_marks_field', 'percentage_field', 'teacher_id', 
            'department_ID', 'school_ID', 'is_active', 
            'created_on', 'updated_on'
        ]

    def validate_teacher_id(self, value):
        # Extract relevant IDs from data
        teacher_id = self.initial_data.get('teacher_id')
        school_id = self.initial_data.get('school_ID')

        # If a teacher is provided, check department and school consistency
        if teacher_id:
            teacher = get_object_or_404(Teachers_Task, employee_id=teacher_id)


            if school_id and teacher.school_ID.school_ID != school_id:
                raise serializers.ValidationError(
                    f"Teacher {teacher.employee_id} does not belong to school ID: {school_id}."
                )
            


            valid_departments = set(teacher.department_ID.values_list('department_ID', flat=True))  # Use .values_list to get IDs

            # Check if the provided department ID is valid for the teacher
            department_id = self.initial_data.get('department_ID')

            # Check if department_id is in the list of valid departments
            if department_id is not None and department_id not in valid_departments:
                raise serializers.ValidationError(
                    f"Teacher {teacher.employee_id} does not belong to department ID: {department_id}."
                )
        return value
