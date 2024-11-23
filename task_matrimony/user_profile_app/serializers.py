# serializers.py in profile_app
from rest_framework import serializers
from .models import User_Profile_Table
from utils import validate_common_matching  # Import the utility function

class UserProfileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
    updated_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = User_Profile_Table
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, attrs):
        field_mappings = {
            'location': 'location',
            'education': 'education',
            'profession': 'profession',
            'caste': 'caste',
            'religion': 'religion',
            'gender': 'gender',
            'marital_status': 'marital_status',
            'language': 'language'
        }

        for field, field_type in field_mappings.items():
            if field in attrs:
                attrs[field] = validate_common_matching(attrs[field], field_type)
            


        return attrs
