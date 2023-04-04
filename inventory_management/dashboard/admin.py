from django.contrib import admin
from .models import Product

# Register your models here.

# To change name of the headre at the Admin Dashboard
admin.site.site_header ="Welcome to your Inventory"

# To display in the Admin Dashboard the columns of the table as table
"""first create a class initilase with the 'admin' module, with 'list_display'variable make a tuple with the keyNames
of table model in models.py. Then pass the class name in example: 'admin.site.register(Product, ClassName)' """

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'quantity')
    """To add a filter in the admin dashboard in 'Product' table"""
    list_filter = ['category']
# Add models in the Admin Dashboard
admin.site.register(Product, ProductAdmin)