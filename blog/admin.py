from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
#The dot in front of models on line 2 indicates that we are 
# importing Post from a file named models, which is in the same directory as our admin.py file.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status',)
    prepolulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here. When we create a custom model and we want it to appear in the admin site, then we need to tell Django by registering it in the admin.py file.
#  That is what admin.site.register does.If you are registering multiple models, you would need a separate line for each model. 
#post redters to the post model created in model.py and imported above in line2
admin.site.register(Comment)

# This will allow you to create, update and delete blog posts from the admin panel. 
#he admin.py file is where we register our custom models so that they can be accessed through the admin panel


