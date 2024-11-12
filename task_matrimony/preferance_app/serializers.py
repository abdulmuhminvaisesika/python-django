from rest_framework import serializers
from .models import Preference
from common_maching_app.serailizers import CommonMatchingSerializer

class PreferenceSerializer(serializers.ModelSerializer):
    age = CommonMatchingSerializer(many=True)
    gender = CommonMatchingSerializer(many=True)
    religion = CommonMatchingSerializer(many=True)
    caste = CommonMatchingSerializer(many=True)
    income = CommonMatchingSerializer(many=True)
    profession = CommonMatchingSerializer(many=True)
    education = CommonMatchingSerializer(many=True)
    location = CommonMatchingSerializer(many=True)
    height = CommonMatchingSerializer(many=True)
    weight = CommonMatchingSerializer(many=True)

    class Meta:
        model = Preference
        fields = ['user', 'age', 'gender', 'religion', 'caste', 'income', 'profession', 'education', 'location', 'height', 'weight', 'created_on', 'updated_on']
