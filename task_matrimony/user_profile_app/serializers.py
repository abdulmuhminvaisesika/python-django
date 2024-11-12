from rest_framework import serializers
from .models import User_Profile_Table
from common_maching_app.serailizers import CommonMatchingSerializer  # Import serializer for Common_Matching model

class UserProfileSerializer(serializers.ModelSerializer):
    # Use the CommonMatchingSerializer for ForeignKey fields
    age = CommonMatchingSerializer()
    gender = CommonMatchingSerializer()
    weight = CommonMatchingSerializer()
    height = CommonMatchingSerializer()
    religion = CommonMatchingSerializer()
    caste = CommonMatchingSerializer()
    income = CommonMatchingSerializer()
    profession = CommonMatchingSerializer()
    education = CommonMatchingSerializer()
    location = CommonMatchingSerializer()
    marital_status = CommonMatchingSerializer()
    language = CommonMatchingSerializer()

    class Meta:
        model = User_Profile_Table
        fields = [
            'user', 'age', 'gender', 'dob', 'bio', 'weight', 'height', 'religion', 'caste',
            'income', 'profession', 'education', 'location', 'created_on', 'updated_on',
            'marital_status', 'address', 'language', 'image'
        ]
        read_only_fields = ['created_on', 'updated_on']

    def validate_age(self, value):
        """Validate that age is at least 18"""
        if value < 18:
            raise serializers.ValidationError("Age should be more than 18")
        return value

    def validate_income(self, value):
        """Validate that income is non-negative"""
        if value < 0:
            raise serializers.ValidationError("Income can't be negative")
        return value
