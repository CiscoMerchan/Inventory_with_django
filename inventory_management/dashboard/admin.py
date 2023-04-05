from django.contrib import admin
from .models import Product,Client, Supplier, ClientOrder, PurchaseOrder

# Register your models here.

# To change name of the headre at the Admin Dashboard
admin.site.site_header ="Welcome to your Inventory"

# To display in the Admin Dashboard the columns of the table as table
"""first create a class initilase with the 'admin' module, with 'list_display'variable make a tuple with the keyNames
of table model in models.py. Then pass the class name in example: 'admin.site.register(Product, ClassName)' """

class ProductAdmin(admin.ModelAdmin):
    list_display = ('code','name', 'category', 'description', 'quantity','image')
    """To add a filter in the admin dashboard in 'Product' table"""
    list_filter = ['category']
# Add models in the Admin Dashboard


#___Admin Dashboard Register____
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Client)
admin.site.register(PurchaseOrder)
admin.site.register(ClientOrder)
