from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#A Model is a Python class, and each attribute represents a database field. Each model in your models.py file maps directly to a single database table.
#Every model you create is a Python class that subclasses the parent class of models.Model. 

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) 
    #In publishing, a slug is a short name for an article that is still in production.
    # In Django, the slug is what you'll use to build a URL for each of your posts. 
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
        )
    #One user can write many posts, so this is a one-to-many or Foreign Key. 
    content = models.TextField() #this is the blog article content itself
    created_on = models.DateTimeField(auto_now_add=True)
    #The auto_now_add=True means the default created time is the time of post entry. 
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

