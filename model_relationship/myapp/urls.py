from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/', views.page, name='page'),
    path('post/', views.post, name='post'),
    path('song/', views.song, name='song'),
    path('user/', views.user, name='user'),
]
