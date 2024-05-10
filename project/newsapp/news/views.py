from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = 'name_post'
    template_name = 'posts_page.html'
    context_object_name = 'post_list'


class PostsDetail(DetailView):
    model = Post
    template_name = 'post_pr.html'
    context_object_name = 'post_name'
