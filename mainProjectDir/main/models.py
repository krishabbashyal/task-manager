from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=175,  blank = True)
    completion = models.BooleanField(default=False)
    due_date = models.DateField(blank = True, null = True)
    date_created = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self):
        return self.title