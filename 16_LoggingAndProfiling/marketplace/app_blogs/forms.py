from django import forms
from app_blogs.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['is_published']
