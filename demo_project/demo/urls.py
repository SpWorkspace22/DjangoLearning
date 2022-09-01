from django.urls import path
from .views import ProductListView, ProductDetailsView,ContactFormView, ProductCreateView, ProductUpdateView, index

urlpatterns = [
    path('prod_list/', ProductListView.as_view(), name="prlist"),
    path('prod_details/<int:pk>/', ProductDetailsView.as_view()),
    path('def/',ContactFormView.as_view()),
    path('add/',ProductCreateView.as_view()),
    path('update/<int:pk>/', ProductUpdateView.as_view()),
    path("index/",index,name="index"),
]