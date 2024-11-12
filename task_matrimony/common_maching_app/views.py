# common_maching_app/views.py
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Common_Matching
from .serailizers import CommonMatchingSerializer

class CommonMatchingListCreateView(generics.ListCreateAPIView):
    queryset = Common_Matching.objects.all()
    serializer_class = CommonMatchingSerializer
    permission_classes = [IsAdminUser]


# common_maching_app/views
class CommonMatchingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Common_Matching.objects.all()
    serializer_class = CommonMatchingSerializer
    permission_classes = [IsAdminUser]
