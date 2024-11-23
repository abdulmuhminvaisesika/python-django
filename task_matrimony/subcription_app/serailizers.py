from .models import SubcriptionTable,SubcriptionsForUser
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers




class SubcriptionSerializer(ModelSerializer):
    class Meta:
        model = SubcriptionTable
        fields = '__all__'

class SubcriptionsForUserSerializer(ModelSerializer):
    subcription_started_at= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
    subcription_end_at= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = SubcriptionsForUser
        fields = '__all__'
        