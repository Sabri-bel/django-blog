from . import views
from django.urls import path

#add a urlpattern for your PostList class-based view named home.As the view is a class, you need an as_view() method
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]