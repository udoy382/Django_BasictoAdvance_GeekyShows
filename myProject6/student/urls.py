from django.urls import path
from . import views

urlpatterns = [
    path('set-cookie', views.set_cookie, name='setcookie'),
    path('get-cookie', views.get_cookie, name='getcookie'),
    path('del-cookie', views.delete_cookie, name='deletecookie'),

    path('set-session', views.set_session, name='setsession'),
    path('get-session', views.get_session, name='getsession'),
    path('del-session', views.del_session, name='delsession'),

    path('set-test-cookie', views.settestcookie, name='settestcookie'),
    path('check-test-cookie', views.checktestcookie, name='checktestcookie'),
    path('del-test-cookie', views.deltestcookie, name='deltestcookie'),
]