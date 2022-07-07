from django.urls import path
from . import views

urlpatterns = [
    # ---------------Function Based View Urls---------------

    # path('', views.add_show, name='add_show'),
    # path('delete/<int:id>/', views.delete_data, name='deletedata'),
    # path('<int:id>/', views.update_data, name='updatedata'),



    # ----------------Class Based View Urls----------------

    path('', views.UserAddShowView.as_view(), name='index'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name='deletedata'),
    path('<int:id>/', views.UserUpdateView.as_view(), name='updatedata'),
]
