from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student_detail_view'),
]
