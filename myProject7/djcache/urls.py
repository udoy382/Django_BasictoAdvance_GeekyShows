from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    # path('', cache_page(60) (views.home), name='home'),
    # path('home/', views.home, name='home_again'),

    path('', views.home, name='home_again'),
    
    path('contact', views.contact, name='contact'),
    path('cache-tem', views.cache_tamplates, name='cache_tamplates'),
]
