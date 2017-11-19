from django.db import models
from django.forms import ModelForm
# from django.core.validators import RegexValidator
from datetime import date
from EventHubApp.search.models import User, UserProfile


class Contact(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=50)
    reason = models.CharField(max_length=50)
    messsage = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastUpdatedDate = models.DateTimeField(auto_now=True)