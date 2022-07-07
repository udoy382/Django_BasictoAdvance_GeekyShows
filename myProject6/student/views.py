from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.


# **************** Django Cookies Code *******************

# -------Method-1 to set cookies---------
"""
def set_cookie(request):
    response =  render(request, 'student/setcookie.html')
    # response.set_cookie('name', 'udoy', max_age=60)
    response.set_cookie('name', 'udoy',expires=datetime.utcnow()+timedelta(days=2))
    return response
"""

# -------Method-2 to set cookies---------
def set_cookie(request):
    response =  render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'udoy', salt='nm', expires=datetime.utcnow()+timedelta(days=2))

    request.session.set_expiry(0)
    return response

# -------Method-1 to get cookies---------
"""
def get_cookie(request):
    # method-1
    # name = request.COOKIES['name']

    # method-2
    # name = request.COOKIES.get('name')
    name = request.COOKIES.get('name', 'Guest')

    return render(request, 'student/getcookie.html', {'name':name})
"""

# -------Method-2 to get cookies---------
def get_cookie(request):
    name = request.get_signed_cookie('name', default='Guest', salt='nm')
    return render(request, 'student/getcookie.html', {'name':name})


def delete_cookie(request):
    response =  render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response



# ************* Django Session Code **************


def set_session(request):
    request.session['name'] = 'Udoy'
    # request.session.set_expiry(5)
    return render(request, 'student/setsession.html')


def get_session(request):
    # name = request.session['name'] = 'Udoy'
    nickname = request.session.get('nickname')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age', '26')

    if 'name' in request.session:
        name = request.session.get('name')
        request.session.modified = True
        return render(request, 'student/getsession.html', {'name':name, 'nickname':nickname, 'keys':keys, 'items':items, 'age':age})
    else:
        return HttpResponse('Your Session has expired...')


"""
def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')
"""

# ---------------Delete Full Sessins Key------------------
def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')

# Test Cookies

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    request.session.test_cookie_worked()
    return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')