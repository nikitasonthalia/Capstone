from django.db import models
from django.template.defaultfilters import default

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
    category_id = models.IntegerField(primary_key=True, default=0)
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category_url = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        #return self.category_name
        return '%s %s' % (self.category_name, self.category_url)