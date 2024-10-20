from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
from .models import Student
from .serializers import Studentserializers
# Create your views here.
 
class StudentView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=Studentserializers(students, many=True)
        return Response(serializer.data)
 
 
    def post(self,request):
        serialize=Studentserializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
   
class StudentDetailView(APIView):
    def get(self,request,id):
        students=Student.objects.get(id=id)
        serializer=Studentserializers(students)
        return Response(serializer.data)
 
    def delete(self,request,id):
        try:
            students = Student.objects.get(id=id)
            name=students.Name
            students.delete()
            return Response({'message': f'Student {name} deleted successfully'}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
        # Handle the case where the student doesn't exist
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
        # Log and handle other exceptions
            print(e)
            return Response({'error': 'An error occurred'}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,request,id):
        students=Student.objects.get(id=id)
        serialize=Studentserializers(students,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)