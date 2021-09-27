from typing import List
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Task

# Create your views here.

class HomeView(ListView):
    model = Task
    template_name = "main/homePage.html"
    context_object_name = "tasks"