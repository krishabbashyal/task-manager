from django import forms
from django.forms import fields
from django import forms
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskCreation(forms.ModelForm):
    class Meta:
        model = Task

        fields = ["title", "description", "due_date"]
        widgets = {
            "due_date": DateInput(),
        }

        labels = {
            "title":"Task Title",
            "description":"Task Description (Optional)",
            "due_date":"Due Date (Optional)"
        }

        error_messages = {
            "title":{
                "required":"This field is required, ensure that it is not empty."
            }
        }

class TaskUpdate(forms.ModelForm):
    class Meta:
        model = Task

        fields = ["title", "description", "due_date", "completion"]
        widgets = {
            "due_date": DateInput(),
        }

        labels = {
            "title":"Task Title",
            "description":"Task Description (Optional)",
            "due_date":"Due Date (Optional)"
        }

        error_messages = {
            "title":{
                "required":"This field is required, ensure that it is not empty."
            }
        }

