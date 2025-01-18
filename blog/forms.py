from .models import Comment
from django import forms

# form is inherited from built in django class imported above
class CommentForm(forms.ModelForm):
    #since form is built in, we just need to create the meta file for  specify what 
    #model and fields we want in our form
    class Meta:
        model = Comment
        fields = ('body',) #imported from the comment model