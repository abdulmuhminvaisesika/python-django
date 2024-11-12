from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions


from .models import Preference
from .serializers import PreferenceSerializer

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
    Retrieve, update, or delete a specific preference.
    """
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to view or edit their own preferences
        return Preference.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Save updates and link to the authenticated user
        serializer.save(user=self.request.user)
