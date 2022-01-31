from django.db import models
from userApp import models as m

# Create your models here.

class Book(models.Model):
    class Meta:         
         db_table = 'book'
    book_id =  models.BigIntegerField(blank=False,default=0,primary_key=True)
    bookname = models.CharField(max_length=255, blank=False, default='')
    authorname = models.CharField(max_length=255, blank=False, default='')
    genre = models.CharField(max_length=50, blank=False, default='')
    bookcondition = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=255, blank=False, default='')
    bookedition = models.CharField(max_length=100, blank=False, default='')
    bookstatus = models.CharField(max_length=100, blank=False, default='')
    user_name =  models.ForeignKey(m.Appuser,on_delete=models.CASCADE , db_column='user_name')
    borrower = models.CharField(max_length=50, blank=False, default='')
    
    
  
