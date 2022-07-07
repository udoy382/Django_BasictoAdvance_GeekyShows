from django.contrib import admin
from django.urls import path, include

# Usernaem = admin
# Password = admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]


