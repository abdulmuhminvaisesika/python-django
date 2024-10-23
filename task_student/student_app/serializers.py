from .models import Student_Task, Teacher_Task
from rest_framework import serializers
 
class TeacherTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Task
        fields = ['name', 'employee_id','perfomance']  
 
class StudentTaskSerializer(serializers.ModelSerializer):
    teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teacher_Task.objects.all())  # Allow write access

    class Meta:
        model = Student_Task
        fields = ['name', 'roll_no', 'chemistry', 'physics', 'maths', 'total_marks_field', 'percentage_field', 'teacher_id']