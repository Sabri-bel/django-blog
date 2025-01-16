from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
#These views allow us to create pages of blog posts, products, orders, or anything else that would be in a list, very quickly. 
# The generic views do a lot of things automatically but limited customization
#Django's generic ListView. Django provides a lot of components to help us develop our projects rapidly, 
# and the ListView class is one of those.
class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("created_on") #queryset explicitly stating all posts are displayed.
    #When you change all() to filter(author=1) on the queryset line filtering by the author ID of 1
    #The User model assigns primary key (PK) IDs to all users by default (1 is the superuser)
    template_name = "post_list.html"