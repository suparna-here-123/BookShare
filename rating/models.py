from django.db import models
from lenderBorrower.models import LenderBorrower

# Create your models here.

class Rating(models.Model):
    id =  models.AutoField(primary_key=True)
    lenderBorrowerId =  models.ForeignKey(LenderBorrower, on_delete=models.CASCADE)
    bookcondtion = models.IntegerField()
    punctuality = models.IntegerField()   
    reasonForFlagging = models.CharField(max_length=20, blank=False, default='')
    flagTheUser = models.BooleanField()
    countForMishnadling = models.IntegerField()
    countForNoShow = models.IntegerField()
