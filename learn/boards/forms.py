from django import forms
from .models import Topics, Post

class newTopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['name', 'description']

class newPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['msg', 'description']