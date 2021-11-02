from typing import List
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import TaskCreation, TaskUpdate
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class IncompletedView(ListView):
    model = Task
    template_name = "main/IncompletedPage.html"
    context_object_name = "tasks"
    ordering = ['date_created']
 

    def get_queryset(self):
        base = super().get_queryset()
        data = base.filter(author = self.request.user,  completion = False)
        return data

class CompletedView(ListView):
    model = Task
    template_name = "main/Completed.html"
    context_object_name = "tasks"
    ordering = ['date_created']

    def get_queryset(self):
        base = super().get_queryset()
        data = base.filter(author = self.request.user, completion = True)
        return data

class CreateTask(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreation
    template_name = "main/taskCreation.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateTask, self).form_valid(form)
    
    success_url = "/incompleted"
    success_message = "Task was created successfully"

class TaskDetailView(UserPassesTestMixin, DetailView):
    model = Task
    template_name = "main/taskDetail.html"

    def test_func(self):
        task = self.get_object()
        return True if self.request.user == task.author else False

class TaskUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskUpdate
    template_name = "main/taskUpdate.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = "/incompleted"
    success_message = "Task was updated successfully."

    def test_func(self):
        task = self.get_object()
        return True if self.request.user == task.author else False

class TaskDeleteView(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = "main/taskConfirmDelete.html"
    success_url = "/incompleted"
    success_message = "Task was deleted successfully"

    def test_func(self):
        task = self.get_object()
        return True if self.request.user == task.author else False
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDeleteView, self).delete(request, *args, **kwargs)





    
