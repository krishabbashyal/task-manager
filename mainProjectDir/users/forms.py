from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 50, required = True, label = "First Name")
    last_name = forms.CharField(max_length = 50, required=True, label="Last Name")
    username = forms.CharField(max_length = 50, required = True, label="Username")
    password1 = forms.PasswordInput()
    password1 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password'].label = False
