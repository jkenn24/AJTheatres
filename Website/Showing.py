import mysql.connector  
from flask import Flask  

def listShowings():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    query = ("select * from Showing order by ShowingDateTime")
    cursor.execute(query)
    
    returnString = []
    returnString = cursor.fetchall()   
    cursor.close()
    cnx.close()
    return returnString

def editShowing(ShowID, ShowDate, MovieID, RoomNum, Price):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    

    if(ShowID!="" and ShowDate!="" and MovieID!="" and RoomNum!="" and Price!=""):
        query = ("Update Showing Set ShowingDateTime=%s, Movie_idMovie=%s, TheatreRoom_RoomNumber=%s, TicketPrice=%s where idShowing=%s")
        try:
            data=(ShowDate, MovieID, RoomNum, Price, ShowID)
            cursor.execute(query,data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def addShowing(ShowID, ShowDate, MovieID, RoomNum, Price):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    if(ShowID!="" and ShowDate!="" and MovieID!="" and RoomNum!="" and Price!=""):
        query = ("Insert into Showing Values (%s, %s, %s, %s, %s)")
        try:
            data = (ShowID, ShowDate, MovieID, RoomNum, Price)
            cursor.execute(query, data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def deleteShowing(ShowID, ShowDate, MovieID, RoomNum, Price):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    if(ShowDate=="" or ShowDate=="None"):
        ShowDate = "0000-00-00 00:00:00"
    if(ShowID!="" and MovieID!="" and RoomNum!="" and Price!=""):
        query = ("Delete from Showing where idShowing=%s and ShowingDateTime=%s and Movie_idMovie=%s and TheatreRoom_RoomNumber=%s and TicketPrice=%s")
        try:
            data=(ShowID, ShowDate, MovieID, RoomNum, Price)
            cursor.execute(query, data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return