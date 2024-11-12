

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Matching
from .serializers import MatchingSerializer

class MatchingView(APIView):
    def post(self, request):
        serializer = MatchingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return errors as JSON
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
                # Retrieve all Matching instances
            matching = Matching.objects.all()
                # Serialize the queryset
            serializer = MatchingSerializer(matching, many=True)
                # Return serialized data with status 200 OK
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR0)