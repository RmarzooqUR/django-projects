from django.shortcuts import render, redirect
from .forms import signUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.urls import reverse_lazy
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

class UpdatUserView(UpdateView):
    model = User
    template_name = 'accounts/my_account.html'
    fields = ('first_name', 'last_name', 'email', )
    success_url = reverse_lazy('myaccount')

    def get_object(self):
        return self.request.user

