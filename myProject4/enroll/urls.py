from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.showFormData, name='showFormData'),
    path('student/', views.student_form, name='student'),
    path('teacher/', views.teacher_form, name='teacher'),
]