from django.urls import path
from .views import StorePageListView
app_name = 'store'
urlpatterns = [
    path('', StorePageListView.as_view(), name='store'),
    path('<slug:cat_slug>', StorePageListView.as_view(), name='products_by_cat')

]
