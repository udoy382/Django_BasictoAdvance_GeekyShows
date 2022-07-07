from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('static/', views.staticsite, name='staticsite'),
    path('a_static/', views.another_static, name='another_static'),
]
