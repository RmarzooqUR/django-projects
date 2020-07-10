from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/pw_reset.html',
        email_template_name='accounts/pw_reset_email.html',
        subject_template_name='accounts/subject.txt'
    ), name='password_reset'),
    path('reset/done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/pw_reset_done.html'), name='password_reset_done'),
    path('reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/pw_reset_complete.html'), name='password_reset_complete'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/pw_reset_confirm.html'), name='password_reset_confirm')
]
