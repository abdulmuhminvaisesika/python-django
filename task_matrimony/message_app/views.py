
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import status

from .models import MessageTable
from .serializers import MessageSerializer
from notification_app.models import Notification_Table


class MessageCrudOperation(ListCreateAPIView):

    queryset = MessageTable.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'sender_id'



    def create(self, request, *args, **kwargs):
        # Extract sender and receiver IDs from the request
        user1_id = request.user.user_id  # Assuming the sender is the logged-in user
        user2_id = request.data.get('receiver_id')  # Provided in the request data

        # Save the message
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Create a notification for the receiver
        Notification_Table.objects.create(
            sender_id_id=user1_id,  # ForeignKey field for sender
            receiver_id_id=user2_id,  # ForeignKey field for receiver
            notification_type="new_message",
            notification_message=f"{user1_id} has sent you a message. Check it now!",
            is_read=False
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetMessagesByReceiver(APIView):
    """
    Fetch all messages sent to a specific user (receiver_id) using the URL.
    Example URL: http://127.0.0.1:8000/messages/new_message/receiver_id/
    """

    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    
    def get(self, request, receiver_id, *args, **kwargs):
        
        # Check if the authenticated user is the same as the receiver_id
        if request.user.user_id != receiver_id:
            raise PermissionDenied("You are not authorized to view these messages.")

        # Fetch all unread messages sent to the receiver
        unread_messages = MessageTable.objects.filter(receiver_id=receiver_id, is_read=False).order_by('-created_at')
        

        # Fetch the new message (last sent message)
        read_message = MessageTable.objects.filter(receiver_id=receiver_id, is_read=True).order_by('-created_at')


        # Serialize the messages
        unread_serializer = MessageSerializer(unread_messages, many=True)
        read_serializer = MessageSerializer(read_message, many=True)        

        # Prepare the response
        response = Response({
            "unread messages": unread_serializer.data,
            "read messages": read_serializer.data,
        })

        # Mark all unread messages as read after sending the response
        unread_messages.update(is_read=True)

        return response
        
