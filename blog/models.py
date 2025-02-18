from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# A Model is a Python class, and each attribute represents a database field. Each model in your models.py file maps directly to a single database table.
# Every model you create is a Python class that subclasses the parent class of models.Model. 

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    stores a single blogpost entry related to model:'auth.User'
    """
    # The slug is used for the blog post path as it uniquely identifies the post and contains only characters valid for a URL. In our Post model, we defined that the title and slug are unique,
    #  with unique=True, so we can be sure that the slug will only match one blog post
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) 
    # In publishing, a slug is a short name for an article that is still in production.
    # In Django, the slug is what you'll use to build a URL for each of your posts.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
        )
    featured_image = CloudinaryField('image', default='Placeholder')
    # One user can write many posts, so this is a one-to-many or Foreign Key. 
    content = models.TextField()  # this is the blog article content itself
    created_on = models.DateTimeField(auto_now_add=True)
    # The auto_now_add=True means the default created time is the time of post entry. 
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)  # The auto_now sets the value to the current date and time whenever the record is saved, not just when it is created.
    field_2 = models.CharField(default='hello world')  # set a custom value as default for the new field
    field_3 = models.CharField(null=True)  # set a null value as default for the new field
    
    class Meta:  # this is an optional class and it is used for data not inclused in the table fields
        ordering = ["-created_on", "author"]  # the hash symbol make it reverse newer to older data creation
    # The __str__() method has changed this post identifier to a string literal. By passing self as an argument to the __str__() method,
    # you can use the field values in the f-string and you can see the title instead of post object(n)
    
    def __str__(self):
        return f"the title of this post is {self.title} | made by {self.author}"


class Comment(models.Model):
    """
    store a single comment entry related to model:'auth.user' and model:'blog.post'
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False) 
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"comment {self.body} by {self.author}"


