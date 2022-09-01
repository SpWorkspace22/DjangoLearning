from django.shortcuts import render

# Create your views here.
from .models import Projects

def indexView(request):
    return render(request,'index.html',{})

def AboutVew(request):
    return render(request,'about.html',{})


def portfolioView(request):
    all_projects = Projects.objects.all()

    return render(request,'portfolio.html',{'project_list':all_projects})


def contactView(request):
    return render(request,'contact.html',{})