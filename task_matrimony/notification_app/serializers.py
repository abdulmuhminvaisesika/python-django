
from rest_framework.serializers import ModelSerializer

from .models import Notification_Table
from rest_framework import serializers


class NotificationSerializer(ModelSerializer):
    notification_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    
    class Meta:
        model = Notification_Table
        fields = '__all__'