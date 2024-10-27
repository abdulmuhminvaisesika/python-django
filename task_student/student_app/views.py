from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
from django.db.models import Q
from django.http import Http404 




# Create your views here.


from teacher_app.models import Teachers_Task
from .models import Student_Task
from .serializers import StudentTaskSerializer
from teacher_app.serializers import TeacherTaskSerializer
from utils.utils import calculate_average, calculate_performance



class Crud_All_Student(APIView):
    def get(self, request, roll_no=None):
        '''
        Handle the GET request to retrieve all students and a student by roll number.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/roll_no/

        '''
        try:
            if roll_no:
                student = Student_Task.objects.get(roll_no=roll_no)
                serializer = StudentTaskSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                student =Student_Task.objects.all()
                serializer = StudentTaskSerializer(student, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Student_Task.DoesNotExist:
            return Response({"error": "Student task not found."}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        '''
        Handle the POST request to create new student tasks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/
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
                        Teachers_Task.objects.filter(employee_id=student.teacher_id.employee_id).update(performance=performance)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, roll_no):
        '''
        Handle the PUT request to update an existing student task.
        Updates the student's data and recalculates the teacher's performance.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/roll_no/
        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
            serializer = StudentTaskSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request,roll_no=None):
        '''
            Handle the DELETE request to delete students by roll no and delete all student tasks.
            Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/
            Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/roll_no/
        '''
        try:
            if roll_no is not None:
                students = Student_Task.objects.all()
                students.delete()
                return Response({"success": "All students deleted."}, status=status.HTTP_204_NO_CONTENT)
            else:
                students = Student_Task.objects.all()
                students.delete()
                return Response({"success": "All students deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    



    


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
            return self.get_top5_students(request)
        elif request.path.endswith('/cutoff/'):
            return self.students_with_cutoff(request)
        elif request.path.endswith('/failed/'):
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
    def get(self, request, teacher_id=None):
        if 'avg' in request.path:
            return self.student_less_greater_avg(request)
        elif teacher_id:
            if 'teacher' in request.path:
                return self.students_by_teacher(request, teacher_id)
            elif 'performance' in request.path:
                return self.performance_of_teacher(request, teacher_id)
        elif 'performance' in request.path:
            return self.performance_of_teacher(request)  # handles case when teacher_id is not provided

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
        View to get students under a class teacher.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students//teacher/teacher_id
        '''
        try:
            students = Student_Task.objects.filter(teacher_id=teacher_id)
            serialize = StudentTaskSerializer(students, many=True)
            return Response({
                "class_teacher_id": teacher_id,
                "students": serialize.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def performance_of_teacher(self, request, teacher_id=None):
        '''
        View to get teh teacher performance when teacher_id passed otherwise give all teacher perfomance.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/performance/
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/students/performance/teacher_id/

        '''
        try:
            if teacher_id:
                # Fetch performance for the specific teacher with the given teacher_id
                teacher = Teachers_Task.objects.filter(employee_id=teacher_id).first()
                if not teacher:
                    return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
                
                # Serialize the specific teacher
                teacher_serializer = TeacherTaskSerializer(teacher)
                teacher_data = {
                    "performer": teacher_serializer.data["name"],
                    "performance": teacher_serializer.data["performance"]
                }
                return Response({"teacher_performance": teacher_data}, status=status.HTTP_200_OK)
            else:
                # Fetch all teachers and sort by performance in descending order
                teachers = Teachers_Task.objects.all()
                sorted_teachers = sorted(teachers, key=lambda teacher: teacher.performance, reverse=True)

                # Serialize the top performer
                top_performer_serializer = TeacherTaskSerializer(sorted_teachers[0])
                top_performer_data = {
                    "top_performer": top_performer_serializer.data["name"],
                    "performance": top_performer_serializer.data["performance"]
                }

                # Serialize other performers
                other_performers_serializer = TeacherTaskSerializer(sorted_teachers[1:], many=True)
                other_performers_data = [
                    {"performer": teacher["name"], "performance": teacher["performance"]}
                    for teacher in other_performers_serializer.data
                ]

                return Response({
                    "top_performer": top_performer_data,
                    "other_performers": other_performers_data
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)