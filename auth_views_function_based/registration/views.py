from urllib import request
from django.shortcuts import render

# Create your views here.


def profile(reqeust):
    return render(request, 'registration/profile.html')

