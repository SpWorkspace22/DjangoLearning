from django.urls import path

from .views import BlogListView, BlogDeatilView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/',BlogDeatilView.as_view(), name='post_detail'),
    path('',BlogListView.as_view(), name='home'),
]

