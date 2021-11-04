from django.db import models

# Create your models here.

class Appuser(models.Model):
    class Meta:         
         db_table = 'userapp_appuser'
         
    username = models.CharField(max_length=50,blank=False, default='',primary_key = True)
    firstName = models.CharField(max_length=50, blank=False, default='',)
    lastName = models.CharField(max_length=50, blank=False, default='')    
    userPassword = models.CharField(max_length=50,blank=False, default='')
    age = models.IntegerField(blank=False,default=0)
    address = models.CharField(max_length=255,blank=False, default='')
    pincode = models.CharField(max_length=50,blank=False, default='')
    mobileno = models.BigIntegerField(blank=False,default=0)
    emailid = models.CharField(max_length=50,blank=False, default='')
