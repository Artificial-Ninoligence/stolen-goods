from django.shortcuts import render
from .models import Payment, Order, OrderProduct

def place_order(request):

    return render(request, 'transactions/place_order.html')

def payments(request):

    return render(request, 'transactions/payment.html')

def order_complete(request):

    return render(request, 'transactions/order_complete.html')
