from .models import *
from django.http import request
from django.shortcuts import render


def product(request):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(request, 'product.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        customer, order = guestOrder(request, data)
        items=[]
        order={
            'get_cart_total':0,'get_cart_items':0,'shipping':False
        }
    
        context={
            "items":items,
            "order":order,

        }
        return render(request, 'cart.html', context)
      

def checkout(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        context={
            "items":items,
            "order":order,

        }
        return render(request, 'checkout.html', context)

    # else:
    #     items=[]
    #     order={
    #         'get_cart_total':0,'get_cart_items':0,'shipping':False
    #     }
    
    #     context={
    #         "items":items,
    #         "order":order,

    #     }
    #     return redirect('products:product')
    # return render(request, 'checkout.html',context)


