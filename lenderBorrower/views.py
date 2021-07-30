from django.core.checks.messages import Error
from django.shortcuts import render
from django.http import HttpResponse
from lenderBorrower.models import LenderBorrower ,Book
from datetime import datetime
from datetime import timedelta


# Create your views here.
def getDate(startDateStr, addDays,before):
    startDate = datetime.strptime(startDateStr, '%m-%d-%y') 
    if before : 
        anotherTime = startDate - startDate.timedelta(days=addDays)
    else:
        anotherTime = startDate + startDate.timedelta(days=addDays)
    return anotherTime.strftime('%m-%d-%y')

def filterData(lenderBorrowerbooks):
    priorityDict = {}
    for item in lenderBorrowerbooks:
        if item.borrowerStartdate >= item.lenderStartdate and item.borrowerEnddate <= item.lenderEnddate:
            priorityDict[1]=item
        if item.borrowerStartdate < getDate(item.lenderStartdate,2,True) and item.borrowerEnddate <= getDate(item.lenderEnddate,2,False):
            priorityDict[2]=item
        if item.borrowerStartdate >= item.lenderStartdate and item.borrowerEnddate >= getDate(item.lenderEnddate,2,False):
            priorityDict[3]=item
        if item.borrowerStartdate >= getDate(item.lenderStartdate,2,True) and item.borrowerEnddate > getDate(item.lenderEnddate,2,False):
            priorityDict[4]=item
    sortedDict = sorted(priorityDict.items())
    priorityBasedLenderBorrowers =[]
    for item,value in sortedDict:
        priorityBasedLenderBorrowers.append(value)
    return priorityBasedLenderBorrowers

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
            if bookname:
                book.bookname = bookname
            if authorname:
                book.authorname = authorname
            if year:
                book.year = year
            startDate = getDate(startDate,2,True) 
            endDate = getDate(endDate,2,False) 
            lenderBorrower = LenderBorrower()                   
            lenderBorrowers = lenderBorrower.objects.select_related('book').filter(entry__bookname__contains=bookname,            
            entry__authorname__contains= authorname,entry__year=year,entry__description__contains=description,entry__bookstatus='Available')
            filterData(lenderBorrowers)
        except ValueError as error: 
            print(error)
    

   
