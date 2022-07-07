from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.


def home(request):
    print('I am view!!')
    return HttpResponse('This is HOME page')


def excp(request):
    print('I am Exception View!!')
    a = 10/0
    return HttpResponse('This is Exception Page!!')


def user_info(request):
    print('I am Use Info View!!')
    context = {'name':'Udoy'}
    return TemplateResponse(request, 'blog/user.html', context)