from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def home(request):
    return HttpResponse('<h1>Welcome to Home</h1>')


def showFormData(request):
    fm = StudentRegistration(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'Your account has been created!')
            messages.info(request, 'Now you can login!')
        else:
            fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})


def student_form(request):
    fm = StudentRegistration(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            fm.save()
            messages.info(request, 'This is a info messages')
            messages.success(request, 'This is a success messages')
            messages.error(request, 'This is a error messages')
        else:
            fm = StudentRegistration()
    return render(request, 'enroll/studentregistration.html', {'form':fm})


def teacher_form(request):
    fm = TeacherRegistration(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            fm.save()
        else:
            fm = TeacherRegistration()
    return render(request, 'enroll/teacherregistration.html', {'form':fm})