from rest_framework import serializers
from .models import Common_Matching

class CommonMatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common_Matching
        fields = ['id', 'type', 'code', 'name', 'display_name']
