from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    join_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = CustomUser
        fields = [
            'user_id', 'username', 'password', 'email', 'first_name', 'last_name',
            'role','subcription_plan','join_date', 'last_login', 'is_active', 'is_admin'
        ]
        extra_kwargs = {'password': {'write_only': True}}  # Password is write-only for security

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)  # Hash the password
        user.save()
        return user
    
