from rest_framework.serializers import ModelSerializer


from .models import MessageTable


class MessageSerializer(ModelSerializer):
    class Meta:
        model = MessageTable
        fields = [
        'message_id', 'sender_id', 'receiver_id', 'message_content', 
        'is_read'
        ]