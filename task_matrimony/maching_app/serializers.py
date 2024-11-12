from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Matching
from django.db.models import Q

class MatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matching
        fields = ['user1', 'user2', 'status']

    def validate(self, data):
        user1 = data['user1']
        user2 = data['user2']
        
        # Prevent a user from matching with themselves
        if user1 == user2:
            raise ValidationError({"error": "A user cannot match with themselves."})
        
        # Ensure only one pending or accepted match exists between two users
        if Matching.objects.filter(
            (Q(user1=user1) & Q(user2=user2)) | (Q(user1=user2) & Q(user2=user1)),
            Q(status__in=['Pending', 'Accepted'])
        ).exists():
            raise ValidationError({"error": "Only one pending or accepted match can exist between two users."})
        
        return data
