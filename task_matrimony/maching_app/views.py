from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from user_app.models import CustomUser
from user_profile_app.models import User_Profile_Table
from notification_app.models import Notification_Table
from preferance_app.models import Preference
from .models import Matching  # Import the Matching model if score storage is required
from utils import calculate_matching_score
from .serializers import MatchingScoreModelSerializer
from user_profile_app.serializers import UserProfileSerializer


class MatchingScoreView(APIView):

    """
    Calculate the matching score between two users based on their preferences and profile data.
    Accepts user1_id and user2_id in the request body.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user1_id = request.data.get('user1_id')
        user2_id = request.data.get('user2_id')


        # Check if user1 is the same as user2
        if user1_id == user2_id:
            return Response(
                {"error": "User cannot be matched with themselves."},
                status=status.HTTP_400_BAD_REQUEST
            )
        

        if not user1_id or not user2_id:
            return Response({"error": "Both user1_id and user2_id are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user objects
        try:
            user1= get_object_or_404(CustomUser, user_id=user1_id)
            if user1.subcription_plan == None:
                return Response({"error": "You need to subscribe to a plan to match with others. Subscribe to a plan to read it!"}, status=status.HTTP_200_OK)
            
            user1_preferences = get_object_or_404(Preference, user=user1_id)
            user2_profile = get_object_or_404(User_Profile_Table, user=user2_id)
        except ObjectDoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        # Calculate the matching score using the most recent profile and preference data
        score = calculate_matching_score(user1_preferences, user2_profile)

        if score == 0:
            return Response({"message": "You can't match with a user of the same gender. This app does not support LGBTQ matches."}, status=status.HTTP_200_OK)
        
        # Save the matching score to the Matching model
        match, created = Matching.objects.update_or_create(
            user1_id=user1_id,
            user2_id=user2_id,
            defaults={'score': score, 'status': 'Pending'}
        )
        # Serialize the matching score
        serializer = MatchingScoreModelSerializer(match)


        user1 = get_object_or_404(CustomUser, user_id=user1_id)

        # Create a notification for the receiver
        Notification_Table.objects.create(
            receiver_id_id=user2_id,
                notification_type="request",
            notification_message=f"{ user1.username} has sent you a match request.",
            is_read=False
        )
        


        

        return Response(serializer.data, status=status.HTTP_200_OK)

        




class UserMatchingRecomentaion(APIView):
    """
    Get or create the matching scores between a given user and all other users.
    Returns users and their matching scores in descending order.
    """
    permission_classes = [permissions.IsAuthenticated]  # Ensure the user is authenticated

    def get(self,request):
        user_id = request.user.user_id

        users = User_Profile_Table.objects.exclude(user=user_id).exclude(gender=get_object_or_404(User_Profile_Table, user=user_id).gender).exclude(user__subcription_plan__isnull = True) 
        
        matching_scores = []
        # show the maching score the users not save in database
        for user in users:
            user1_preferences = get_object_or_404(Preference, user=user_id)
            user2_profile = get_object_or_404(User_Profile_Table, user=user.user_id)
            score = calculate_matching_score(user1_preferences, user2_profile)
            # Add user1 ID, user2 ID, and score to the list

            matching_scores.append({
                'recomended_user': user.user.username,
                'score': score, 
                'recomended_user_profile': UserProfileSerializer(user).data
                
            })
            
            # Sort the matching scores in descending order
            matching_scores.sort(key=lambda x: x['score'], reverse=True)
        
        
        # Serialize the matching scores
        return Response({f"recomendations for the {request.user.username } ":matching_scores}, status=status.HTTP_200_OK)
    

       
        

        



class UpdateMachingStatus(APIView):
    """
    Update the status of a matching record.
    Accepts the matching IDs in the URL and the new status in the request body.
    """
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        # Extracting user1 and user2 from the URL parameters
        user1 = request.user.user_id
        user2 = self.kwargs['user_id']

        
        try:
            # Retrieve the matching record between user1 and user2
            matching = Matching.objects.get(user1=user1, user2=user2)
        except Matching.DoesNotExist:
            return Response({"error": "Matching record not found."}, status=status.HTTP_404_NOT_FOUND)


        new_status = request.data.get('status')
        if new_status not in dict(Matching.STATUS_CHOICES).keys():
            return Response({"error": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the status
        matching.status = new_status
        matching.save()

        if new_status == 'Pending':
            # Create a notification for the sender
            Notification_Table.objects.create(
                sender_id_id=user1,
                receiver_id_id=user2,
                notification_type="request",
                notification_message=f"{matching.user1.username} has accepted your match request.",
                is_read=False
            )
        elif new_status == 'Accepted':
            # Create a notification for the sender
            Notification_Table.objects.create(
                sender_id_id=user2,
                receiver_id_id=user1,
                notification_type="accepted",
                notification_message=f"{matching.user2.username} has accepted your match request.",
                is_read=False
            )
        elif new_status == 'Rejected':
            # Create a notification for the sender
            Notification_Table.objects.create(
                sender_id_id=user2,
                receiver_id_id=user1,
                notification_type="rejected",
                notification_message=f"{matching.user2.username} has rejected your match request.",
                is_read=False
            )


        # Serialize the updated matching object
        serializer = MatchingScoreModelSerializer(matching)

        return Response(serializer.data, status=status.HTTP_200_OK)
