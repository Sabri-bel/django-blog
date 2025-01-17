from django.shortcuts import render, get_object_or_404
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
    template_name = "blog/index.html"
    paginate_by = 6 # pagination settings control = six post per page
    #When we set the paginate_by property in the ListView class, Django adds two items to the data that is passed through to the template: a boolean value, 
    # is_paginated and a dictionary object called page_obj, which we just call the Page object.
    #For is_paginated, Django counts the number of objects, or records, returned by our queryset. If that is more than the number set in the paginate_by property,
    #  then is_paginated is set to True otherwise it is set to False.

def post_detail(request, slug):
    ''' display an individual model:'blog.Post '''
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "blog/post_detail.html",
        {"post": post}
    )