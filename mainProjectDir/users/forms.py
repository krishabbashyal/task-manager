from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length= 50, required=True)
    last_name = forms.CharField(max_length= 50, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

        
    labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            'password1': "Password",
            'password2': "Confirm Password"
        }
    
    