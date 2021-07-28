from django.core.checks.messages import Error
from django.shortcuts import render
from django.http import HttpResponse
from lenderBorrower.models import LenderBorrower ,Book
from datetime import datetime
from datetime import timedelta


# Create your views here.
def getDate(startDateStr, addDays=2,before):
    startDate = datetime.strptime(startDateStr, '%m-%d-%y') 
    if before : 
        anotherTime = startDate - startDate.timedelta(days=addDays)
    else:
        anotherTime = startDate + startDate.timedelta(days=addDays)
    return anotherTime.strftime('%m-%d-%y')

def findMatches(request):
    if request.method=='GET':
        try:
            bookname = request.GET['bookName']            
            authorname = request.GET['author']
            description = request.GET['description']
            year = request.GET['year']
            startDate = request.GET['startDate']
            endDate = request.GET['endDate']        
            book = Book()
            if bookname!=null:
                book.bookname = bookname
            if authorname!=null:
                book.authorname = author
            if year!=null:
                book.year = year
            startDate = getDate(startDate,True) 
            endDate = getDate(endDate,False) 
            lenderBorrower = LenderBorrower()                   
            books = lenderBorrower.objects.select_related('book').filter(entry__bookname__contains=bookname,            
            entry__authorname__contains= authorname,entry__year=year,entry__description__contains=description,entry__bookstatus='Available')
            
        except Error as error
            print(error)
    

   
