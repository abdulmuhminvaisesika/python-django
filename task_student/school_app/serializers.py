from rest_framework import serializers
from school_app.models import School_Task



class SchoolTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Task
        fields = ['school_name','school_ID','school_location','department_ID','is_active','created_on','updated_on']