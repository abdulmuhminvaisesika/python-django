from .models import Student_Task
from rest_framework import serializers



class StudentTaskSerializer(serializers.ModelSerializer):
    total_marks = serializers.SerializerMethodField()
    percentage = serializers.SerializerMethodField()

    class Meta:
        
        model = Student_Task
        fields = ['name', 'roll_no', 'chemistry', 'physics', 'maths', 'class_teacher', 'total_marks', 'percentage']

    def get_total_marks(self, obj):
        return obj.total_marks()

    def get_percentage(self, obj):
        return obj.percentage()