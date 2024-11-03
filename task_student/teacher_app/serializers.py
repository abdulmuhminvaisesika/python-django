#django imports
from django.shortcuts import get_object_or_404

#restframework import
from rest_framework import serializers

#local imports
from .models import Teachers_Task
from school_app.models import School_Task
from department_app.models import Department_Task

class TeacherTaskSerializer(serializers.ModelSerializer):
    school_ID = serializers.PrimaryKeyRelatedField(queryset=School_Task.objects.all())
    department_ID = serializers.PrimaryKeyRelatedField(many=True, queryset=Department_Task.objects.all())  # Change to many=True

    class Meta:
        model = Teachers_Task
        fields = ['employee_id', 'name', 'performance', 'school_ID', 'department_ID', 'is_active', 'created_on', 'updated_on']

    def validate_department_ID(self, value):
        # Get the school ID from the input data
        school_id = self.initial_data.get('school_ID')
        
        if school_id:
            # Use get_object_or_404 to retrieve the school
            school = get_object_or_404(School_Task, school_ID=school_id)
            
            # Get the valid department IDs for this school
            valid_departments = set(school.department_ID.values_list('department_ID', flat=True))

            # Check if the selected departments are valid for the school
            for department in value:
                if department.department_ID not in valid_departments:
                    raise serializers.ValidationError(
                        f"Department {department.department_name} (ID: {department.pk}) is not associated with the selected school."
                    )
        
        return value
