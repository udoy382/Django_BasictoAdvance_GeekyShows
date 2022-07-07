from django.urls import path
from django.contrib.auth.decorators import login_required
from registration import views

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    # path('profile/', login_required(views.ProfileTemplateView.as_view()), name='profile'),
    path('profile/', views.ProfileTemplateView.as_view(), name='profile'),
]

