from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app2, name='app2'),
    path('udoy', views.udoy, name='udoy'),
    path('mariyam', views.mariyam, name='mariyam'),
    path('mitu', views.mitu, name='mitu'),
]
