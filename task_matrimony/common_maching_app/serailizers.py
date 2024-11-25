from rest_framework import serializers
from .models import Common_Matching

class CommonMatchingSerializer(serializers.ModelSerializer):

    created_on= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
    updated_on= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False) 
      
    class Meta:
        model = Common_Matching
        fields = ['id', 'type', 'code', 'name', 'display_name', 'created_on','updated_on']
