from django.shortcuts import render
from django.http import HttpResponse
"""To enforce verification and authorization(in a way that only login user can see the authorases pages)
using 'login_required' (inbuild in django) as decorator"""
from django.contrib.auth.decorators import login_required
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
    return render(request, "dashboard/product.html")

@login_required(login_url='user-login')
def order(request):
    return render(request, "dashboard/order.html")
