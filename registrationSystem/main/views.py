from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    template_name =  'main/index.html'

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'