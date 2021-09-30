
from category.models import Category
from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Product
# Create your views here.


class StorePageListView(ListView):
    template_name = 'store.html'
    model = Product

    def get_context_data(self, **kwargs):

        products = None
        categories = None

        try:
          cat_slug =self.kwargs['cat_slug']
        except:
            cat_slug=None

        context = super().get_context_data(**kwargs)

        if cat_slug != None:
            categories = get_object_or_404(
                Category, slug=cat_slug)
            products=Product.objects.filter(is_available=True,category=categories)
            count = products.count()
            context["products"] = products
            context["count"] = count

        else:
            products = Product.objects.filter(is_available=True)
            count = products.count()
            context["products"] = products
            context["count"] = count

        return context
