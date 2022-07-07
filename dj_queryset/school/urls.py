from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home')
    # path('', views.home2, name='home2')
    path('', views.home3, name='home3')
]