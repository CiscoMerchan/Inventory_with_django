"""To create a new form that will take the entered data into the Product models
and will create a new product """
# django form module
from django import forms
# import the model object 
from .models import Product, Client, Supplier, PurchaseOrder, ClientOrder

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
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())

    class Meta:
        model= PurchaseOrder
        fields = [
            'orderCode', 'product', 'supplier', 'quantity',
        ]

class SearchPurchaseOrderForm(forms.ModelForm):
    orderCode = forms.ModelChoiceField(queryset=PurchaseOrder.objects.all(), required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = PurchaseOrder
        fields = ['orderCode', 'product', 'supplier', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class ClientOrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all())

    class Meta:
        model= ClientOrder
        fields = [
            'orderCode', 'product', 'client', 'quantity',
        ]


