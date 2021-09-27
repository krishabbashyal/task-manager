from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

class UserView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/registerPage.html"
    success_url = "/home"
