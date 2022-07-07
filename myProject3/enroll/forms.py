from cProfile import label
from dataclasses import field
from tkinter import Label, Widget
from django import forms
from django.core import validators
from .models import User


# Custom Validation for name field in form
def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name should not start with s')

class StudentRegistration(forms.Form):
    # name = forms.CharField(help_text='this is a help text')
    # name = forms.CharField(label='Your Name', label_suffix=' ', initial='SR Udoy', required=False, disabled=True, help_text='Limit 70 Char')

    # Widget Field like Form type
    # name = forms.CharField(widget=forms.PasswordInput)
    # name = forms.CharField(widget=forms.Textarea)
    # name = forms.CharField(widget=forms.CheckboxInput)
    # name = forms.CharField(widget=forms.FileInput)
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'ThisIsaClass'}))

    name = forms.CharField(widget=forms.TextInput(attrs={'id':'ThisIsaId'}))

    # name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    key = forms.EmailField(widget=forms.HiddenInput)

    # convert small ( f ) to capital ( F ) and underscore ( _ ) to blank ( )
    first_name = forms.CharField()



class Student_forms(forms.Form):
    # name = forms.CharField(min_length=5, max_length=50, strip=True, empty_value='helloudoy', error_messages={'required':'Enter Your Name'})
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])

    # name = forms.CharField(validators=[starts_with_s])

    name = forms.CharField()
    email = forms.EmailField(min_length=5)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)


    # password = forms.CharField(widget=forms.PasswordInput)
    # agree = forms.BooleanField(label_suffix=' ') # label_suffix is clear any symble or add any symble or set blank or space
    # roll = forms.IntegerField(min_value=5, max_value=40)
    # price = forms.DecimalField(min_value=5, max_value=50, max_digits=4, decimal_places=1)
    # rate = forms.FloatField(min_value=5, max_value=50)
    # comment = forms.SlugField()
    # website = forms.URLField()
    # desc = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))

    # --------------------

    # ----------if i want to make our own validation method-------------

    def clean_name(self):
        user_name = self.cleaned_data['name']

        if len(user_name) < 4:
            raise forms.ValidationError('Enter Your name more than 4 char!')

        return user_name


    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']

        if password != re_password:
            raise forms.ValidationError('Password doesn\'t match')


# Own Validation
"""
    def clean(self):
        cleaned_data = super().clean()
        user_name = self.cleaned_data['name']
        user_email = self.cleaned_data['email']

        if len(user_name) < 4:
            raise forms.ValidationError('Name should be more then or equal 4 char')

        if len(user_email) < 10:
            raise forms.ValidationError('Email should be more then or equal 10 char')
"""


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 're_password']

        # --------------doesn't work this line of code------------
        # labels = {'name':'Enter Name'}

        # widget = {
        #     'name':forms.PasswordInput
        # }