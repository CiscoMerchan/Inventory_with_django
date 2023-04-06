"""To create a new form that will take the entered data into the Product models
and will create a new product """
# django form module
from django import forms
# import the model object 
from .models import Product, Client, Supplier, PurchaseOrder

# Creation of the form 
class ProductForm(forms.ModelForm):
    class Meta:
        model= Product #importing the model
        fields = [
            'code','name','category','quantity','description','image'
        ] #Form fields

class ClientForm(forms.ModelForm):
    class Meta:
        model= Client
        fields = [
            'name','telephone','email'
            ]
        
class SupplierFrom(forms.ModelForm):
    class Meta:
        model=Supplier
        fields=[
            'category','name','telephone','email',
        ]
       
class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model= PurchaseOrder
        fields = [
            'orderCode', 'product', 'supplier','quantity','order_date', 
        ]
    


