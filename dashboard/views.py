from django.shortcuts import render
from lenderBorrower.models import Book
from django.http import HttpResponse
import mysql.connector as m

# Create your views here.
def available():
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            #print('connection to database established')
            #sql1="select username from userapp_appuser u"
            #name=mycursor.execute(sql1)
            sql2 = "select count(book_id) from book b, userapp_appuser u where b.user_name<>u.username and bookstatus='yes' and u.username='sujitha'"
            mycursor.execute(sql2)
            result = mycursor.fetchall()
            print("Available books",result)
            return render(request,'home.html',result)
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()

