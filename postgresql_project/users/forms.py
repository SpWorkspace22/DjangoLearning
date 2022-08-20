from dataclasses import field
from pyexpat import model
from webbrowser import get
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields  = ('email','username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email','username',)


