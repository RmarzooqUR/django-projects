from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', context={'form':form})

def login(request):
    pass

def reset_pw(request):
    pass
