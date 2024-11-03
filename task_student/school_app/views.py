
#resr framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Local Imports
from .models import School_Task
from .serializers import SchoolTaskSerializer  
from department_app.models import Department_Task
from department_app.serializers import DepartmentTaskSerializer
from teacher_app.models import Teachers_Task
from teacher_app.serializers import TeacherTaskSerializer
from student_app.models import Student_Task
from student_app.serializers import StudentTaskSerializer

# Create your views here.
class SchoolCrudOperations(APIView):
    def get(self, request, school_ID=None):

        try:
            # If a primary key is provided, retrieve a specific school
            if school_ID:  
                try:
                    school = School_Task.objects.get(school_ID=school_ID)
                    serializer = SchoolTaskSerializer(school)
                    return Response(serializer.data)
                except School_Task.DoesNotExist:
                    return Response({"error":"School with the specific id not found"}, status=status.HTTP_400_BAD_REQUEST)

            # If no primary key, return all schools
            schools = School_Task.objects.all()
            serializer = SchoolTaskSerializer(schools, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

    


class SchoolUnderTask(APIView):

    def get(self, request, school_ID):

        if 'student' in request.path:
            return self.student_under_school(request,school_ID)
        elif 'teacher' in request.path:
            return self.teacher_under_school(request, school_ID)
        
    
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)
    

    
    def teacher_under_school(self, request, school_ID):
        '''
        Retrieves a list of teachers associated with a specific school.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/schools/teacher/shcool_ID/
        '''

        
        try:
            teachers = Teachers_Task.objects.filter(school_ID=school_ID)    
            serializer = TeacherTaskSerializer(teachers, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def student_under_school(self, request, school_ID):
        '''
        Retrieves a list of students associated with a specific school.
        Use Postman to test this API at the following URL:http://127.0.0.1:8000/schools/student/school_ID/
        '''
        try:
            students = Student_Task.objects.filter(school_ID=school_ID)
            serializer = StudentTaskSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    

class SchoolStatusView(APIView):
    def get(self, request, status):
        if status == 'active':
            schools = School_Task.objects.filter(is_active=True)
        elif status == 'inactive':
            schools = School_Task.objects.filter(is_active=False)
        else:
            return Response({"error": "Invalid status. Use 'active' or 'inactive'."}, status=400)
        
        serializer = SchoolTaskSerializer(schools, many=True)
        return Response(serializer.data)
