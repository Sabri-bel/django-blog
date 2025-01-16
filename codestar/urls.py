"""
URL configuration for codestar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #it allows to use and import another urls.py file
#Our project-level urls.py file should include the urls.py files in all of our apps, and, therefore, will define our top-level URL structure


urlpatterns = [
    #This pattern tells Django to look in the blog directory URL file for any blog urlpatterns.
    path('', include("blog.urls"), name='blog-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
]
 #Next, we need to create a templates directory in the blog app, with another directory nested within, named blog. Django expects this file structure. 
 # To create the directory structure, use the following command in the terminal:mkdir -p blog/templates/blog