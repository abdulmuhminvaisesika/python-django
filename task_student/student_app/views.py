from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
from django.db.models import Q
from django.http import Http404 




# Create your views here.



from .models import Student_Task,Teacher_Task
from .serializers import StudentTaskSerializer, TeacherTaskSerializer
from utils.utils import calculate_average, calculate_performance



class Crud_All_Student(APIView):

    def post(self, request):
        '''
        Handle the POST request to create new student tasks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/crud/
        '''
        try:
            serializer = StudentTaskSerializer(data=request.data, many=True)

            if serializer.is_valid():
                students = serializer.save()  
                
                # After saving students, calculate and update teacher performance
                for student in students:
                    if student.teacher_id:  # Check if teacher_id is set
                        # Calculate the performance based on the updated student records
                        performance = calculate_performance(Student_Task.objects.filter(teacher_id=student.teacher_id))

                        # Update the teacher's performance directly
                        Teacher_Task.objects.filter(employee_id=student.teacher_id.employee_id).update(perfomance=performance)

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        '''
        Handle the GET request to retrieve all student tasks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/crud/
        '''
        try:
            students = Student_Task.objects.all()
            serializer = StudentTaskSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        '''
        Handle the DELETE request to delete all existing student tasks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/crud/
        '''
        try:
            students = Student_Task.objects.all()
            students.delete()
            return Response({"success": "All students deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    


class StudentTaskByRollno(APIView):
    
    def get(self, request, roll_no):
        '''
        Handle the GET request to retrieve a student by roll number.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/crud/roll_no/
        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
            serializer = StudentTaskSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student_Task.DoesNotExist:
            return Response({"error": "Student task not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, roll_no):
        '''
        Handle the DELETE request to delete an existing student task.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/crud/roll_no/
        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
            student.delete()
            return Response({"success": f"Student with roll no {roll_no} deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Student_Task.DoesNotExist:
            return Response({"error": "Student task not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, roll_no):
        '''
        Handle the PUT request to update an existing student task.
        Updates the student's data and recalculates the teacher's performance.
        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
            serializer = StudentTaskSerializer(student, data=request.data)

            if serializer.is_valid():
                updated_student = serializer.save()

                if updated_student.teacher_id:
                    # Recalculate the teacher's performance based on the updated student
                    performance = calculate_performance(Student_Task.objects.filter(teacher_id=updated_student.teacher_id))
                    Teacher_Task.objects.filter(employee_id=updated_student.teacher_id.employee_id).update(perfomance=performance)


                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student_Task.DoesNotExist:
            return Response({"error": "Student task not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StudentTopper(APIView):
    def get(self, request):
        '''
        View to list students based on the requested action.
        Use Postman to test this API at the following URLs:
        - http://127.0.0.1:8000/toppers/
        - http://127.0.0.1:8000/cutoff/
        - http://127.0.0.1:8000/failed/
        '''
        if request.path == '/toppers/':
            return self.get_top5_students(request)
        elif request.path == '/cutoff/':
            return self.students_with_cutoff(request)
        elif request.path == '/failed/':
            return self.failed_student(request)
        
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)



    def get_top5_students(self, request):
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
        

    def students_with_cutoff(self, request, cutoff=150):
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


    def failed_student(self, request,pass_mark=35):     
        '''
        View to list students who have failed.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/failed/
        '''
        
        try:
            student= Student_Task.objects.filter(Q(chemistry__lt=pass_mark) | Q(physics__lt=pass_mark) | Q(maths__lt=pass_mark))
            serilize = StudentTaskSerializer(student, many=True)
            return Response({"student_who_failed":serilize.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class StudentAvg(APIView):
    def get(self, request,teacher_id=not None):
        '''
        Use Postman to test this API at the following URLs:
        - http://127.0.0.1:8000/avg/
        - http://127.0.0.1:8000/teacher/teacher_id
        - http://127.0.0.1:8000/performance/employee_id
        '''
        if request.path == '/avg/':
            return self.student_less_greater_avg(request)
        if request.path.startswith('/teacher/'):
            return self.students_by_teacher(request,teacher_id)
        elif request.path.startswith('/perfomance/'):
            return self.performance_of_teacher(request,teacher_id)

        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)
    
    def student_less_greater_avg(self, request):
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
    
       

    def students_by_teacher(self, request, teacher_id):
        '''
        Use Postman to test this API at the following URL:http://127.0.0.1:8000/teacher/teacher_id/
        This function retrieves all students associated with a specific teacher, based on the teacher's ID (employee_id).
        '''
        try:
            
            students = Student_Task.objects.filter(teacher_id=teacher_id)
            serialize = StudentTaskSerializer(students, many=True)

            response_data = {
                "class_teacher_id": teacher_id, 
                "students": serialize.data
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def performance_of_teacher(self, request,teacher_id):
        '''
        View to get the performance of teacher
        Use Postman to test this API at the following URL:http://127.0.0.1:8000/perfomance/employee_id/

        '''
        try:
            teacher =Teacher_Task.objects.filter(employee_id=teacher_id)
            serilize=TeacherTaskSerializer(teacher,many=True)
            return Response(serilize.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        