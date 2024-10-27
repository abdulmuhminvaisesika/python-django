from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department_Task
from .serializers import DepartmentTaskSerializer 


# Create your views here.

class DepartmentCrudOperations(APIView):
    def get(self, request, department_ID=None):
        if department_ID:  # If a primary key is provided, retrieve a specific department
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
            serializers = []
            for department_data in request.data:
                serializer = DepartmentTaskSerializer(data=department_data)
                if serializer.is_valid():
                    serializer.save()
                    serializers.append(serializer)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, department_ID):
        try:
            department = Department_Task.objects.get(department_ID=department_ID)
        except Department_Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentTaskSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, department_ID=None):
        try:
            department = Department_Task.objects.get(department_ID=department_ID)
            department.delete()
            return Response({"success": "department has been deleted."},status=status.HTTP_204_NO_CONTENT)
        except Department_Task.DoesNotExist:
            return Response({"error": "department not found."},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        