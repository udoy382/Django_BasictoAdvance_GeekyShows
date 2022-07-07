from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

# Create your views here.


# @login_required
# def profile(reqeust):
#     return render(request, 'registration/profile.html')


# ----------------------------

# class ProfileTemplateView(TemplateView):
#     template_name = 'registration/profile.html'


# -----------------------

class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)