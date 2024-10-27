from department_app.models import Department_Task
from rest_framework import serializers
from school_app.models import School_Task

class DepartmentTaskSerializer(serializers.ModelSerializer):
    school_ID = serializers.PrimaryKeyRelatedField(queryset=School_Task.objects.all())  # Adjusted to match your model field
    department_HOD = serializers.PrimaryKeyRelatedField(queryset=Department_Task.objects.all())
    class Meta:
        model = Department_Task
        fields = ['department_ID', 'department_name', 'department_HOD', 'school_ID','created_on','updated_on']  
