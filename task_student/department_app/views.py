#rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Local imports
from .models import Department_Task
from .serializers import DepartmentTaskSerializer 
from teacher_app.models import Teachers_Task
from teacher_app.serializers import TeacherTaskSerializer
from student_app.models import Student_Task
from student_app.serializers import StudentTaskSerializer
from school_app.models import School_Task

# Create your views here.

class DepartmentCrudOperations(APIView):
    def get(self, request, department_ID=None):
        # If a primary key is provided, retrieve a specific department
        if department_ID:  
            try:
                department = Department_Task.objects.get(department_ID=department_ID)
                serializer = DepartmentTaskSerializer(department)
                return Response(serializer.data)
            except Department_Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        # If no primary key, return all departments
        departments = Department_Task.objects.all()
        serializer = DepartmentTaskSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        try:
            serializer = DepartmentTaskSerializer(data=request.data)

            if serializer.is_valid():
                print("Validated Data:", serializer.validated_data)  # Debugging line

                department_instance = serializer.save()
                print("Saved Department Instance:", department_instance)  # Debugging line

                return Response(
                    {'message': 'Record created successfully', 'data': DepartmentTaskSerializer(department_instance).data},
                    status=status.HTTP_201_CREATED
                )
                
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, department_ID):
        try:
            department = Department_Task.objects.get(department_ID=department_ID)
        

            serializer = DepartmentTaskSerializer(department, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Department_Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
class DepartmentUnderTask(APIView):
    def get(self, request, department_ID):

        if 'teacher' in request.path:
            return self.teacher_under_department(department_ID)
        elif 'student' in request.path:
            return self.student_under_department(department_ID)
        
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)
    
    def teacher_under_department(self,department_ID):
        '''
        Retrieves a list of teachers associated with a specific department.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/departments/teacher/department_ID/
        '''
        try:
            teachers = Teachers_Task.objects.filter(department_ID=department_ID)
            serializer = TeacherTaskSerializer(teachers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def student_under_department(self,department_ID):
        '''
        Retrieves a list of students associated with a specific department.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/departments/student/department_ID/
        '''
        try:
            students = Student_Task.objects.filter(department_ID=department_ID)
            serializer = StudentTaskSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   



class DepartmentStatusView(APIView):
    def get(self, request, status=None):
        if status == "active":
            departments = Department_Task.objects.filter(is_active=True)
        elif status == "inactive":
            departments = Department_Task.objects.filter(is_active=False)
        else:
            return Response({"error": "Invalid status provided"}, status=400)
        
        serializer = DepartmentTaskSerializer(departments, many=True)
        return Response(serializer.data)
    



class DepartmentsBySchoolView(APIView):
    def get(self, request, school_id):
        try:
            # Get the school instance
            school = School_Task.objects.get(school_ID=school_id)
            
            # Get departments associated with the school
            departments = school.department_ID.all()
            
            # Serialize the departments
            serializer = DepartmentTaskSerializer(departments, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except School_Task.DoesNotExist:
            return Response(
                {"error": "School not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )