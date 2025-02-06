from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
#These views allow us to create pages of blog posts, products, orders, or anything else that would be in a list 
# The generic views do a lot of things automatically but limited customization
#Django's generic ListView. Django provides a lot of components to help us develop our projects rapidly, 
# and the ListView class is one of those.
class PostList(generic.ListView): #class base views
    queryset = Post.objects.all().order_by("created_on") #queryset explicitly stating all posts are displayed.
    #When you change all() to filter(author=1) filtering by the author ID of 1
    #The User model assigns primary key (PK) IDs to all users by default (1 is the superuser)
    template_name = "blog/index.html"
    paginate_by = 6 # pagination settings control = six post per page
    #When we set the paginate_by property in the ListView class, Django adds two items to the data that is passed 
    # through to the template: a boolean value is_paginated and a dictionary object called page_obj
    #For is_paginated, Django counts the number of objects returned by queryset. If that is more than the number 
    # set in the paginate_by property,then is_paginated is set to True otherwise it is set to False.

def post_detail(request, slug): #slg param get the argument from urls.py post_detail. 
    ''' display an individual model:'blog.Post '''
    queryset = Post.objects.filter(status=1) #status constant of models.py mapped to published
    post = get_object_or_404(queryset, slug=slug) #By passing the queryset and the slug argument to get_object_or_404()
    # we only get the post returned with that unique slug.
    # this select a single blog post from the database, the one whose slug matches the slug in our URL and store that 
    # result in a variable called post, and then we add a dictionary as an argument to the render function.
    #  This dictionary is referred to as context.It is convention that the key name would be the same as the variable 
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST) #from forms.py files
        if comment_form.is_valid(): # check the costraints
            comment = comment_form.save(commit=False) #retrun an object that can be modified further (work like the "git add" command)
            comment.author = request.user
            comment.post = post
            comment.save() # this is the commit of the form
            messages.add_message( #is is giving feedback to the user about the posted message
                request,
                messages.SUCCESS,
                'comment submitted and awaiting approval'
            )
    comment_form = CommentForm()
#When the dictionary is sent to the template, we can then access its values using dot notation, 
# Because our post object only contains one database record, 
#we don't need a for loop to iterate through it in the template.
    return render(
        request,
        "blog/post_detail.html", # The path to the template file is included in the view function return. 
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }, #In our views file, we set the name of the object as post, e.g. {"post": post}.
        # So, in post_detail.html, we can now access its attribute
    )
#A view function takes a web request and returns a web response. always passes in the request object as the first argument
#In addition to the mandatory HTTP request object, the post_detail view has also been given a slug parameter.  
#Post (with a capital P) always refers to the Post model created. post (with a lowercase p) refers to an individual blog post,
#  either as an iterator variable in the for loop on the home page 
# or in the variable inside our post_detail view or in the context Python dictionary.

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset,slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, 
                messages.SUCCESS,
                'comment updated!' )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'error updating comment!'
            )
        return HttpResponseRedirect(reverse('post_detail',args=[slug]))