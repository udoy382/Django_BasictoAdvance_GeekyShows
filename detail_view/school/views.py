from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView

# Create your views here.


class StudentDetailView(DetailView):
    model = Student