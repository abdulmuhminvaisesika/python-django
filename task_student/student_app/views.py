from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict


# Create your views here.



from .models import Student_Task
from .serializers import StudentTaskSerializer


class StudentAdd(APIView):
    def post(self,request):
        '''
            Handle the POST request to create a new student task.
            Use Postman to test this API at the following URL:http://127.0.0.1:8000/add/


        '''
        serialize=StudentTaskSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        '''
            Handle the GET request to retrieve all student tasks.
            Use Postman to test this API at the following URL:http://127.0.0.1:8000/list/

        '''
        student=Student_Task.objects.all()
        serialize=StudentTaskSerializer(student, many=True)
        return Response(serialize.data,status=status.HTTP_200_OK)
    
    def put(self, request, roll_no):
        '''
            Handle the PUT request to update an existing student task.
            Use Postman to test this API at the following URL:http://127.0.0.1:8000/update/roll_no/

        '''
        
        student=Student_Task.objects.get(roll_no=roll_no)
        serialize=StudentTaskSerializer(student, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, roll_no):
        '''
            Handle the DELETE request to delete an existing student task.
            Use Postman to test this API at the following URL:http://127.0.0.1:8000/delete/roll_no/

        '''
        try:
            student = Student_Task.objects.get(roll_no=roll_no)
        
            student.delete()
        
            return Response({"sucess":"deleted"}, status=status.HTTP_204_NO_CONTENT)
    
        except Student_Task.DoesNotExist:
            return Response({"error": "Student task not found."}, status=status.HTTP_404_NOT_FOUND)
    

    

class StudentTopper(APIView):
    def get(self, request):
        '''
        View to list students based on the requested action.
        Use Postman to test this API at the following URLs:
        - http://127.0.0.1:8000/toppers/
        - http://127.0.0.1:8000/cutoff/
        '''
        if request.path == '/toppers/':
            return self.get_top_students(request)
        elif request.path == '/cutoff/':
            return self.students_with_cutoff(request)
        elif request.path == '/failed/':
            return self.failed_student(request)
        
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)
    



    def get_top_students(self, request):
        '''
        View to list first 5 top-performing students.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/toppers/
        '''

        try:
            students = Student_Task.objects.all()
            topers = sorted(students, key=lambda student: student.total_marks(), reverse=True)[:5]

            
            serialize = StudentTaskSerializer(topers, many=True)

            return Response(serialize.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def students_with_cutoff(self, request):
        '''
        View to list students who have scored 150 or more total marks.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/cutoff/
        '''
        try:
            cutoff = 150
            students = Student_Task.objects.all()
            students_reach_cutoff = [student for student in students if student.total_marks() >= cutoff]

            serialize = StudentTaskSerializer(students_reach_cutoff, many=True)

            return Response(serialize.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def failed_student(self,request):
        '''
        View to list students who have failed in one or more subjects.
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/failed/
        '''
        try:
            students= Student_Task.objects.all()
            student_failed= [ student for student in students if student.chemistry<35 or student.physics<35 or student.maths<35]
            serilize=StudentTaskSerializer(student_failed, many=True)
            return Response(serilize.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StudentAvg(APIView):
    def get(self,request):

        if request.path == '/avg/':
            return self.student_less_geater_avg(request)
        elif request.path == '/subject_failed/':
            return self.subject_wise_failed_student(request)
        elif request.path == '/teacher/':
            return self.students_by_teacher(request)
        elif request.path == '/perfomance/':
            return self.perfromace_of_teacher(request)
        
        
        return Response({"error": "Invalid endpoint"}, status=status.HTTP_404_NOT_FOUND)
    
    def student_less_geater_avg(self, request):
        '''
        View to calculate students with less then average and greater than average
        Use Postman to test this API at the following URL: http://127.0.0.1:8000/avg/
        '''

        try:
            
            students = Student_Task.objects.all()
            total_students = students.count()
            total_marks_sum = sum(student.total_marks() for student in students)
            average_marks = total_marks_sum / total_students

            less_than_avg = [student for student in students if student.total_marks() < average_marks]
            greater_than_avg = [student for student in students if student.total_marks() > average_marks]

            less_serialize = StudentTaskSerializer(less_than_avg, many=True)
            greater_serialize = StudentTaskSerializer(greater_than_avg, many=True)

            return Response({
                "less_than_average": less_serialize.data,
                "greater_than_average": greater_serialize.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


    def subject_wise_failed_student(self,request):
        '''
        view to list student who failed in subjects
        Use Postman to test this API at the following URL:http://127.0.0.1:8000/subject_failed/
        '''
        try:
            students=Student_Task.objects.all()
            chem_failed=[student for student in students if student.chemistry<35]
            phy_failed=[student for student in students if student.physics<35]
            math_failed=[student for student in students if student.maths<35]
            serialize_chem=StudentTaskSerializer(chem_failed, many=True)
            serialize_phy=StudentTaskSerializer(phy_failed, many=True)
            serialize_math=StudentTaskSerializer(math_failed, many=True)
            return Response({
                "chemistry_failed":serialize_chem.data,
                "physics_failed":serialize_phy.data,
                "maths_failed":serialize_math.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def students_by_teacher(self, request):
        '''
        view to list students by teacher
        Use Postman to test this API at the following URL:http://127.0.0.1:8000/teacher/
        '''
        try:
            students = Student_Task.objects.all()
            
            grouped_students = defaultdict(list)
            
            for student in students:
                grouped_students[student.class_teacher].append(student)
            
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

    def perfromace_of_teacher(self,request):
        '''
        view to get the performance of teachers  in percentage according to total students and passed students scored by students
        Use Postman to test this API at the following URL:
        '''
        try:
            students = Student_Task.objects.all()

            grouped_students = defaultdict(list)

            for student in students:
                grouped_students[student.class_teacher].append(student)

            response_data = []
            for teacher, students in grouped_students.items():
                total_students = len(students)
                total_mark_avg = (sum(student.total_marks() for student in students) / (total_students * 300)) * 100 if total_students > 0 else 0
                passed_students = sum(1 for student in students if student.total_marks() >= 35)
                failed_students = sum(1 for student in students if student.total_marks() < 35)
                pass_percentage = (passed_students / total_students) * 100
                fail_percentage = (failed_students / total_students) * 100

                response_data.append({
                    "class_teacher": teacher,
                    "pass_percentage": pass_percentage,
                    "fail_percentage": fail_percentage,
                    "average_of_tatal_mark":total_mark_avg
                })

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
            



        