from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app1/index.html', {'name':'Saifur Rahman Udoy'})


def staticsite(request):
    return render(request, 'app1/staticsite.html', {'name':'Udoy', 'age':16, 'gread':'10th'})


def another_static(request):
    Info = [
        {
            'name':'Saifur Rahman Udoy',
            'age':16,
            'country':'Bangladesh'
        }
    ]
    return render(request, 'app1/staticsite2.html', {'info':Info})