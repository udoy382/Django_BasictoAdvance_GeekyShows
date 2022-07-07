from django.shortcuts import render
from .models import Student, ProxyStudent

# Create your views here.

def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.students.all()

    # student_data = Student.students.get_stu_roll_range(1, 3)

    student_data = ProxyStudent.students.get_stu_roll_range(1, 3)

    return render(request, 'school/home.html', {'students':student_data})

