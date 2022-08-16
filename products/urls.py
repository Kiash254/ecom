from django.urls import path
from .views import product, cart, checkout


app_name="products"

urlpatterns=[

    path("",product,name="product"),
    path("cart/",cart,name="cart"),
    path("checkout/",checkout,name="checkout"),
]