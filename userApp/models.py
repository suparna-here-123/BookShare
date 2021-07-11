from django.db import models

# Create your models here.

class Appuser(models.Model):   
    firstName = models.CharField(max_length=50, blank=False, default='',)
    lastName = models.CharField(max_length=50, blank=False, default='')
    userId = models.CharField(max_length=50,blank=False, default='',primary_key = True)
    userPassword = models.CharField(max_length=50,blank=False, default='')
    age = models.IntegerField(blank=False,default=0)
    address = models.CharField(max_length=255,blank=False, default='')
    pincode = models.CharField(max_length=50,blank=False, default='')
    mobileno = models.BigIntegerField(blank=False,default=0)
    emailid = models.CharField(max_length=50,blank=False, default='')
