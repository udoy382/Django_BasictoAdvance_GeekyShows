from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

''' 
def index(request):
    return HttpResponse('<h1>This is a Home page</h1>')

def learn_django(request):
    return HttpResponse('<h1>Hello World This is a myProject</h1>')


def my_math(request):
    a = 10
    b = 20
    c = a + b
    return HttpResponse(f'10 + 20 = {c}')
'''



def home(request):
    udoy =[
        {
        'name':'Saifur Rahman Udoy',
        'age':16,
        'phone_number':'01782299436',
        'address':'Sylhet Habiganj Bangladesh',
    },
        {
        'name':'Mariyam',
        'age':16,
        'phone_number':'565645466',
        'address':'America',
    }
]

    return render(request, 'myApp/home.html', {'context':udoy})


"""
def templ(request):
    name = 'Django'
    duration = '4 Months'
    seats = 10
    django_details = {'nm':name, 'du':duration, 'st':seats}

    # return render(request, 'myApp/templ.html', {'nm':'Django'})
    return render(request, 'myApp/templ.html', django_details)
"""

"""
def templ(request):
    django_details = {'nm':'saifur Rahman UDOY is a vary good boy'}
    return render(request, 'myApp/templ.html', django_details)
"""

"""
def templ(request):
    d = datetime.now()
    return render(request, 'myApp/templ.html', {'dt':d})
"""


"""
def templ(request):
    s_list = ['Udoy', 'Mariyam', 'Akhi', 'Fariha', 'Mahima', 'Jarien', 'Mitu']

    student = {'names':s_list}

    # return render(request, 'myApp/templ.html', {'nm':True, 'n':'Django', 'st':5})
    return render(request, 'myApp/templ.html', student)
"""


def templ(request):
    stu = {
        'student1':{'name':'Udoy', 'rool':101},
        'student2':{'name':'Mariyam', 'rool':102},
        'student3':{'name':'Akhi', 'rool':103},
        'student4':{'name':'Mitu', 'rool':104},
    }

    students = {'student':stu}
    return render(request, 'myApp/templ.html', students)


"""
def templ(request):
    data = {'name':'Saifur Rahman Udoy', 'rool':10}
    return render(request, 'myApp/templ.html', {'data':data})
"""