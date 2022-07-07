from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileTemplateView.as_view(), name='Profile'),
]