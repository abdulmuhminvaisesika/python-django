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
            user1_preferences = get_object_or_404(Preference, user=user1_id)
            user2_profile = get_object_or_404(User_Profile_Table, user=user2_id)
        except ObjectDoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        print(">>>>>>>>", user1_preferences)
        print(">>>>>>>>", user2_profile)
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

        # Debugging output: Check status before notification
        print(f"Match status: {match.status}")
        print(f"Matching score: {score}")

        user1 = get_object_or_404(CustomUser, user_id=user1_id)

        # Create a notification for the receiver
        Notification_Table.objects.create(
            sender_id_id=user1_id,
            receiver_id_id=user2_id,
                notification_type="request",
            notification_message=f"{ user1.username} has sent you a match request.",
            is_read=False
        )
        print(">>>>>>>>",user1_id)
        print(">>>>>>>>",user2_id)
        


        

        return Response(serializer.data, status=status.HTTP_200_OK)

        




class UserMatchingRecomentaion(APIView):
    """
    Get or create the matching scores between a given user and all other users.
    Returns users and their matching scores in descending order.
    """
    permission_classes = [permissions.IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request, user_id):
        try:
            # Get the user preferences and profile
            user_preferences = Preference.objects.get(user=user_id)
            User_Profile_Table.objects.get(user=user_id)  # Ensure user exists in the profile table
        except (Preference.DoesNotExist, User_Profile_Table.DoesNotExist):
            return Response({"error": "User not found."}, status=404)

        # Get all users, including newly added ones, excluding the provided user_id
        all_users = User_Profile_Table.objects.exclude(user=user_id)
        print(">>>>>>>",all_users)

        # Iterate through all users and calculate match scores
        for user in all_users:
            try:
                user_profile = User_Profile_Table.objects.get(user=user.user_id)
                print(">>>>>>>>", user_profile)
            except User_Profile_Table.DoesNotExist:
                continue

            # Calculate the matching score
            score = calculate_matching_score(user_preferences, user_profile)
            print(">>>>>>>>", score)
            if score > 0:
                # Save the matching score to the Matching model
                match, created = Matching.objects.update_or_create(
                    user1_id=user_id,
                    user2_id=user.user_id,
                    defaults={'score': score, 'status': 'Pending'}
                )
                print(">>>>>>>>", match)
        

        # Retrieve all matching scores for the given user, ordered by score in descending order
        matching_scores = Matching.objects.filter(user1_id=user_id).order_by('-score')
        print(">>>>>>>>", matching_scores)
        # Serialize the matching scores
        serializer = MatchingScoreModelSerializer(matching_scores, many=True)
        print(">>>>>>>>", serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)




class UpdateMachingStatus(APIView):
    """
    Update the status of a matching record.
    Accepts the matching IDs in the URL and the new status in the request body.
    """
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        # Extracting user1 and user2 from the URL parameters
        user1 = self.kwargs['user1']
        user2 = self.kwargs['user2']


        # Ensure the authenticated user is user2
        if request.user.user_id != str(user2):
            return Response(
                {"error": "You are not authorized to update this match status."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            # Retrieve the matching record between user1 and user2
            matching = Matching.objects.get(user1=user1, user2=user2)
        except Matching.DoesNotExist:
            return Response({"error": "Matching record not found."}, status=status.HTTP_404_NOT_FOUND)

        # You can include validation logic for the new status (if needed)
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
