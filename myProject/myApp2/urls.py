from django.urls import path
from . import views

urlpatterns = [
    path('', views.learn_django2, name='learn_django2')
]