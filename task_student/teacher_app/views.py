#Django Imports


#rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Local Imports
from .models import Teachers_Task
from teacher_app.serializers import TeacherTaskSerializer 
from student_app.models import Student_Task
from student_app.serializers import StudentTaskSerializer





# Create your views here.

class TeacherCrudOperations(APIView):
    def get(self, request, employee_id=None):
        try:
            if employee_id is not None:
                try:
                    teacher = Teachers_Task.objects.get(employee_id=employee_id)
                    serializer = TeacherTaskSerializer(teacher)
                    return Response(serializer.data)
                except Teachers_Task.DoesNotExist:
                    return Response({"error":"id not found"},status=status.HTTP_400_BAD_REQUEST)
            
            # If no teacher_id key, return all teachers
            else:
                teachers = Teachers_Task.objects.all()
                serializer = TeacherTaskSerializer(teachers, many=True)
                return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

    def post(self, request):
        try:
            serializer = TeacherTaskSerializer(data=request.data)
            
            # Validate the input data
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, employee_id=None):
        try:
            # Attempt to retrieve the existing teacher record
            teacher = Teachers_Task.objects.get(employee_id=employee_id)
        except Teachers_Task.DoesNotExist:
            return Response({"message": "Teacher does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Initialize the serializer with the existing teacher's data and the updated data
        serializer = TeacherTaskSerializer(teacher, data=request.data, partial=True)  # Use partial=True to allow partial updates

        # Validate the input data
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teacher updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherUnderTask(APIView):
    def get(self, request, employee_id=None):
        if 'students' in request.path:
            return self.students_under_teacher(employee_id)
        elif 'performance' in request.path:
            return self.performance_of_teacher(employee_id)
        elif 'best_perfomer' in request.path:
            return self.best_perfomer()
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)

    def students_under_teacher(self, employee_id):
        """
        View to get students under a class teacher.
        Use Postman to test this API at the URL: http://127.0.0.1:8000/teachers/students/<teacher_id>
        """
        try:
            students = Student_Task.objects.filter(teacher_id=employee_id)
            serializer = StudentTaskSerializer(students, many=True)
            return Response({
                "class_teacher_id": employee_id,
                "students": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def performance_of_teacher(self, employee_id=None):
        """
        View to get teacher performance. If `employee_id` is provided, retrieve performance for a specific teacher; otherwise, get performance for all teachers.
        """
        try:
            if employee_id:
                
                teachers = Teachers_Task.objects.filter(employee_id=employee_id).values('name', 'performance')
                return Response(teachers, status=status.HTTP_200_OK)
            else:
                
                teachers = Teachers_Task.objects.all().values('name', 'performance')
                return Response(teachers, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def best_perfomer(self):
        try:
            teacher = Teachers_Task.objects.values('name','performance').order_by('-performance').first()
            return Response(teacher, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


        
    

class TeacherStatusView(APIView):
    def get(self, request, status):
        if status == 'active':
            teachers = Teachers_Task.objects.filter(is_active=True)
        elif status == 'inactive':
            teachers = Teachers_Task.objects.filter(is_active=False)
        else:
            return Response({"error": "Invalid status. Use 'active' or 'inactive'."}, status=400)
        
        serializer = TeacherTaskSerializer(teachers, many=True)
        return Response(serializer.data)
