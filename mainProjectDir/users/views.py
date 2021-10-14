from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class UserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/registerPage.html"
    success_url = "/login"
    success_message = "Account was created successfully, you may now Log In"


class HomePageView(TemplateView):
    template_name = "users/home.html"