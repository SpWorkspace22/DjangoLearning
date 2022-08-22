from django.urls import path
from .views import IndexView, DetailView, AlbumCreateView

app_name = "music"

urlpatterns  = [
    path('',IndexView.as_view(),name="index"),
    path('<int:pk>/',DetailView.as_view(),name="detail"),
    path('<int:pk>/album/add/',AlbumCreateView.as_view(), name="album-add"),
]