from unittest import mock
from django import forms

from .models import Product

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=100)

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
