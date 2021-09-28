from typing import List
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from .models import Task
from .forms import TaskCreation

# Create your views here.
class IncompletedView(ListView):
    model = Task
    template_name = "main/IncompletedPage.html"
    context_object_name = "tasks"

    def get_queryset(self):
        base = super().get_queryset()
        data = base.filter(author = self.request.user,  completion = False)
        return data

class CompletedView(ListView):
    model = Task
    template_name = "main/Completed.html"
    context_object_name = "tasks"

    def get_queryset(self):
        base = super().get_queryset()
        data = base.filter(author = self.request.user, completion = True)
        return data

class CreateTask(CreateView):
    model = Task
    form_class = TaskCreation
    template_name = "main/taskCreation.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateTask, self).form_valid(form)
    
    success_url = "/incompleted"
    success_message = "Account was created successfully, you may now Log In"
    
