from django.urls import path

from .views import BlogListView, BlogDeatilView

urlpatterns = [
    path('post/<int:pk>/',BlogDeatilView.as_view(), name='post_detail'),
    path('',BlogListView.as_view(), name='home'),
]

