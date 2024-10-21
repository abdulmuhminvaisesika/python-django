from .models import Student_Task
from rest_framework import serializers



class StudentTaskSerializer(serializers.ModelSerializer):
    

    class Meta:
        
        model = Student_Task
        fields = '__all__'

    