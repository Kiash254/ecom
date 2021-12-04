from django.contrib import admin
from products.models import Product
# Register your models here.
admin.site.site_header="KIASH FARM PRODUCTS"
admin.site.site_title="KIASH FARM PRODUCTS"
admin.site.register(Product)