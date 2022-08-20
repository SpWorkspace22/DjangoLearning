from webbrowser import get
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .forms import CustomUserChangeForm, CustomUserCreation


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser,CustomUserAdmin)




