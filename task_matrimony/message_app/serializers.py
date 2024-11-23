
from rest_framework.serializers import ModelSerializer


from .models import MessageTable
from rest_framework import serializers


class MessageSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, required=False)
    updated_at = serializers.DateTimeField(read_only=True, required=False)
    class Meta:
        model = MessageTable
        fields = '__all__'