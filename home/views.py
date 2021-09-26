
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from shop.models import Product
# Create your views here.


class HomePageView(ListView):
    template_name = 'index.html'
    model = Product
    queryset = Product.objects.all().filter(is_available=True)
    context_object_name = 'products'


class ProductDetailPageView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product-detail.html'

    def get_object(self, queryset=None):
        return Product.objects.get(slug=self.kwargs.get('slug'))
