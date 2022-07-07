from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from enroll.models import Student, User
from .forms import StudentRegistration, Student_forms

# ----------------------------------------
# username = Udoy
# email = srudoy436@gmail.com
# password = udoy2299
# ----------------------------------------

# Create your views here.
def home(request, check):
    print(check)
    return render(request, 'enroll/home.html', {'ch':check})


def studentInfo(request):
    students = Student.objects.all()

    return render(request, 'enroll/studetails.html', {'stu':students})


def showFormData(request):
    # change buildin django form id fild name with [ id_name => some_name ] like this 

    fm = StudentRegistration()
    # fm = StudentRegistration(auto_id='some_%s')
    # fm = StudentRegistration(auto_id=True)
    # fm = StudentRegistration(auto_id='udoy')
    # fm = StudentRegistration(auto_id=False)

    fm = StudentRegistration(initial={'name':'Udoy', 'email':'srudoy@gmail.com'})

    # fm = StudentRegistration(label_suffix='-')

    # ORDERS FORM FILDS IN DJANGO FORM 

    fm.order_fields(field_order=['first_name', 'name', 'email'])

    return render(request, 'enroll/registration.html', {'form':fm})


def forms(request):
    # data = Student_forms()

    if request.method == 'POST':
        # name = request.POST['name']

        data = Student_forms(request.POST)
        if data.is_valid():
            # print(data)
            # print('Valid data: ', data.cleaned_data['name'])

            """
            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            password = data.cleaned_data['password']
            print(name, email, password)
            
            """

            print('Form Validated & Submited Successfully!')

            # print('You Name: ', data.cleaned_data['name'])
            # print('You Email: ', data.cleaned_data['email'])
            # print('You Password: ', data.cleaned_data['password'])
            # print('You re_password: ', data.cleaned_data['re_password'])


            # Make and save data for model and and admin panel


            # ----------get single data with this one line of comment----------
            # pi = User.objects.get()

            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            password = data.cleaned_data['password']
            re_password = data.cleaned_data['re_password']

            print(name, email, password, re_password)

            # all_data = User(id=1, name=name, email=email, password=password, re_password=re_password)
            # all_data.save()

            # From Update in database / admin panel 
            # context = User(id=1, name=name, email=email, password=password, re_password=re_password)
            # context.save()

            # Form Deleted in database / admin panel
            # context = User(id=1)
            context = User(id=3)
            context.delete()

            # print('Agree', data.cleaned_data['agree'])
            # print('Roll', data.cleaned_data['roll'])
            # print('Price', data.cleaned_data['price'])
            # print('Rate', data.cleaned_data['rate'])

            # return render(request, 'enroll/success.html', {'name':name})
            # return HttpResponseRedirect('success/')
    else:
        data = Student_forms()
        print('From Doesn\'t Submited!')

    return render(request, 'enroll/forms.html', {'forms':data})


def thankYou(request):
    return render(request, 'enroll/success.html')


# def showDetails(request, my_id):
#     # print('my_id is: ' + my_id)

#     return render(request, 'enroll/show.html', {'id':my_id})


def showDetails(request, my_id=1):
    # print('my_id is: ' + my_id)

    # if my_id == str(1):
    if my_id == 1:
        student = {'id':my_id, 'name':'Udoy'}
    # elif my_id == str(2):
    elif my_id == 2:
        student = {'id':my_id, 'name':'Mariyam'}
    # elif my_id == str(3):
    elif my_id == 3:
        student = {'id':my_id, 'name':'Fariha'}

    return render(request, 'enroll/show.html', student)

"""
def subDetails(request, my_id, my_sub_id):
    # print('my_id is: ' + my_id)

    # if my_id == str(1):
    if my_id == 1 and my_sub_id == 4:
        student = {'id':my_id, 'name':'Udoy', 'info':'Sub Details'}
    # elif my_id == str(2):
    elif my_id == 2 and my_sub_id == 5:
        student = {'id':my_id, 'name':'Mariyam', 'info':'Sub Details'}
    # elif my_id == str(3):
    elif my_id == 3 and my_sub_id == 6:
        student = {'id':my_id, 'name':'Fariha', 'info':'Sub Details'}

    return render(request, 'enroll/show.html', student)
"""


def details(request, year):
    student = {'yr':year}

    return render(request, 'enroll/show.html',  student)

