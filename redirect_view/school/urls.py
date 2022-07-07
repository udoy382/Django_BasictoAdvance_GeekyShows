from django.urls import path
from . import views

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='home'),
    # path('home/', views.RedirectView.as_view(url='/'), name='home2'),
    path('home/', views.RedirectView.as_view(url='https://github.com'), name='home2'),
    # path('index/', views.RedirectView.as_view(url='/'), name='home3'),
    path('index/', views.RedirectView.as_view(pattern_name='home2'), name='home3'),
    path('facebook/', views.RedirectView.as_view(url='https://facebook.com'), name='facebook'),
    path('instagram/', views.InstagramRedirectView.as_view(), name='facebook'),
    path('udoy/<int:pk>', views.TwitterRedirectView.as_view(), name='twitter'),

    path('post/<slug:post>', views.SlugPostRedirectview.as_view(), name='post'),
    path('<slug:post>/', views.TemplateView.as_view(template_name = 'school/home.html'), name='mindex'),
]

