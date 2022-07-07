from django.shortcuts import render, HttpResponse
from mysignal import signals

# Create your views here.



def home(request):
    signals.notification.send(sender=None, request=request, user=['Programmer', 'Udoy'])
    return HttpResponse('<h1>Welcome to Home</h1>')