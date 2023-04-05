"""To create a new form that will take the entered data into the Product models
and will create a new product """
# django form module
from django import forms
# import the model object 
from .models import Product

# Creation of the form 
class ProductForm(forms.ModelForm):
    class Meta:
        model= Product #importing the model
        fields = [
            'code','name','category','quantity','description','image'
        ] #Form fields

        



