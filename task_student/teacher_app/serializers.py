from rest_framework import serializers
from .models import Teachers_Task 
from school_app.models import School_Task
from department_app.models import Department_Task

class TeacherTaskSerializer(serializers.ModelSerializer):
    school_ID = serializers.PrimaryKeyRelatedField(queryset=School_Task.objects.all())
    department_ID = serializers.PrimaryKeyRelatedField(queryset=Department_Task.objects.all())

    class Meta:
        model = Teachers_Task
        fields = ['name', 'employee_id', 'performance', 'school_ID', 'department_ID','created_on','updated_on']  
