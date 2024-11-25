# common_maching_app/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Common_Matching
from .serailizers import CommonMatchingSerializer
from user_app.models import CustomUser
from notification_app.models import Notification_Table


class CommonMatchingListCreateView(generics.ListCreateAPIView):
    queryset = Common_Matching.objects.all()
    serializer_class = CommonMatchingSerializer
    permission_classes = [IsAdminUser]


    def create(self, request, *args, **kwargs):

        all_users = CustomUser.objects.all()



        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the subscription instance and capture it
        master_table = serializer.save()  


        for user in all_users:


            Notification_Table.objects.create(
                sender_id_id="AD001",  # Replace with admin user ID if necessary
                receiver_id_id=user.user_id,  # Using `user_id` as the primary key
                notification_type="reminder",
                notification_message = f"New {master_table.type} option '{master_table.name}' added by Admin. Update your profile and preferences now!",
                is_read=False
                )
        return Response(
            {"new option is created and notifications sent to all users!": serializer.data},
            status=status.HTTP_201_CREATED
        )
            




# common_maching_app/views
class CommonMatchingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Common_Matching.objects.all()
    serializer_class = CommonMatchingSerializer
    permission_classes = [IsAdminUser]

class CommonMatchingOptionsView(APIView):
    def get(self, request, field_type=None):
        if field_type not in dict(Common_Matching.FIELD_TYPES):
            return Response({"error": "Invalid field type"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filter options by type
        options = Common_Matching.objects.filter(type=field_type)
        serializer = CommonMatchingSerializer(options, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
