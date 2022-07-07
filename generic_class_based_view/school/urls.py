from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentListView.as_view(), name='student')
]
