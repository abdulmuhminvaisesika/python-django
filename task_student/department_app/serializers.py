from department_app.models import Department_Task
from rest_framework import serializers
from teacher_app.models import Teachers_Task

class DepartmentTaskSerializer(serializers.ModelSerializer):
    department_HOD = serializers.PrimaryKeyRelatedField(queryset=Teachers_Task.objects.all())  # Use Teachers_Task

    class Meta:
        model = Department_Task
        fields = '__all__'