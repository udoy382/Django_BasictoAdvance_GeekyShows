from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('mymath', views.my_math, name='my_math'),
    # path('dj', views.learn_django, name='learn_django'),


    path('', views.home, name='home'),
    path('templ', views.templ, name='templ')
]