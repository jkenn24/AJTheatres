import mysql.connector  
from flask import Flask  

def listMovies():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    query = ("select * from Movie order by MovieName")
    cursor.execute(query)
    
    returnString = []
    #for i in cursor:
    #    returnString.append(i)
    returnString = cursor.fetchall()   
    cursor.close()
    cnx.close()
    return returnString

def editMovie(oldID, newTitle, newYear):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    if (oldID != ""):
        data=None
        if(newTitle!="" and newYear!=""):
            query = ("Update Movie Set MovieName=%s, MovieYear=%s where idMovie=%s")
            data=(newTitle,newYear,oldID)
        elif(newTitle=="" and newYear!=""):
            query = ("Update Movie Set MovieYear=%s where idMovie=%s")
            data=(newYear,oldID)
        elif(newTitle!="" and newYear==""):
            query = ("Update Movie Set MovieName= %s where idMovie=%s")
            data=(newTitle,oldID)
        try:
            cursor.execute(query,data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def addMovie(newID,newTitle,newYear):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    if (newID != "" and newTitle != "" and newYear != ""):
        query = ("Insert into Movie Values (%s, %s, %s)")
        try:
            data = (newID,newTitle,newYear)
            cursor.execute(query, data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def deleteMovie(ID,Title,Year):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    if (ID != "" and Title != "" and Year != ""):
        query = ("Delete from Movie where idMovie=%s and MovieName=%s and MovieYear=%s")
        data=(ID,Title,Year)
        try:
            cursor.execute(query,data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return
