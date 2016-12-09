import mysql.connector  
from flask import Flask

def listCustomers():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    query = ("select * from Customer order by LastName")
    cursor.execute(query)
    
    returnString = []
    returnString = cursor.fetchall()   
    cursor.close()
    cnx.close()
    return returnString

def editCustomer(CustomerID, Fname, Lname, Email, Sex):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    if(CustomerID!="" and Fname!="" and Lname!="" and Email!="" and Sex!=""):
        query = ("Update Customer Set FirstName=%s, LastName=%s, EmailAddress=%s, Sex=%s where idCustomer=%s")
        try:
            data=(Fname, Lname, Email, Sex, CustomerID)
            cursor.execute(query,data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def addCustomer(CustomerID, Fname, Lname, Email, Sex):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    if(CustomerID!="" and Fname!="" and Lname!="" and Email!="" and Sex!=""):
        query = ("Insert into Customer Values (%s, %s, %s, %s, %s)")
        try:
        	data = (CustomerID, Fname, Lname, Email, Sex)
        	cursor.execute(query, data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def deleteCustomer(CustomerID, Fname, Lname, Email, Sex):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    if(CustomerID!="" and Fname!="" and Lname!="" and Email!="" and Sex!=""):
        query = ("Delete from Customer where idCustomer=%s and FirstName=%s and LastName=%s and EmailAddress=%s and Sex=%s")
        try:
            data=(CustomerID, Fname, Lname, Email, Sex)
            cursor.execute(query, data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return