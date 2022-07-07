from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='home'),
    path('', views.PostListView.as_view(), name='home'),
]
