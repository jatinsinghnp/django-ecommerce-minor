from django.conf.urls import url
from django.urls import path
from .views import CartListView,add_cart,remove_cart,remove_item_cart
app_name='cart'
urlpatterns = [
    path('',CartListView.as_view(),name='cart_page'),
    path('add-cart/<int:product_id>',add_cart,name='add_to_cart'),
    path('remove-cart/<int:product_id>',remove_cart,name='remove_to_cart'),
    path('remove-cart-item/<int:product_id>',remove_item_cart,name='remove_cart_item'),

]
