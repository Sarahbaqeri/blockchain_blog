from django import forms
from .models import PostBlog


class AddNewPost(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ['title', 'text', 'author', 'status']



