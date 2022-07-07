from django.shortcuts import render

# Create your views here.


def app2(request):
    return render(request, 'app2/app2.html')


def udoy(request):
    return render(request, 'app2/udoy.html')

def mariyam(request):
    return render(request, 'app2/mariyam.html')

def mitu(request):
    return render(request, 'app2/mitu.html')