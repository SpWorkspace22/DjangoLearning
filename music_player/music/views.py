from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView

from .models import Album

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_albums'

    def get_queryset(slef):
        return Album.objects.all()

class DetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Album

class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


    