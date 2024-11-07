#Django Imports
from django.db.models import Q

#Rest Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Local Imports
from .models import Student_Task
from .serializers import StudentTaskSerializer


from utils.utils import calculate_average



class Crud_All_Student(APIView):
    def get(self, request, roll_no=None):
        '''
        Handle the GET request to retrieve all students and a student by roll number.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/roll_no/

        '''
        try:
            #get student by iD
            if roll_no:
                try:
                    student = Student_Task.objects.get(roll_no=roll_no)
                    serializer = StudentTaskSerializer(student)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Student_Task.DoesNotExist:
                    return Response({"error": "Student with the specific id not found"}, status=status.HTTP_400_BAD_REQUEST)
            
            #get all students 
            student =Student_Task.objects.all()
            serializer = StudentTaskSerializer(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    
    def post(self, request):
        try:
            # Create a new student task
            serializer = StudentTaskSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()  # Save the new student
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



    def put(self, request, roll_no):
        '''
        Handle the PUT request to update an existing student task.
        Updates the student's data and recalculates the teacher's performance.
        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
            serializer = StudentTaskSerializer(student, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()  # Save the updated student
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Student_Task.DoesNotExist:
            return Response({"error": "Student with the specified roll number not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentTopper(APIView):
    def get(self, request):
        '''
        View to list students based on the requested action.
        Use Postman to test this API at the following URLs:
        - http://127.0.0.1:8000/students/toppers/
        - http://127.0.0.1:8000/students/cutoff/
        - http://127.0.0.1:8000/students/failed/
        '''
        if request.path.endswith('/toppers/'):
            return self.get_top5_students()
        elif request.path.endswith('/cutoff/'):
            return self.students_with_cutoff()
        elif request.path.endswith('/failed/'):
            return self.failed_student()
        
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)


    def get_top5_students(self):
        '''
        View to list the first 5 top-performing students based on total marks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/toppers/
        '''
    
        try:
            # Retrieve the top 5 students ordered by total marks in descending order
            top_students = Student_Task.objects.order_by('-total_marks_field')[:5]            
            serializer = StudentTaskSerializer(top_students, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def students_with_cutoff(self, cutoff=150):
        '''
        View to list students who have scored at least the specified cutoff(150) total marks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/cutoff/
        '''
        try:
            # Fetch students with total marks greater than or equal to the cutoff
            students = Student_Task.objects.filter(total_marks_field__gte=cutoff)            
            serializer = StudentTaskSerializer(students, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def failed_student(self,pass_mark=80):     
        '''
        View to list students who have failed.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/failed/
        '''
        
        try:
            #filter only students totalmark lessthan passmark(80)
            student= Student_Task.objects.filter(total_marks_field__lt=pass_mark)

            serilize = StudentTaskSerializer(student, many=True)
            return Response({"student_who_failed":serilize.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class StudentAvg(APIView):
    def get(self, request):
        if 'avg' in request.path:
            return self.student_less_greater_avg()
        
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)
    def student_less_greater_avg(self):
        '''
        View to calculate students with less than and greater than average.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/avg/
        '''
        try:
            students = Student_Task.objects.all()

            #calculating average using calculate_average() function from utils.py
            average_marks = calculate_average(students)

            less_than_avg = [student for student in students if student.total_marks_field < average_marks]
            greater_than_avg = [student for student in students if student.total_marks_field > average_marks]

            less_serialize = StudentTaskSerializer(less_than_avg, many=True)
            greater_serialize = StudentTaskSerializer(greater_than_avg, many=True)

            return Response({
                "less_than_average": less_serialize.data,
                "greater_than_average": greater_serialize.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
       
class StudentStatusView(APIView):
    def get(self, request, status):
        if status == 'active':
            students = Student_Task.objects.filter(is_active=True)
        elif status == 'inactive':
            students = Student_Task.objects.filter(is_active=False)
        else:
            return Response({"error": "Invalid status. Use 'active' or 'inactive'."}, status=400)
        
        serializer = StudentTaskSerializer(students, many=True)
        return Response(serializer.data)