from . import views
from django.urls import path

urlpatterns = [
    path('', views.About_me, name='about'),
]