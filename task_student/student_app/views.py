from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
from django.db.models import Q
from django.http import Http404 




# Create your views here.



from .models import Student_Task
from .serializers import StudentTaskSerializer
from utils.utils import format_students_data,calculate_average, group_students_by_teacher, filter_failed_students



class Crud_All_Student(APIView):

    def post(self, request):
        '''
        Handle the POST request to create new student tasks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/add/
        '''
        # Set `many=True` to handle a list of dictionaries (multiple students)
        serializer = StudentTaskSerializer(data=request.data, many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        '''
        Handle the GET request to retrieve all student tasks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/list/
        '''
        # Directly handle GET logic here
        students = Student_Task.objects.all()
        serializer = StudentTaskSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        '''
        Handle the DELETE request to delete all existing student tasks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/delete/
        '''
        # Directly handle DELETE logic here
        Student_Task.objects.all().delete()
        return Response({"success": "All students deleted"}, status=status.HTTP_204_NO_CONTENT)
    


class StudentTaskByRollno(APIView):

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
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/crud/roll_no/
        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
            serializer = StudentTaskSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student_Task.DoesNotExist:
            return Response({"error": "Student task not found."}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, roll_no):
        '''
        Handle the GET request to retrieve a student task by roll number.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/crud/roll_no/
        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
            serializer = StudentTaskSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student_Task.DoesNotExist:
            return Response({"error": "Student task not found."}, status=status.HTTP_404_NOT_FOUND)

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
            # Extract subject name from the URL path
            return self.failed_student(request)
        
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)



    def get_top5_students(self, request):
        '''
            View to list the first 5 top-performing students.
            Use Postman to test this API at the following URL: http://127.0.0.1:8000/toppers/
        '''
    
        try:
            top_students = Student_Task.objects.order_by('-total_marks_field')[:5]

            serialized_data = format_students_data(top_students, title=f"top_5_students")
            return serialized_data 
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def students_with_cutoff(self, request,cutoff=150):
        '''
        View to list students who have scored 150 or more total marks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/cutoff/
        '''
        try:
            # Fetch students with marks greater than or equal to the cutoff
            students = Student_Task.objects.filter(total_marks_field__gte=cutoff)
            
            # Call the utility function to format the data
            formatted_students = format_students_data(students, title=f"students_who_meet_cutoff_{cutoff}")
            
            return formatted_students
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def failed_student(self, request,pass_mark=35):
        '''
        View to list students who have failed in one or more subjects.
        Use Postman to test this API at the following URL: 
        - http://127.0.0.1:8000/failed/chemistry/
        - http://127.0.0.1:8000/failed/physics/
        - http://127.0.0.1:8000/failed/maths/
        '''
        try:
            student= Student_Task.objects.filter(Q(chemistry__lt=pass_mark) | Q(physics__lt=pass_mark) | Q(maths__lt=pass_mark))
            serialized_data = format_students_data(student, title=f"students_who_failed_lessthan_{pass_mark}")
            return serialized_data
        except Exception as e:
            # Log the error (you might want to use a logging framework)
            print(f"Error occurred: {str(e)}")  # Replace with actual logging
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class StudentAvg(APIView):
    def get(self, request):
        '''
        View to list students based on the requested action.
        Use Postman to test this API at the following URLs:
        - http://127.0.0.1:8000/avg/
        - http://127.0.0.1:8000/subject_failed/
        - http://127.0.0.1:8000/teacher/
        - http://127.0.0.1:8000/performance/
        '''
        if request.path == '/avg/':
            return self.student_less_greater_avg(request)
        elif request.path == '/subject_failed/':
            return self.subject_wise_failed_student(request)
        elif request.path == '/teacher/':
            return self.students_by_teacher(request)
        elif request.path == '/perfomance/':
            return self.performance_of_teacher(request)

        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)
    
    def student_less_greater_avg(self, request):
        '''View to calculate students with less than and greater than average.'''
        try:
            students = Student_Task.objects.all()
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
    
    def subject_wise_failed_student(self, request):
        '''View to list students who failed in subjects.'''
        try:
            students = Student_Task.objects.all()
            failed_students = {
                "chemistry_failed": filter_failed_students(students, 'chemistry'),
                "physics_failed": filter_failed_students(students, 'physics'),
                "maths_failed": filter_failed_students(students, 'maths')
            }

            serialized_data = {key: StudentTaskSerializer(value, many=True).data for key, value in failed_students.items()}
            return Response(serialized_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def students_by_teacher(self, request):
        '''View to list students by teacher.'''
        try:
            students = Student_Task.objects.all()
            grouped_students = group_students_by_teacher(students)

            response_data = []
            for teacher, students in grouped_students.items():
                serialize = StudentTaskSerializer(students, many=True)
                response_data.append({
                    "class_teacher": teacher,
                    "students": serialize.data
                })

            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




    def performance_of_teacher(self, request):
        '''
        View to get the performance of teachers based on average marks scored by students.
        '''
        try:
            students = Student_Task.objects.all()
            grouped_students = group_students_by_teacher(students)
            teacher_performance = []
            total_marks_possible = 300
            for teacher, students in grouped_students.items():
                average_marks = calculate_average(students) 

                # Calculate performance percentage based on average marks
                performance_percentage = (average_marks / total_marks_possible) * 100 if total_marks_possible > 0 else 0

                teacher_performance.append({
                    "class_teacher": teacher,
                    "average_marks": average_marks,
                    "performance_percentage": performance_percentage,
                })

            # Sort teachers by average marks in descending order
            teacher_performance.sort(key=lambda x: x['average_marks'], reverse=True)

            # Separate the first performer teacher
            first_performer = teacher_performance[0] if teacher_performance else None
            other_teachers = teacher_performance[1:] if len(teacher_performance) > 1 else []

            # Prepare the final response data
            response_data = {
                "first_performer": first_performer,
                "other_teachers": other_teachers,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        