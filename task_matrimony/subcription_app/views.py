from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


from .models import SubcriptionTable,SubcriptionsForUser
from .serailizers import SubcriptionSerializer,SubcriptionsForUserSerializer
from user_app.models import CustomUser
from notification_app.models import Notification_Table

# Create your views here.




class SubcriptionCrudOperation(ListCreateAPIView):

    queryset = SubcriptionTable.objects.all()
    serializer_class = SubcriptionSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):

        all_users = CustomUser.objects.all()



        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the subscription instance and capture it
        subscription = serializer.save()  


        for user in all_users:


            Notification_Table.objects.create(
                sender_id_id="AD001",  # Replace with admin user ID if necessary
                receiver_id_id=user.user_id,  # Using `user_id` as the primary key
                notification_type="offer",
                notification_message=f"New Offer! A new subscription '{ subscription.subcription_type }' is now available. Check it out!",
                is_read=False
                )
        return Response(
            {"Subscription created and notifications sent to all users!": serializer.data},
            status=status.HTTP_201_CREATED
        )
            



class SubcriptionCrudOperationWithSubcriptionType(RetrieveUpdateDestroyAPIView):

    queryset = SubcriptionTable.objects.all()
    serializer_class = SubcriptionSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'subcription_type'

    
class SubcriptionList(ListCreateAPIView):

    queryset = SubcriptionsForUser.objects.all()
    serializer_class = SubcriptionsForUserSerializer
    permission_classes = [IsAdminUser]




