from django.urls import path
from .views import indexView, AboutVew, portfolioView, contactView

urlpatterns = [
    path('', indexView, name='index'),
    path('about/', AboutVew, name='about'),
    path('portfolio/',portfolioView, name='portfolio'),
    path('contact/', contactView, name='contact'),
]