import mysql.connector  
from flask import Flask 

def listAttendance():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    query = ("select idCustomer, FirstName, LastName, idShowing, ShowingDateTime, idMovie, MovieName, Rating from (((Attend inner join Customer on Customer_idCustomer=idCustomer) inner join Showing on Showing_idShowing=idShowing) inner join Movie on Movie_idMovie=idMovie) order by Rating")
    cursor.execute(query)
    
    returnString = []
    returnString = cursor.fetchall()   
    cursor.close()
    cnx.close()
    return returnString