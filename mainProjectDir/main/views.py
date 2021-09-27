from typing import List
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.

class HomeView(TemplateView):
    template_name = "main/homePage.html"