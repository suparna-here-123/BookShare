from django.shortcuts import render
from lenderBorrower.models import Book
from django.http import HttpResponse
import mysql.connector as m

# Create your views here.

def available(x): #to get available books
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql2 = f"select count(book_id) from book b, userapp_appuser u where b.user_name<>u.username and bookstatus='yes' and u.username='{x}'"
            sql3 = f"select bookname,authorname,user_name,book_id from book b, userapp_appuser u where b.user_name<>u.username and bookstatus='yes' and u.username='{x}'"
            mycursor.execute(sql2)
            result = mycursor.fetchall()
            mycursor.execute(sql3)
            result2 = mycursor.fetchall()
            d2=result2
            d=result[0][0]
            return d,d2
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()
        
result2=0
def lendable(x): #to get the books the user can lend
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql2 = f"select  count(book_id) from book b, userapp_appuser u where u.username=b.user_name and u.username='{x}'"            
            mycursor.execute(sql2)
            result = mycursor.fetchall()
            sql3 = f"select bookname,authorname,book_id from book b, userapp_appuser u where u.username=b.user_name and u.username='{x}'"
            mycursor.execute(sql3)
            global result2
            result2 = mycursor.fetchall()
            d1=result[0][0]
            return d1,result2
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()
        
def profile(x): #to get the details of the user
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql3 = f"select * from userapp_appuser u where u.username='{x}'"
            mycursor.execute(sql3)
            result2 = mycursor.fetchall()
            return result2
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()
        
def getBorrowdetails(x): #to display the details of the book
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql3 = f"select * from book b where b.book_id={x}"
            mycursor.execute(sql3)
            result2 = mycursor.fetchall()
            result3={"borrowdetails":result2}
            return result3
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()

def lenderemailid(x): #getting emailid of lender
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql3 = f"select user_name from book b where b.book_id={x}"
            mycursor.execute(sql3)
            result2 = mycursor.fetchall()
            for i in result2:
                l_user=i[0]
                sql4=f"select emailid from userapp_appuser where username='{l_user}'" 
                mycursor.execute(sql4)
                result3 = mycursor.fetchall()
            return result3[0][0]
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()
        
def delete(x): #remove a book the lender no longer wishes to lend
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql3 = f"delete from book where book_id={x}"
            mycursor.execute(sql3)
            con.commit()
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()

def my_borrow(x): #to display the books the user has borrowed
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql4 = f"select bookname,authorname,book_id,user_name,borrower from book where borrower='{x}'"
            mycursor.execute(sql4)
            result4 = mycursor.fetchall()
            sql5 = f"select count(book_id) from book where borrower='{x}'"
            mycursor.execute(sql5)
            result5 = mycursor.fetchall()
            return result4,result5[0][0]
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()

def ret_but(x): #Enables the borrower to indicate his/her desire to return borrowed books
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql3 = f"update book set bookstatus='yes',borrower=null where book_id={x}"
            mycursor.execute(sql3)
            con.commit()
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()

    

    
    



    
    



        


