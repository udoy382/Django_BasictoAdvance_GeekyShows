from django.shortcuts import render, HttpResponse
from .models import Student
from datetime import date, time
from django.db.models import Avg, Sum, Min, Max, Count, Q

# Create your views here.

"""
def home(request):
    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(name__exact='Udoy')
    # student_data = Student.objects.filter(name__iexact='udoy') # { case sencetive}

    # student_data = Student.objects.filter(name__contains='F') # Return all data whcih start with F or given first char...
    # student_data = Student.objects.filter(name__icontains='f') # Return all data whcih start wih F or given first char... { case sencetive}

    # student_data = Student.objects.filter(id__in = [1, 3]) # Returns all data form this ideq
    # student_data = Student.objects.filter(marks__in = [400, 800]) # Returns all data form this marks

    # student_data = Student.objects.filter(marks__gt = 400) # Returns all data greater then 400
    # student_data = Student.objects.filter(marks__gte = 400) # Returns all data greater then and uel 120

    # student_data = Student.objects.filter(marks__lt = 400) # Returns all data less then 400
    # student_data = Student.objects.filter(marks__lte = 400) # Returns all data less then and uel 120

    # student_data = Student.objects.filter(name__startswith='m')
    # student_data = Student.objects.filter(name__istartswith='m')

    # student_data = Student.objects.filter(name__endswith='y')
    # student_data = Student.objects.filter(name__iendswith='y')

    # student_data = Student.objects.filter(passdate__range = ('2022-03-01', '2022-03-29')) # returns all data, bettern this date

    # student_data = Student.objects.filter(passdate__year=2021) we used [ month, day etc]
    # student_data = Student.objects.filter(passdate__year__gte=2021)

    # student_data = Student.objects.filter(passdate__quarter=1) # [ 1 = Jan, Fev, Mar ... 2 = Apr, May, Jun ... 3 = Jul, Aug, Sep ect.]

    # student_data = Student.objects.filter(admdatetime__time__gt=time(21,17))
    # student_data = Student.objects.filter(admdatetime__hour__gt=5)
    # student_data = Student.objects.filter(admdatetime__minute__gt=20)
    # student_data = Student.objects.filter(admdatetime__second__gt=20)

    student_data = Student.objects.filter(roll__isnull=False)


    print('Return: ', student_data)
    print('SQL Qery: ', student_data.query)
    return render(request, 'lookups/home.html', {'students':student_data}) 
"""


def home(request):
    # student_data = Student.objects.all()
    # average = student_data.aggregate(Avg('marks'))
    # sum = student_data.aggregate(Sum('marks'))
    # min = student_data.aggregate(Min('marks'))
    # max = student_data.aggregate(Max('marks'))
    # count = student_data.aggregate(Count('marks'))

    # print('Average: ', average)
    # print('Sum: ', sum)
    # print('Min: ', min)
    # print('Max: ', max)
    # print('Count: ', count)
    # print('Return: ', student_data)
    # print('SQL Qery: ', student_data.query)
    # return render(request, 'lookups/home.html', {'average':average, 'sum':sum, 'min':min, 'max':max, 'count':count})

    # --------------------------

    # student_data = Student.objects.filter(Q(id=3) & Q(roll=3))
    # student_data = Student.objects.filter(Q(id=3) | Q(roll=2))
    student_data = Student.objects.filter(~Q(id=5))


    print(student_data)
    return render(request, 'lookups/home.html', {'students':student_data})