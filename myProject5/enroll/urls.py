from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('forgot-pass/', views.forgot_pass, name='forgotpass'),
]