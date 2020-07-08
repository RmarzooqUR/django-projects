from django.shortcuts import render, redirect
from .forms import signUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boardsHome')
    else:
        form = signUpForm()
    return render(request, 'accounts/signup.html', context={'form':form})

def login(request):
    pass

def reset_pw(request):
    pass
