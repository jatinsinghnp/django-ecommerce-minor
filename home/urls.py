from django import urls
from django.urls import path
from .views import HomePageView
from .views import ProductDetailPageView
app_name = 'root'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<slug:slug>', ProductDetailPageView.as_view(), name='product_list'),

]
