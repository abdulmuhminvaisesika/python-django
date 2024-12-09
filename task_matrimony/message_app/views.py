from django.db.models import Q
from django.shortcuts import get_object_or_404


from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import status
from rest_framework.pagination import PageNumberPagination

from .models import MessageTable
from .serializers import MessageSerializer
from notification_app.models import Notification_Table
from django.db import models
from user_app.models import CustomUser


class MessageCrudOperation(APIView):
    """
    API view to create messages and handle messaging operations.
    URL Example: POST /messages/<receiver_id>/
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, receiver_id=None):
        # Validate receiver ID from URL
        if not receiver_id:
            return Response({"error": "Receiver ID is required in the URL."}, status=status.HTTP_400_BAD_REQUEST)
        if not CustomUser.objects.filter(user_id=receiver_id).exists():
            return Response({"error": "Receiver does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        if receiver_id == request.user.user_id:
            return Response({"error": "You cannot send a message to yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        

        # Verify receiver exists
        receiver = get_object_or_404(CustomUser, user_id=receiver_id)
        

        # Get sender (authenticated user)
        sender_id = request.user.user_id

        sender = get_object_or_404(CustomUser, user_id=sender_id)
        if sender.subcription_plan == None:
            return Response({"error": "You need to subscribe to a plan to send messages."}, status=status.HTTP_400_BAD_REQUEST)



        # Extract message content from request data
        message_content = request.data.get("message_content")
        if not message_content:
            return Response({"error": "Message content is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare data for serialization
        data = {
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "message_content": message_content
        }

        # Serialize and validate
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            
            if receiver.subcription_plan == None:
                Notification_Table.objects.create(
                    receiver_id_id=receiver_id,
                    notification_type="new_message",
                    notification_message=f"{request.user.username} has sent you a message. Subscribe to a plan to read it!",
                    is_read=False
                )
            else:
                # Create a notification for the receiver
                Notification_Table.objects.create(
                    receiver_id_id=receiver_id,
                    notification_type="new_message",
                    notification_message=f"{request.user.username} has sent you a message. Check it now!",
                    is_read=False
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class TotalMessagesOnReceiver(ListAPIView):
    """
    API view to list messages received by the authenticated user.
    URL Example: GET /messages/
    """

    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # Get the authenticated user's ID
        receiver_id = self.request.user.user_id
        receiver = get_object_or_404(CustomUser, user_id=receiver_id)
        if receiver.subcription_plan == None:
            raise PermissionDenied("You need to subscribe to a plan to read messages.")

        # Fetch unread messages received by the user
        queryset = MessageTable.objects.filter(receiver_id=receiver_id, is_read=False).order_by('-created_at')

        return queryset

    

class GetAllMessageHistoryOfTwoUsers(APIView):
    """
    Fetch all messages between the current authenticated user and a receiver.
    Example URL: http://127.0.0.1:8000/messages/<receiver_id>/
    """

    permission_classes = [IsAuthenticated]  # Ensures user is authenticated

    def get(self, request, receiver_id=None):
        # Ensure receiver ID is provided
        if not receiver_id:
            return Response({"error": "Receiver ID is required."}, status=400)

        try:
            # Get current user ID from the token
            user1_id = request.user.user_id
            user = get_object_or_404(CustomUser, user_id=user1_id)
            receiver = get_object_or_404(CustomUser, user_id=receiver_id)

            if user.subcription_plan == None or receiver.subcription_plan == None:
                raise PermissionDenied("both user has to been subcribed!")
           
            # Query for messages sent between the current user and the receiver
            messages = MessageTable.objects.filter(
                Q(sender_id=user1_id, receiver_id=receiver_id) |
                Q(sender_id=receiver_id, receiver_id=user1_id)
            ).order_by('-created_at')
            # Update `is_read` for messages where the receiver is the current user
            messages.filter(receiver_id=user1_id, is_read=False).update(is_read=True)

            serailizers = MessageSerializer(messages, many=True)
            return Response(serailizers.data, status=200)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)