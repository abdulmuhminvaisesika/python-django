from rest_framework import serializers
from .models import Student_Task  # Assuming you have a Student_Task model

class StudentTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Task
        fields = ['name', 'roll_no', 'chemistry', 'physics', 'maths', 'total_marks_field', 'percentage_field', 'teacher_id','created_on','updated_on']