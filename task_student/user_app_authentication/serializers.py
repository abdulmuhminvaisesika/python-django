from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['employee_id', 'username', 'password', 'first_name', 'last_name', 'performance', 'is_active', 'created_on', 'updated_on', 'school_ID', 'department_ID']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):


        department_ids = validated_data.pop('department_ID', [])


        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()

        user.department_ID.set(department_ids)


        return user
