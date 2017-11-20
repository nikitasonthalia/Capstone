from django.db import models
from EventHubApp.search.models import UserProfile

# Create your models here.
class Userprofiledetails(models.Model):
    servicename = models.CharField(db_column='serviceName', max_length=50)  # Field name made lowercase.
    type = models.CharField(max_length=50)
    offers = models.CharField(max_length=50)
    package = models.CharField(max_length=50)
    servicedetails = models.CharField(db_column='serviceDetails', max_length=50)  # Field name made lowercase.
    productdescription = models.CharField(db_column='productDescription', max_length=50)  # Field name made lowercase.
    aboutproduct = models.CharField(db_column='aboutProduct', max_length=50)  # Field name made lowercase.
    aboutus = models.CharField(db_column='aboutUs', max_length=50)  # Field name made lowercase.
    profile = models.ForeignKey(UserProfile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userprofiledetails'