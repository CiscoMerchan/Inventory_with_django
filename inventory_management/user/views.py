from django.shortcuts import render, redirect
# to create a form with django
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('ojk')
            return redirect('user/login.html')
    else:    
        form =UserCreationForm()
    return render(request, 'user/register.html',{'form':form})


