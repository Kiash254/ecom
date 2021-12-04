from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    price=models.CharField(max_length=255,blank=True,null=True)
    tax=models.CharField(max_length=255,blank=True,null=True)


    def __str__(self):
        return f'name {self. name }price{self. price} tax{self.tax}'
    