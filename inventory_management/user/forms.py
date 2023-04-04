"""
This module is created to add in the register form the email.(because in thr UserCreationForm
inbuild with django only takes: username, password1 and password2. So to register the email user
and add to the User table and using for the login form in login.html, is necessary to modify
the original form). Ten this form is export to user/views.py and rendered in register.html
"""

from django import forms
# Table User
from django.contrib.auth.models import User
# Django inbuild UserCreationForm 'form'
from django.contrib.auth.forms import UserCreationForm 

# create a new class to export in user/views.py
class CreateUserForm(UserCreationForm):
    # add email field
    email = forms.EmailField()

    class Meta:
        # Table
        model = User
        # new form fields to render in register.html and add in User table
        fields = ['username','email','password1', 'password2']