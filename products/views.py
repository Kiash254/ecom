from types import DynamicClassAttribute
from django.http import request
from django.shortcuts import render
import products
from products.models import Product
from products.models import home


def home (request):
    products=Product.objects.all()
    data={
  products:"products"
    }
    return render(request,"home.html",data)
