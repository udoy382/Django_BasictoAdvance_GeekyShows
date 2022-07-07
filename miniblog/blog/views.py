from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm, LoginForm, PostForm
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.


def home(reqest):
    posts = Post.objects.all()
    return render(reqest, 'blog/home.html', {'posts':posts})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':gps})
    else:
        return redirect('/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have become an Author.')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        form = LoginForm(request = request, data = request.POST)
        if request.method == 'POST':
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                
                user = authenticate(username=uname, password=upass)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return redirect('/dashboard')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return redirect('/dashboard')

def addpost(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
    else:
        return redirect('/login')
    return render(request, 'blog/addpost.html', {'form':form})

def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return redirect('/login')


def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return redirect('/dashboard/')
    else:
        return redirect('/login')