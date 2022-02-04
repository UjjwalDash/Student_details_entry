from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# Create your views here.

def home(request):
    return render(request,'index.html')
def save(request):
    resistration_id=str(request.GET['resistration_id'])
    first_name=str(request.GET['first_name'])
    last_name=str(request.GET['last_name'])
    mail_id=str(request.GET['email'])
    department=str(request.GET['department'])
    phone_no=str(request.GET['phone_no'])
    connection=sqlite3.connect('db.sqlite3')
    #print("INSERT INTO Student VALUES ('%s','%s','%s','%s','%s','%s')"%(resistration_id,first_name,last_name,mail_id,department,phone_no))
    cr=connection.cursor()
    cr.execute("CREATE TABLE IF NOT EXISTS Student(Resistration_id TEXT,First_name TEXT,Last_name TEXT,Mail_id TEXT,Department TEXT,Phone_no TEXT)")
    cr.execute("INSERT INTO Student VALUES ('%s','%s','%s','%s','%s','%s')"%(resistration_id,first_name,last_name,mail_id,department,phone_no))
    connection.commit()
    connection.close()
    return render(request,'sumit.html',{'resistration_id':resistration_id,
    'first_name':first_name,
    'last_name':last_name,
    'mail_id':mail_id,
    'department':department,
    'phone_no':phone_no
    })