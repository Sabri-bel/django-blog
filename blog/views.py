from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all() #queryset explicitly stating all posts are displayed.
    template_name = "post_list.html"