from django.urls import path
from . import views

urlpatterns = [
    # path('', views.TemplateView.as_view(template_name = 'school/home.html'), name='home'),
    path('', views.HomeTemplateView.as_view(extra_context={'course':'Python'}), name='home'),
    path('about/<int:cl>', views.HomeTemplateView.as_view(extra_context={'course':'Python'}), name='class'),
]
