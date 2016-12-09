import mysql.connector
from flask import Flask  

def availableMovies():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	#query = ("select MovieName,ShowingDateTime,idShowing, RoomNumber from Showing, Movie, TheatreRoom where Movie_idMovie=idMovie and TheatreRoom_RoomNumber=RoomNumber order by ShowingDateTime")

	query = ("select MovieName,ShowingDateTime,idShowing, RoomNumber from ((Showing inner join Movie on Movie_idMovie=idMovie) inner join TheatreRoom on TheatreRoom_RoomNumber=RoomNumber) order by ShowingDateTime")

	cursor.execute(query)

	availableMovies = cursor.fetchall()  
	cursor.close()
	cnx.close()
	return availableMovies

def purchaseMovie(idCustomer, idShowing):
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	insert_stmt = ("insert into Attend (Customer_idCustomer, Showing_idShowing) values("+idCustomer+","+idShowing+")")
	cursor.execute(insert_stmt)
    
	cnx.commit()
	cnx.close()
	return
