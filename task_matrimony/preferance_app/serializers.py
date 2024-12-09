# serializers.py in preference_app
from rest_framework import serializers
from .models import Preference
from utils import validate_common_matching  # Import the utility function

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = [
        'user', 'age_range', 'income_range', 'height_range', 'weight_range',
        'gender', 'religion', 'caste', 'profession', 'education', 'location',
        'language', 'marital_status'
        ]
        read_only_fields = ['user']

    def validate(self, attrs):
        field_mappings = {
            'location': 'location',
            'education': 'education',
            'profession': 'profession',
            'caste': 'caste',
            'religion': 'religion',
            'gender': 'gender',
            'language': 'language',
            'marital_status': 'marital_status',
            
        }

        for field, field_type in field_mappings.items():
            if field in attrs:
                attrs[field] = validate_common_matching(attrs[field], field_type)

        return attrs
