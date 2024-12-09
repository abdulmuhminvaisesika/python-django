from rest_framework import serializers
from .models import User_Profile_Table
from utils import validate_common_matching
from django.utils import timezone
from datetime import date

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Profile_Table
        fields = [
        'user', 'age', 'gender', 'dob', 'bio', 'weight', 'height',
        'religion', 'caste', 'income', 'profession', 'education',
        'location', 'marital_status', 'language', 'address', 'image']
        read_only_fields = ['user']

    def calculate_age(self, dob):
        """Calculate age from date of birth."""
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def validate(self, attrs):
        """
        Perform combined validation for `dob` and `age`.
        """
        dob = attrs.get('dob', self.instance.dob if self.instance else None)
        age = attrs.get('age', self.instance.age if self.instance else None)

        if dob:
            # Calculate the age from `dob`
            calculated_age = self.calculate_age(dob)

            # If age is provided but doesn't match the calculated age, update the age field
            if age is not None and age != calculated_age:
                attrs['age'] = calculated_age

            # Enforce the age range between 18 and 50 years
            if not (18 <= calculated_age <= 50):
                raise serializers.ValidationError({"dob": "Age must be between 18 and 50 years."})

            # Auto-fill `age` if not provided
            if age is None:
                attrs['age'] = calculated_age

        # Perform additional field-specific validations
        field_mappings = {
            'location': 'location',
            'education': 'education',
            'profession': 'profession',
            'caste': 'caste',
            'religion': 'religion',
            'gender': 'gender',
            'marital_status': 'marital_status',
            'language': 'language',
        }

        for field, field_type in field_mappings.items():
            if field in attrs:
                attrs[field] = validate_common_matching(attrs[field], field_type)

        return attrs
    


