from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied


from .models import Preference
from .serializers import PreferenceSerializer
from utils import get_user_object_or_permission_denied  # Import the optimized utility function

class PreferenceListCreateView(generics.ListCreateAPIView):
    """
    List all preferences or create a new preference for a user.
    """
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the preference is linked to the currently authenticated user
        serializer.save(user=self.request.user)


class PreferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific preference for a given user_id.
    Ensures that only the authenticated user can access and modify their own preferences.
    """
    serializer_class = PreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Fetch the specific preference object associated with the user_id, 
        and ensure the authenticated user has permission to access it.
        """
        user_id = self.kwargs.get('user_id')
        return get_user_object_or_permission_denied(user_id, Preference, self.request.user)

    def perform_update(self, serializer):
        """
        Perform the update operation on the preference, ensuring the authenticated user is the one making the request.
        """
        preference = self.get_object()  # Fetch and validate the preference object
        serializer.save(user=self.request.user)  