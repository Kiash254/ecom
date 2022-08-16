from .models import Product, Order, OrderItem, Shipping, Customer
from django.http import request
from django.shortcuts import render


def product(request):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(request, 'product.html', context)

def cart(request):
      context={}
      return render(request, 'cart.html')

def checkout(request):
     context={}
     return render(request, 'checkout.html')


