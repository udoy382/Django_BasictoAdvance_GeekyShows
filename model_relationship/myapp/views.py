from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'myapp/home.html')


def page(request):
    return render(request, 'myapp/page.html')

def post(request):
    return render(request, 'myapp/post.html')

def song(request):
    return render(request, 'myapp/song.html')

def user(request):
    return render(request, 'myapp/user.html')