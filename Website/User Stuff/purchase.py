import mysql.connector
from flask import Flask  

def purchaseMovie():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select MovieTitle, ShowingDateTime, TheatreRoom_RoomNumber from Movie, Showing, TheatreRoom where Movie.idMovie = Showing.Movie_idMovie, Showing.TheatreRoom_RoomNumber = TheatreRoom.RoomNumber order by MovieName")
	cursor.execute(query)

	returnString = []
	#for i in cursor:
	#    returnString.append(i)
	returnString = cursor.fetchall()   
	cursor.close()
	cnx.close()
	return returnString