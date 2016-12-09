import mysql.connector
from flask import Flask 

def listGenres():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    query = ("select Genre, MovieName from Movie inner join Genre on Genre.Movie_idMovie=Movie.idMovie order by Genre")
    cursor.execute(query)
    
    returnString = []
    returnString = cursor.fetchall()   
    cursor.close()
    cnx.close()
    return returnString

def addGenre(ID,Genre):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    if (ID != "" and Genre != ""):
        query = ("Insert into Genre Values (%s, %s)")
        try:
        	data = (Genre,ID)
        	cursor.execute(query, data)
        except:
        	print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return

def deleteGenre(ID,Genre):
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    if (ID != "" and Genre != ""):
        query = ("Delete from Genre where Movie_idMovie=%s and Genre=%s")
        data=(ID,Genre)
        try:
            cursor.execute(query,data)
        except:
            print ("Invalid Query")
    cnx.commit()
    cursor.close()
    cnx.close()
    return