
from django.core.exceptions import ObjectDoesNotExist

from cart.models import Cart, CartItem
from shop.models import Product
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DeleteView

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    print(cart)
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product, quantity=1,
            cart=cart
        )
    return redirect('cart:cart_page')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_page')


class CartListView(ListView):
    template_name = 'cart.html'
    model = Cart

    def get_context_data(self, **kwargs):
        total = 0
        quantity = 0
        cart_items = None

        try:
            cart = Cart.objects.get(cart_id=_cart_id(self.request))
            cart_items = CartItem.objects.filter(cart=cart, is_activate=True)
            for cart_item in cart_items:
                total += (cart_item.product.price*cart_item.quantity)
                quantity += cart_item.quantity
            tax = (13*total) / 100
            grand_total = total+tax

        except ObjectDoesNotExist:
            pass

        context = super().get_context_data(**kwargs)
        context["total"] = total
        context["quantity"] = quantity
        context["cart_items"] = cart_items
        context["tax"] = tax
        context["grand_total"] = grand_total

        return context

def remove_item_cart(request, product_id):

        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.delete()
        return redirect('cart:cart_page')
