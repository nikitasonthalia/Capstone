from django.db import models
from EventHubApp.search.models import User, UserProfile

# Create your models here.
class UserProfileDetails(models.Model):
    profile = models.ForeignKey(UserProfile, models.DO_NOTHING)
    serviceName = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    offers = models.CharField(max_length=50)
    package = models.CharField(max_length=50)
    serviceDetails = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=50)
    aboutProduct = models.CharField(max_length=50)
    aboutUs = models.CharField(max_length=50)