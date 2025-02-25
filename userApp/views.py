from django.shortcuts import render
from django.http import HttpResponse
from userApp.models import Appuser
from django.db import IntegrityError
from dashboard import views as v

# Create your views here.

def index(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

combinedresult={}

def validate(request): #allows registered user to login by validating
    
    if request.method=='POST':
        global username
        global password
        username = request.POST['username']
        password = request.POST['userPassword']
        users = Appuser.objects.filter(username=username)
        for usr in users:            
            username = usr.username
            if usr.userPassword == password:
                result=v.available(username)
                result1=v.lendable(username)
                result2=v.profile(username)
                result3=v.my_borrow(username)
                global combinedresult
                combinedresult = {
                    "available":result[0],"lendable":result1[0],"available2":result[1],
                    "lendable2":result1[1],
                    "profile":result2,"Username":username,"my_borrow":result3[0],"borrow_number":result3[1]
                    }
                return render(request,'home.html',combinedresult)
            
    elif request.method == 'GET':
        users = Appuser.objects.filter(username=username)
        for usr in users:            
            username = usr.username
            if usr.userPassword == password:
                result=v.available(username)
                result1=v.lendable(username)
                result2=v.profile(username)
                result3=v.my_borrow(username)
                combinedresult = {
                    "available":result[0],"lendable":result1[0],"available2":result[1],
                    "lendable2":result1[1],
                    "profile":result2,"Username":username,"my_borrow":result3[0],"borrow_number":result3[1]
                    } 
                return render(request,'home.html',combinedresult)
        return render(request,'login.html',{'error':'User name or password is wrong'})


def add_user(request): #adds newly registered users into the database
    if request.method=='POST':
        try:
            firstName = request.POST['firstName']            
            lastName = request.POST['lastName']
            age =request.POST['age']
            username =request.POST['username']
            userPassword = request.POST['userPassword']
            cuserPassword = request.POST['cuserPassword']
            address =request.POST['address']
            pincode= request.POST['pincode']
            mobileno =request.POST['mobileno']
            emailid =request.POST['emailid']                
            s = Appuser()
            s.firstName = firstName
            s.lastName =lastName
            s.age = int(age)
            s.username = username
            s.userPassword = userPassword
            s.address = address
            s.pincode = pincode
            s.mobileno = int(mobileno)
            s.emailid = emailid
            if userPassword==cuserPassword:
                s.save(force_insert=True)                
                return render(request,'register.html',{'success':'User saved successfully'})
            else:
                return render(request, 'register.html', {'error':'Passwords did not match'})
        except IntegrityError:
            return render(request, 'register.html', {'error':'That username has already been taken. Please choose a new username'})



    
    


