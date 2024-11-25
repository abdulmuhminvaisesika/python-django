from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Notification_Table
from .serializers import NotificationSerializer





class NotificationCrudOperation(ListCreateAPIView):

    queryset = Notification_Table.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]







class GetNotificationByReceiver(APIView):
    """
    Fetch all messages sent to a specific user (receiver_id) using the URL.
    Example URL: http://127.0.0.1:8000/messages/new_message/receiver_id/
    """

    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    
    def get(self, request, receiver_id, *args, **kwargs):
        
        # Check if the authenticated user is the same as the receiver_id
        if request.user.user_id != receiver_id:
            raise PermissionDenied("You are not authorized to view these messages.")

        # Fetch all unread notifications sent to the receiver
        unread_notifications = Notification_Table.objects.filter(receiver_id=receiver_id, is_read=False).order_by('-created_at')
        

        # Fetch the new notifications (last sent notifications)
        read_notifications = Notification_Table.objects.filter(receiver_id=receiver_id, is_read=True).order_by('-created_at')


        # Serialize the notifications
        unread_serializer = NotificationSerializer(unread_notifications, many=True)
        read_serializer = NotificationSerializer(read_notifications, many=True)        

        # Prepare the response
        response = Response({
            "unread messages": unread_serializer.data,
            "read messages": read_serializer.data,
        })

        # Mark all unread notifications as read after sending the response
        unread_notifications.update(is_read=True)

        return response
        






