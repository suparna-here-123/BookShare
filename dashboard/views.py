from django.shortcuts import render
from lenderBorrower.models import Book
from django.http import HttpResponse
import mysql.connector as m

# Create your views here.
def available(x):
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            #print('connection to database established')
            #sql1="select username from userapp_appuser u"
            #name=mycursor.execute(sql1)
            sql2 = f"select count(book_id) from book b, userapp_appuser u where b.user_name<>u.username and bookstatus='yes' and u.username='{x}'"
            sql3 = f"select bookname,authorname,user_name,book_id from book b, userapp_appuser u where b.user_name<>u.username and bookstatus='yes' and u.username='{x}'"
            mycursor.execute(sql2)
            result = mycursor.fetchall()
            mycursor.execute(sql3)
            result2 = mycursor.fetchall()
            d2=result2
            print("list",d2)
            d=result[0][0]
            print("Available books",d)
            return d,d2
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()
result2=0
def lendable(x):
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
            print(result2)
            
            d1=result[0][0]
            print("lendable books",d1)
            return d1,result2
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()
def profile(x):
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
def getBorrowdetails(x):
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

def lenderemailid(x):
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql3 = f"select user_name from book b where b.book_id={x}"
            mycursor.execute(sql3)
            result2 = mycursor.fetchall()
            for i in result2:
                l_user=i[0]
                sql4=f"select emailid from userapp_appuser where username='{l_user}'" #getting emailid of lender
                mycursor.execute(sql4)
                result3 = mycursor.fetchall()
            #email_d={"email":result3[0][0]}
            return result3[0][0]
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()
        
def delete(x):
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

def my_borrow(x):
    try:
        con = m.connect(host='localhost',user='admin', passwd='password',db='bookshare')
        if con.is_connected():
            mycursor = con.cursor()
            sql4 = f"select bookname,authorname,book_id,user_name,borrower from book where borrower='{x}'"
            mycursor.execute(sql4)
            result4 = mycursor.fetchall()
            return result4
        else:
            print('connection to database not established')
    except m.Error as e:
            print(e)
    else:
        con.close()

def ret_but(x):
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

    

    
    



    
    



        


