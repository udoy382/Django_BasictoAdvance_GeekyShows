from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    a = 10/0
    return HttpResponse('Hello')


def main_home(request):
    return HttpResponse('<h1>Hello! Welcome to Home</h1> <br> <h3>Learn Signal... </h3>')