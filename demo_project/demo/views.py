from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView

from .forms import ContactForm, ProductCreationForm
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = "prod_list.html"
    paginate_by =  2


class ProductDetailsView(DetailView):
    model = Product
    template_name = "prod_detail.html"

class ContactFormView(FormView):
    template_name = "def_form.html"
    form_class = ContactForm

class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    template_name = "def_form.html"
    success_url = reverse_lazy("prlist")

class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "def_form.html"
    success_url = reverse_lazy("prlist")


def index(request):

    if request.method=='POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ProductCreationForm()

    page = {
        "forms":form,
        "title":"TODO LIST" 
    }

    return render(request,'index.html',page)
