from django import forms
from django.forms import fields
from django import forms
from .models import Task

class TaskCreation(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]

        labels = {
            "title":"Task Title",
            "description":"Task Description (Optional)"
        }

        error_messages = {
            "title":{
                "required":"This field is required, ensure that it is not empty."
            }
        }