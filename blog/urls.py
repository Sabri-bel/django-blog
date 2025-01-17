from . import views
from django.urls import path

#it is good to separate the urls.py files into separate apps because, as stated, this follows the Django design philosophy of loose coupling. 
#Having one urls.py file per app keeps our apps more modular and independent. It also means that we can more easily change URLs without breaking our project. 
#add a urlpattern for your PostList class-based view named home.As the view is a class, you need an as_view() method
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]