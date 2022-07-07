from django.urls import path
from . import views

urlpatterns = [
    # ********** Page Counter URL ***********
    path('/', views.home, name='home')
]