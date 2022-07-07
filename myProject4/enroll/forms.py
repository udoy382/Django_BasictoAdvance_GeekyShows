from django import forms
from .models import User


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'password', 'email']

        # show all form in registration page, this is a sort and easy process
        # fields = '__all__'

        exclude = ['name']


# second code
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name', 'email', 'password']


class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ['teacher_name', 'email', 'password']