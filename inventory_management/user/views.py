from django.shortcuts import render, redirect
# to create a form with django
from django.contrib.auth.forms import UserCreationForm

#  import form from user/forms.py
from .forms import CreateUserForm

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print('ojk')
            return redirect('dashboard-index')
    else:    
        form =CreateUserForm()
    return render(request, 'user/register.html',{'form':form})


