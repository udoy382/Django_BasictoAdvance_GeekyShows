from django.urls import path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.home, {'check':'OK'}, name='home'),
    path('student-info/', views.studentInfo, name='studentInfo'),
    path('registration/', views.showFormData, name='registration'),
    path('forms/', views.forms, name='forms'),
    path('success/', views.thankYou, name='thankYou'),

    # path('show-details/<my_id>', views.showDetails, name='showDetails'),
    # path('show-details/<int:my_id>', views.showDetails, name='showDetails'),
    # path('show-details/<int:my_id>/<int:my_sub_id>', views.subDetails, name='subDetails'),
    path('details/<yyyy:year>', views.details, name='details'),
]
