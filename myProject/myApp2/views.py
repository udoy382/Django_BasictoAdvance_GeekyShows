from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django2(request):
    # return HttpResponse('<h1>Hello Django learn_Django2</h1>')

    return render(request, 'myApp2/myapp2-home.html')