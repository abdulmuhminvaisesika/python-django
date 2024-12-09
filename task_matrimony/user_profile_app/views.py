from django.shortcuts import get_object_or_404

from rest_framework.exceptions import NotFound
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser


from .models import User_Profile_Table
from .serializers import UserProfileSerializer
from preferance_app.models import Preference
from user_app.models import CustomUser
from .models import User_Profile_Table
from maching_app.models import Matching
from .serializers import UserProfileSerializer
from utils import get_user_object_or_permission_denied  # Import the optimized utility function
from notification_app.models import Notification_Table
from utils import calculate_matching_score

class UserProfileListCreateView(APIView):
    """
    List all user profiles or create a new profile.
    """
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        """
        List all user profiles.
        """
        profiles = User_Profile_Table.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileCreateView(APIView):
    """
    Create a new user profile.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        """
        Create a new profile and associate the user with it.
        """

        # Check if a profile for the user already exists
        if User_Profile_Table.objects.filter(user=request.user).exists():
            return Response(
                {"error": "A profile already exists for this user."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new profile and associate the user with it
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            # Save the profile
            user_profile = serializer.save(user=request.user)

            # Get all existing user preferences
            preferences = Preference.objects.all()

            # Get the profile of the new user
            profile = get_object_or_404(User_Profile_Table, user=request.user)

            # Iterate over preferences and calculate the matching score
            for user_preference in preferences:
                # Calculate matching score between the new profile and existing user preferences
                score = calculate_matching_score(user_preference, profile)

                # If score is above 0, send a notification
                if score > 0:
                    # Send a notification to the user with the matching score
                    Notification_Table.objects.create(
                        receiver_id_id=user_preference.user.user_id,  # Notification for this user
                        notification_type="profile",
                        notification_message=f"A new match found! '{request.user.username}' has joined the platform with a matching score of {score}%",
                        is_read=False
                    )

            # Return response with the created profile
            return Response({
                "user_profile": UserProfileSerializer(user_profile).data,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific user profile by user_id.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Fetch the specific user profile object associated with the authenticated user.
        """
        current_user = self.request.user 
        if current_user is None:
            raise NotFound("User not found")
        
        # Assuming you're fetching the profile for the currently authenticated user:
        return User_Profile_Table.objects.get(user=current_user)

    def perform_update(self, serializer):
        """
        Perform the update operation on the user profile, ensuring the authenticated user is the one making the request.
        """
        profile = self.get_object()  # Fetch and validate the profile object
        serializer.save(user=self.request.user)  # Save the profile with the authenticated user
