from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class signUpForm(UserCreationForm):
    email = forms.EmailField(help_text='example@example.com', widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

# class loginForm(UserCreationForm):
