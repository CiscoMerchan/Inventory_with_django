from django.db import models
from django import forms

# Create your models here.
"""Product"""
class Product(models.Model):
    code = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    quantity = models.PositiveIntegerField(null=True)
    image = models.ImageField(default='/static/img/product.png', upload_to='product_images')

    # to return in admin dashboard the name of the columns
    def __str__(self):
        return f'{self.name}.'

"""Client"""    
class Client(models.Model):
    name = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    # to return in admin dashboard the name of the columns
    def __str__(self):
        return f'{self.name}'

"""Supplier"""    
class Supplier(models.Model):
    category = models.CharField(max_length=20)
    name = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    # to return in admin dashboard the name of the columns
    def __str__(self):
        return f'{self.name}'


"""purchase order"""    
class PurchaseOrder(models.Model):
    orderCode = models.CharField(max_length=20 , blank=True, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='purchase_orders')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name='purchase_orders')
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    
    # to return in admin dashboard the name of the columns
    def __str__(self):
        return f'{self.orderCode}'

"""Client order"""    
class ClientOrder(models.Model):
    orderCode = models.CharField(max_length=20, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='client_orders')
    client = models.ForeignKey(Client,on_delete=models.CASCADE, related_name='client_orders')
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    
    # to return in admin dashboard the name of the columns
    def __str__(self):
        return f'Order: {self.orderCode}. Product Name: {self.product}. Client: {self.client}. Qty: {self.quantity}. date: {self.order_date}'



