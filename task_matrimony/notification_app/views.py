from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Notification_Table
from .serializers import NotificationSerializer
from user_app.models import CustomUser




class NotificationCrudOperation(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request):
        # Check if the user is an admin
        if not request.user.is_staff:
            raise PermissionDenied("Only admin users can create notifications.")
        
        type= request.data.get('type')
        if type != 'bulck':
            return Response({"error": "currently admin can only create bulck notifications."}, status=400)
        message = request.data.get('message')
        if not message:
            return Response({"error": "Message is required."}, status=400)
        users = CustomUser.objects.filter(is_active=True,is_staff=False)

        for user in users:
            Notification_Table.objects.create(
                receiver_id=user,
                notification_type="bulck",
                notification_message=message,
                is_read=False
            )
        
        return Response({"message": "Notifications created successfully."}, status=201)


      
   



class UnreadNotificationCount(ListAPIView):
    """
    API view to retrieve the count of unread notifications for the authenticated user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the authenticated user's ID
        receiver_id = self.request.user.user_id

        # Fetch unread notifications for the user
        queryset = Notification_Table.objects.filter(receiver_id=receiver_id, is_read=False)

        return queryset



   

class GetNotificationByReceiver(ListAPIView):
    """
    API view to retrieve notifications for the authenticated user.
    Marks notifications as read once they are fetched.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the authenticated user's ID
        receiver_id = self.request.user.user_id

        # Fetch unread notifications for the user
        queryset = Notification_Table.objects.filter(receiver_id=receiver_id).order_by('-created_at')

        # Update `is_read` status to True for the fetched notifications
        queryset.update(is_read=True)

        return queryset
    