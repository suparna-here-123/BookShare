from django.core.checks.messages import Error
from django.shortcuts import render
from django.http import HttpResponse
from lenderBorrower.models import Book
from datetime import datetime
from datetime import timedelta
from .models import Book


# Create your views here.


def display(request):
    
    lb=Book.objects.all()
    print("data",lb)
    return render(request,'lender2.html',{'books':lb})
    
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[{'author':'Nithika B',
'title':'Post',
'content':'hello',
'date_posted': '2000'},
    {'author':'Nith',
'title':'Post',
'content':'hello',
'date_posted': '6000'}
]
def lender2(request):
    
    lb=Book.objects.all()
    context={
      'posts':lb
    }
    return render(request,'lender2.html',context)
def borrower(request):
    lb=Book.objects.all()
    context={
      'posts':lb
    }
    return render(request,'borrower.html',context)
def lend(request):
    return render(request,'lend.html')
def add_book(request):
    if request.method=='POST':
        try:
            bookname = request.POST['bookname']            
            authorname = request.POST['authorname']
            genre =request.POST['genre']
            bookcondition =request.POST['bookcondition']
            description = request.POST['description']
            bookphoto = request.POST['bookphoto']
            s = Book()
            s.bookname = bookname
            s.authorname = authorname 
            s.genre = genre
            s.bookcondition = bookcondition
            s.description  = description 
            s.bookphoto = bookphoto
            s.save(force_insert=True)                
            return render(request,'lend.html',{'success':'details saved successfully'})
        except IntegrityError:
            return render(request, 'lend.html', {'error':'That username has already been taken. Please choose a new username'})


   
