from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EditAdminProfileForm, SignUpForm, EditUserProfileForm

# Create your views here.


def sign_up(request):
    user_form = SignUpForm(request.POST)
    if request.method == "POST":
        if user_form.is_valid():
            user_form.save()
        else:
            user_form = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':user_form})


def user_login(request):
    fm = AuthenticationForm(request=request, data=request.POST)
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Logged in successfully {username}!! ')
                    return HttpResponseRedirect('/profile/')
                else:
                    return redirect('/login')
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
        if request.user.is_superuser == True:
            fm = EditAdminProfileForm(instance=request.user)
        else:
            fm = EditUserProfileForm(instance=request.user)

        return render(request, 'enroll/profile.html', {'name':request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def forgot_pass(request):
    if not request.user.is_authenticated:
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if request.method == 'POST':
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/profile/')
            else:
                fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/forgot.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')