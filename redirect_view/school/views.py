from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.


class InstagramRedirectView(RedirectView):
    url = 'https://instagram.com'

class TwitterRedirectView(RedirectView):
    url = 'https://twitter.com'


class SlugPostRedirectview(RedirectView):
    pattern_name = 'mindex'
    permanent = True
    # query_string = False
    query_string = True