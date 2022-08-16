from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, Shipping


admin.site.site_header = 'My Shop'
admin.site.site_title = 'My Shop Admin Portal'
admin.site.index_title = 'My Shop Admin'

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)
