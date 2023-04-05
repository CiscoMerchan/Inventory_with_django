from django.shortcuts import render, redirect
from django.http import HttpResponse
"""To enforce verification and authorization(in a way that only login user can see the authorases pages)
using 'login_required' (inbuild in django) as decorator"""
from django.contrib.auth.decorators import login_required

# to import model to render in views that will take it in to .html
from .models import Product, Supplier, Client

# to render the product form to enter new products
from .forms import ProductForm, ClientForm, SupplierFrom

# Create your views here.

"""@login_required(decorator) then 'login_url'=the value will be the precondition 
necesary to acces to the requested page. in this case means that is the user is login
 user have access to 'dashboard/index.html"""
@login_required(login_url='user-login')
def index(request):
    
    return render(request, "dashboard/index.html")

@login_required(login_url='user-login')
def staff(request):
    return render(request, "dashboard/staff.html")

@login_required(login_url='user-login')
def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()    
    
    items = Product.objects.raw(
        'SELECT * FROM dashboard_product'
        )
    context = {
        'items': items,
        'form' : form,
    }

    return render(request, "dashboard/product.html", context)

@login_required(login_url='user-login')
def client(request):

    if request.method == 'POST':
        forms = ClientForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard-client')
    else:
        forms = ClientForm()


    clients = Client.objects.all()

    context = {
        'clients':clients,
        "forms":forms,
    }
    return render(request, 'dashboard/client.html', context)

@login_required(login_url='user-login')
def supplier(request):
    if request.method == 'POST':
        form = SupplierFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-supplier')
    else:
        form = SupplierFrom()

    suppliers = Supplier.objects.all()    

    context = {
        'suppliers':suppliers,
        'form':form
    }


    return render(request, "dashboard/supplier.html", context)


@login_required(login_url='user-login')
def order(request):
    return render(request, "dashboard/order.html")
