from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView

# Create your views here.

# ------------Function Based View--------------

"""
def post_list(request):
    all_post  = Post.objects.all().order_by('id')

    # paginator = Paginator(all_post, 3)
    paginator = Paginator(all_post, 3, orphans=1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'myapp/home.html', {'posts':page_obj})
"""

# ------------Class Based View-------------- DOESN'T WORK

class PostListView(ListView):
    model = Post
    template_name = 'myapp/home.html'
    ordering = ['id']
    paginate_by = 3