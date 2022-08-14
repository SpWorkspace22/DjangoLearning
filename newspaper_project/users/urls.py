from re import template
from django.urls import path

from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
from .views import SignUpView


urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('password_change/', PasswordChangeView.as_view(template_name ='password_change.html'), name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(template_name='password_done.html'), name='done'),
    path('password_reset/',PasswordResetView.as_view(template_name='registration/password_reset_from.html'), name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='done'),
]
