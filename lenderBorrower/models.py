from django.db import models
from userApp import models as m

# Create your models here.

'''class LenderBorrower(models.Model):
    id =  models.AutoField(primary_key=True)
    userName =  models.CharField(max_length=20, blank=False, default='')
    borrowerStartdate = models.DateTimeField(null=True, blank=True)
    borrowerEnddate = models.DateTimeField(null=True, blank=True)
    lenderEnddate = models.DateTimeField(null=True, blank=True)
    lenderStartdate = models.DateTimeField(null=True, blank=True)
    userType = models.CharField(max_length=20, blank=False, default='')   
    returnPolicy = models.CharField(max_length=2000, blank=False, default='')
    hasWishlist = models.BooleanField()
    lendingpolicyAgreement = models.BooleanField()'''

class Book(models.Model):
    class Meta:         
         db_table = 'book'
    book_id =  models.BigIntegerField(blank=False,default=0,primary_key=True)
    bookname = models.CharField(max_length=255, blank=False, default='')
    authorname = models.CharField(max_length=255, blank=False, default='')
    genre = models.CharField(max_length=50, blank=False, default='')
    bookcondition = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=255, blank=False, default='')
    bookphoto = models.CharField(max_length=100, blank=False, default='')
    bookstatus = models.CharField(max_length=100, blank=False, default='')
    user_name =  models.ForeignKey(m.Appuser,on_delete=models.CASCADE , db_column='user_name')
    borrower = models.CharField(max_length=50, blank=False, default='')
    
    
  
