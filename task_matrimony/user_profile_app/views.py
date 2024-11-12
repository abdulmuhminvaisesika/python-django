from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from rest_framework import generics, permissions
from .models import User_Profile_Table
from .serializers import UserProfileSerializer

from .models import User_Profile_Table
from .serializers import UserProfileSerializer
class UserProfileListCreateView(generics.ListCreateAPIView):
    """
    List all user profiles or create a new profile.
    """
    queryset = User_Profile_Table.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the user with the profile
        serializer.save(user=self.request.user)


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific user profile.
    """
    queryset = User_Profile_Table.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to view or edit their own profile
        return User_Profile_Table.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
