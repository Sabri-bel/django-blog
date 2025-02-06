from . import views
from django.urls import path

#it is good to separate the urls.py files into separate apps because, as stated, this follows the Django design philosophy of loose coupling. 
#Having one urls.py file per app keeps our apps more modular and independent. It also means that we can more easily change URLs without breaking our project. 
#add a urlpattern for your PostList class-based view named home.As the view is a class, you need an as_view() method
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), #Note that as this is a function-based view, no as_view() method is required, as we saw with class-based views
    path('<slug:slug>/edit_comment/<int:comment_id>', 
        views.comment_edit, name='comment_edit'),
]
#In the post_detail URL path, the argument value from the url tag is then passed into <slug:slug>. The slug path converter before the colon defines the data type as a slug, 
# and the slug after the colon is the post.slug value passed from the template. 
 #The critical component of the URL pattern for this topic is the part enclosed in angle brackets, denoted as <slug:slug>. This is where the slug value is passed from the template's URL tag. 
 #This urlpattern creates a url path of the domain path plus the slug value.
#A string is appended to the end of the URL path that uniquely identifies the blog post. This string is the slug, which is the blog title in lowercase, 
# with all spaces replaced with dashes and all punctuation removed.