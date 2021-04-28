from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    
    return redirect('cart')


def remove_cart(request, product_id, cart_item_id):

    return redirect('cart')


def remove_cart_item(request, product_id, cart_item_id):

    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):

    return render(request, 'carts/cart.html')


def checkout(request):
    
    return render(request, 'store/checkout.html')