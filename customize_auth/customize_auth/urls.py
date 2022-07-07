from django.contrib import admin
from django.urls import path, include

# Username = admin
# Password = admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    
]
