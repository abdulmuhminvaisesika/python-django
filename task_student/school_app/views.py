from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import School_Task
from .serializers import SchoolTaskSerializer  # Make sure to create this serializer

# Create your views here.

# Create your views here.
class SchoolCrudOperations(APIView):
    def get(self, request, school_ID=None):
        if school_ID:  # If a primary key is provided, retrieve a specific school
            try:
                school = School_Task.objects.get(school_ID=school_ID)
                serializer = SchoolTaskSerializer(school)
                return Response(serializer.data)
            except School_Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        # If no primary key, return all schools
        schools = School_Task.objects.all()
        serializer = SchoolTaskSerializer(schools, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = SchoolTaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, school_ID=None):
        try:
            school = School_Task.objects.get(school_ID=school_ID)
        except School_Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SchoolTaskSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, school_ID=None):
        try:
            school = School_Task.objects.get(school_ID=school_ID)
            school.delete()
            return Response({"succes":"school has been deleted"},status=status.HTTP_204_NO_CONTENT)
        except School_Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
