from django.contrib import admin
from .models import Student, User

# Register your models here.

# This is a decorators for regester models in admin site only releted with `StudentAdmin model`
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('student_id', 'student_name', 'student_email', 'student_password')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    User_list = ('id', 'nmae', 'email', 'password')

# admin.site.register(Student, StudentAdmin)