from django.contrib import admin
from django.urls import path, include

# Admin Panel Username and Password =>
# username = admin
# Password = admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
