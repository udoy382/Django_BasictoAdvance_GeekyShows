from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm

# Create your views here.

# ****--------------Function Based View--------------****

def myview(request):
    return HttpResponse('<h1>Function Based View</h1>')


# ----------Template rendering with function based view--------------

def home(request):
    return render(request, 'school/home.html')

# -----------Pass context in templates with function based view------------

def about(request):
    context = {'msg':'Welcome to Function Based view'}
    return render(request, 'school/about.html', context)


# ------------Use forms with function based view--------------

def contactfun(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you! Form submited ( Funciton Based View)')
    
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form':form})


def newsfun(request):
    context = {'info':'Saifur Rahman Udoy is a programmer!!'}

    return render(request, 'school/news.html', context)

# ****----------------Class Based View----------------****


class MyView(View):
    name = 'Saifur Rahman Udoy'
    def get(self, request):
        # return HttpResponse('<h1>Class Based View</h1>')
        return HttpResponse(self.name)


class MyViewChild(MyView):
    def get(self,request):
        return HttpResponse(self.name)


# ----------Template rendering with class based view--------------

class HomeClassview(View):
    def get(self, request):
        return render(request, 'school/clshome.html')

# -----------Pass context in templates with class based view------------

class AboutClassView(View):
    def get(self, request):
        context = {'msg':'Welcome to Class Based view'}
        return render(request, 'school/clsabout.html', context)


# ------------Use forms with class based view--------------


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/clscontact.html', {'form':form})

    def post(self, request):
        form =ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you! Form submited ( Class Based View )')
