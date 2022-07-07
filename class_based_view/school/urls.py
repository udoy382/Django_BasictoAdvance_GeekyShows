from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.myview, name='Function_Based_View'),
    path('cls/', views.MyView.as_view(name='Udoy'), name='Class_Based_View'),
    path('sub-cls/', views.MyViewChild.as_view(), name='Sub_Class_Based_View'),
    path('home-func/', views.home, name='home_function'),
    path('home-cls/', views.HomeClassview.as_view(), name='home_class'),
    path('home-cls/', views.HomeClassview.as_view(), name='home_class'),
    path('about-func/', views.about, name='about'),
    path('about-cls/', views.AboutClassView.as_view(), name='about'),
    path('contact/', views.contactfun, name='contact_function'),
    path('contact-cls/', views.ContactClassView.as_view(), name='contact_class_function'),
    path('news/', views.newsfun, name='news_function'),
]