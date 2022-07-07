from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.

# ------------Built in - generic class based view and listview-------------

# class StudentListView(ListView):
#     model = Student


# ------------custom - generic class based view and listview-------------

# class StudentListView(ListView):
#     model = Student
#     template_name_suffix = '_get' # change default template name with this functon
#     ordering = ['course'] # ordering our data 


# ------------more custom - generic class based view and listview-------------

class StudentListView(ListView):
    model = Student
    template_name = 'school/student.html' # change default full template name
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='Python')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')

        return context


    def get_template_names(self):
        # if self.request.COOKIES['user'] == 'udoy':
        if self.request.user.is_superuser:
            # template_name = 'school/udoy.html'
            template_name = 'school/staff.html'
        else:
            template_name = self.template_name
        
        return [template_name]