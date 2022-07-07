from distutils import core
from turtle import clear
import django
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.

# Cache in each page with using cache_page

"""
@cache_page(30)
def home(request):
    return render(request, 'djcache/course.html')
"""

# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'The One', 30)
#         mv = cache.get('movie')
#     return render(request, 'djcache/course.html', {'fm':mv})


# def home(request):
#     mv = cache.get_or_set('fees', 4000, 30)
#     return render(request, 'djcache/course.html', {'fm':mv})


# def home(request):
#     data = {'name':'Udoy', 'roll':10}
#     cache.set_many(data, 30)
#     mv = cache.get_many(data)
#     return render(request, 'djcache/course.html', {'fm':mv})


# def home(request):
#     cache.delete('roll')
#     return render(request, 'djcache/course.html')     # Not Working

def home(request):
    cache.clear()
    return render(request, 'djcache/course.html')       # Not Working

        # Clear all data in database using command line cause function does not work,
        # >>> python manage.py shell
        # >>> from django.core.cache import cache
        # >>> cache.clear()

def contact(request):
    return render(request, 'djcache/contact.html')


def cache_tamplates(request):
    return render(request, 'djcache/cache.html')