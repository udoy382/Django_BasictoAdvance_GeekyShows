from django.shortcuts import render
from .models import Student, Teacher

# Create your views here.

'''
def home(request):
    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=333) # Print only this marks data

    # student_data = Student.objects.exclude(marks=333) # Print all data without this marks

    # student_data = Student.objects.order_by('city') # order by A to Z
    # student_data = Student.objects.order_by('-city') # order by A to Z with negetive formet

    # student_data = Student.objects.order_by('id').reverse()[:3] # reverce items with order by

    # student_data = Student.objects.values('name', 'city') # show specific objects like name and city show here only
    
    # student_data = Student.objects.values_list('id', 'name', named=True) # come data with tuple formet

    # student_data = Student.objects.using('default') # show database name default

    # student_data = Student.objects.dates('pass_date', 'year') # show this data with tuple formet this way do not show thsi data in browser only show in terminal [ we user := dates, month, year]

    # ***********Secend Table Start Here*********************

    """
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)

    student_data = qs2.union(qs1)
    student_data = qs2.intersection(qs1)
    """

    # -----------------------

    """
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)

    student_data = qs2.difference(qs1)
    """

    # student_data = Student.objects.filter(id=5) and Student.objects.filter(roll=101) # show data if both are true
    student_data = Student.objects.filter(id=3) or Student.objects.filter(roll=101) # show data if both are true

    return render(request, 'school/home.html', {'students':student_data})
'''

#*** _________________________________ QuerySet API Methods that do not return new QuerySet [ QuerySet Second video ] __________________________***


def home2(request):
    # student_data = Student.objects.get(id=1)

    # student_data = Student.objects.first()

    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.order_by('name').last()

    # student_data = Student.objects.latest('pass_date')

    # student_data = Student.objects.earliest('pass_date')

    '''
    student_data = Student.objects.all()
    print(student_data.exists())
    '''

    '''
    student_data = Student.objects.all()
    one_data = Student.objects.get(pk=1)
    print(student_data.filter(pk=one_data.pk).exists())
    '''

    # student_data =  Student.objects.create(name='Samer', roll=46, city='New York', marks=550, pass_date = '2022-3-22')

    # student_data =  Student.objects.get_or_create(name='Samer', roll=46, city='New York', marks=550, pass_date = '2022-3-22')
    # return render(request, 'school/home2.html', {'student':student_data})
    pass


def home3(request):
    # student_data =  Student.objects.filter(marks=550).update(city='pass')
    # student_data = Student.objects.update_or_create(id=99, name='Mitu', defaults={'name':'Kohli'})

    # ------------- Create to many data in this way -------------
    """
    objs = [
        Student(name='Atif', roll=116, city='Dhanbad', marks=70, pass_date='2022-5-4'),
        Student(name='Mitu', roll=117, city='Nouakali', marks=80, pass_date='2022-5-5'),
        Student(name='Saifur', roll=118, city='stylet', marks=90, pass_date='2022-5-6'),
        Student(name='Rahman', roll=119, city='Cox Bazar', marks=100, pass_date='2022-5-7'),
    ]

    # student_data = Student.objects.bulk_create(objs)
    
    # ----------update bulk data------------
    all_student_data = Student.objects.all()
    for stu in all_student_data:
        stu.city = 'Bhel'
    
    student_data = Student.objects.bulk_update(all_student_data, ['city'])
    """


    # return render(request, 'school/home3.html', {'student':student_data})
    pass