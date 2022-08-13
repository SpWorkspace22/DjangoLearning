from cgitb import html
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

'''def homePageView(request):

    return render(request,'pages/home.html')'''

class HomePageView(TemplateView):
    template_name= 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html' 

