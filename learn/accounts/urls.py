from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('reset-pw/', views.reset_pw, name='reset-pw'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
