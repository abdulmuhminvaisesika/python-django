from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teachers_Task
from teacher_app.serializers import TeacherTaskSerializer 
from utils.utils import calculate_performance
from student_app.models import Student_Task
# Create your views here.



class TeacherCrudOperations(APIView):
    def get(self, request, employee_id=None):
        if employee_id is not None:
            try:
                teacher = Teachers_Task.objects.get(employee_id=employee_id)
                serializer = TeacherTaskSerializer(teacher)
                return Response(serializer.data)
            except Teachers_Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
            # If no teacher_id key, return all teachers
        else:
            teachers = Teachers_Task.objects.all()
            serializer = TeacherTaskSerializer(teachers, many=True)
            return Response(serializer.data)

    def post(self, request):
        try:
            serializer = TeacherTaskSerializer(data=request.data, many=True)
            if serializer.is_valid():
                teachers = serializer.save()
                
                for teacher in teachers:
                    if teacher.employee_id:
                        students = Student_Task.objects.filter(teacher_id=teacher.employee_id)
                        
                        performance = calculate_performance(students)
                        
                        teacher.performance = performance
                        teacher.save()
                        
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Handle unexpected exceptions
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, employee_id=None):
        try:
            teacher = Teachers_Task.objects.get(employee_id=employee_id)
        except Teachers_Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherTaskSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id=None):
        try:
            if employee_id is not None:
                # Delete a specific teacher by employee_id
                teacher = Teachers_Task.objects.get(employee_id=employee_id)
                teacher.delete()
                return Response({"success": f"Teacher with employee ID {employee_id} deleted."}, status=status.HTTP_204_NO_CONTENT)
            else:
                # Delete all teachers
                Teachers_Task.objects.all().delete()
                return Response({"success": "All teachers deleted."}, status=status.HTTP_204_NO_CONTENT)

        except Teachers_Task.DoesNotExist:
            return Response({"error": "Teacher with employee ID not found."}, status=status.HTTP_404_NOT_FOUND) 