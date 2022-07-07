from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('add-post/', views.addpost, name='addpost'),
    path('update-post/<int:id>/', views.updatepost, name='updatepost'),
    path('delete-post/<int:id>/', views.deletepost, name='deletepost'),
]