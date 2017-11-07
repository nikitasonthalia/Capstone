from django.db import models
from django.forms import ModelForm
#from django.core.validators import RegexValidator
from datetime import date

# Create your models here.
class User(models.Model):
    id = models.IntegerField
    user_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    street1 = models.CharField(max_length=30)
    street2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pin_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        return self.username

class Category(models.Model):
    category_id = models.IntegerField
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category_url = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        #return self.category_name
        return '%s %s' % (self.category_name, self.category_url)

class ServiceProviders(models.Model):
    title = models.CharField(max_length=50)
    inputFname = models.CharField(max_length=50)
    inputLname = models.CharField(max_length=50)
    emailId = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)
    birthDate = models.DateField(default=date.today)
    pic = models.ImageField(upload_to="")
    stadd1 = models.CharField(max_length=50)
    stadd2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    serviceDesc = models.CharField(max_length=50)


class ServiceProviderDetails(models.Model):
    spID = models.CharField(max_length=50)
    serviceName = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    offers = models.CharField(max_length=50)
    package = models.CharField(max_length=50)
    serviceDetails = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=50)
    aboutProduct = models.CharField(max_length=50)
    aboutUs = models.CharField(max_length=50)