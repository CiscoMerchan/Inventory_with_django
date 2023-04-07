from django.shortcuts import render, redirect
from django.http import HttpResponse
"""To enforce verification and authorization(in a way that only login user can see the authorases pages)
using 'login_required' (inbuild in django) as decorator"""
from django.contrib.auth.decorators import login_required

# to import model to render in views that will take it in to .html
from .models import Product, Supplier, Client, PurchaseOrder

# to render the product form to enter new products
from .forms import ProductForm, ClientForm, SupplierFrom, PurchaseOrderForm, SearchPurchaseOrderForm

# to seach 
from django.db.models import Q

# Create your views here.
# ------------INDEX -----------------------#
"""@login_required(decorator) then 'login_url'=the value will be the precondition 
necesary to acces to the requested page. in this case means that is the user is login
 user have access to 'dashboard/index.html"""
@login_required(login_url='user-login')
def index(request):
    
    return render(request, "dashboard/index.html")
# ------------END INDEX-----------------------#

@login_required(login_url='user-login')
def staff(request):
    return render(request, "dashboard/staff.html")


# ------------PRODUCT-----------------------#
#---- CREATE AND READ PRODUCT
@login_required(login_url='user-login')
def product(request):
    #CREATE PRODUCT
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()    
    # READ PRODUCT
    items = Product.objects.raw(
        'SELECT * FROM dashboard_product'
        )
    context = {
        'items': items,
        'form' : form,
    }

    return render(request, "dashboard/product.html", context)

# DELETE PRODUCT
def product_delete(request,pk):
    # item will retain the id of thproduct which in this case will be the pk that model asign automaticly to each product
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

# UPDATE PRODUCT (Edit)
def product_update(request,pk):
    
    item_to_update = Product.objects.get(id=pk)
    if request.method == 'POST':
            form = ProductForm(request.POST, 
                               instance=item_to_update) #item_to_update, will render the choosen product and rendered in the form
            if form.is_valid():
                form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item_to_update)
    context = {
            'form':form,

        }    
        
    return render(request, 'dashboard/product_update.html',context)



# ------------END PRODUCT-----------------------#

# ------------CLIENT-----------------------#
# CREATE AND READ
@login_required(login_url='user-login')
def client(request):
    # CREATE
    if request.method == 'POST':
        forms = ClientForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard-client')
    else:
        forms = ClientForm()

    # READ
    clients = Client.objects.all()

    context = {
        'clients':clients,
        "forms":forms,
    }
    return render(request, 'dashboard/client.html', context)

# EDIT
def client_update(request,pk):
    item_to_update = Client.objects.get(id=pk)
    if request.method == 'POST':
            form = ClientForm(request.POST, 
                               instance=item_to_update) #item_to_update, will render the choosen client and rendered in the form
            if form.is_valid():
                form.save()
            return redirect('dashboard-client')
    else:
        form = ClientForm(instance=item_to_update)
    context = {
            'form':form,

        }    
    return render(request,'dashboard/client_update.html', context)

# DELETE
def client_delete(request,pk):
    client = Client.objects.get(id = pk)
    if request.method == 'POST':
        client.delete()
        return redirect('dashboard-client')
   
    
    return render(request,'dashboard/client_delete.html')
 
# ------------END CLIENT-----------------------#

# ------------SUPPLIER-----------------------#
# CREATE AND READ
@login_required(login_url='user-login')
def supplier(request):
    # CREATE
    if request.method == 'POST':
        form = SupplierFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-supplier')
    else:
        # READ
        form = SupplierFrom()

    suppliers = Supplier.objects.all()    

    context = {
        'suppliers':suppliers,
        'form':form
    }


    return render(request, "dashboard/supplier.html", context)

# UPDATE (EDIT)
def supplier_update(request,pk):
    item_to_update = Supplier.objects.get(id=pk)
    if request.method == 'POST':
            form = SupplierFrom(request.POST, 
                               instance=item_to_update) #item_to_update, will render the choosen supplier and rendered in the form
            if form.is_valid():
                form.save()
            return redirect('dashboard-supplier')
    else:
        form = SupplierFrom(instance=item_to_update)
    context = {
            'form':form,

        }    
    return render(request,'dashboard/supplier_update.html', context)


# DELETE
def supplier_delete(request,pk):
    supplier = Supplier.objects.get(id = pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('dashboard-supplier')
   
    
    return render(request,'dashboard/supplier_delete.html')


# ------------END SUPPLIER-----------------------#
@login_required(login_url='user-login')
def order(request):
    return render(request, "dashboard/order.html")


# ------------PURCHASE ORDERS-----------------------#
# CREATE AND READ
@login_required(login_url='user-login')
def purchase_order(request):
    # CREATE
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            # Save the purchase order
            order = form.save()

            # Update the product quantity
            product = order.product
            product.quantity += order.quantity
            product.save()

            return redirect('dashboard-purchase-order')
    else:
        # READ
        form = PurchaseOrderForm()
    
    orders = PurchaseOrder.objects.all()
    context = {
        'orders': orders,
        'form': form,
    }
    return render(request, "dashboard/purchase_order.html", context)


# SEARCH
def search_purchase_order(request):
    form = SearchPurchaseOrderForm(request.POST or None)
    queryset = PurchaseOrder.objects.all()

    if request.method == 'POST' and form.is_valid():
        order_code = form.cleaned_data.get('orderCode')
        product = form.cleaned_data.get('product')
        supplier = form.cleaned_data.get('supplier')
        date = form.cleaned_data.get('date')
        
        if order_code:
            queryset = queryset.filter(orderCode=order_code)
        if product:
            queryset = queryset.filter(product__name__icontains=product)
        if supplier:
            queryset = queryset.filter(supplier__icontains=supplier)
        if date:
            queryset = queryset.filter(order_date=date)

    context = {
        'form': form,
        'queryset': queryset,
    }
    return render(request, 'dashboard/purchase_order_list.html', context)
