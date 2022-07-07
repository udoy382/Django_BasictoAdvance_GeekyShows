from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('excp/', views.excp, name='excp'),
    path('user/', views.user_info, name='user_info'),
]
