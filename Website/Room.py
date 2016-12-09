import mysql.connector  
from flask import Flask 

def listRooms():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    query = ("select * from TheatreRoom order by RoomNumber")
    cursor.execute(query)
    
    returnString = []
    returnString = cursor.fetchall()   
    cursor.close()
    cnx.close()
    return returnString

def editRoom(RoomNum, capacity):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    if(RoomNum!="" and capacity!=""):
        query = ("Update TheatreRoom Set Capacity=%s where RoomNumber=%s")
        try:
            data = (capacity, RoomNum)
            cursor.execute(query,data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def addRoom(RoomNum, capacity):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    if(RoomNum!="" and capacity!=""):
        query = ("Insert into TheatreRoom Values (%s, %s)")
        try:
            data = (RoomNum, capacity)
            cursor.execute(query, data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def deleteRoom(RoomNum, capacity):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    if(RoomNum!="" and capacity!=""):
        query = ("Delete from TheatreRoom where RoomNumber=%s and Capacity=%s")
        try:
            data = (RoomNum, capacity)
            cursor.execute(query, data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return