import mysql.connector  
from flask import Flask

def getYear():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select DISTINCT ShowingDateTime from Showing order by ShowingDateTime")
	cursor.execute(query)
	Years = cursor.fetchall()
	cursor.close()
	cnx.close()
	return Years

def getGenre():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select DISTINCT Genre from Genre order by Genre")
	cursor.execute(query)
	Genres = cursor.fetchall()
	cursor.close()
	cnx.close()
	return Genres

def searchMovies():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	MovieName= request.form['MovieName']
	Genre=request.form.get('Genre')
	StartDate=request.form.get('StartDate')
	EndDate=request.form.get('EndDate')

	if MovieName is not None and len(MovieName) is not 0:
		query=("select MovieName, showingDateTime, TheatreRoom_RoomNumber,TicketPrice,Capacity-count(Customer_idCustomer) from Movie,Showing,Attend, TheatreRoom where MovieName='"+ MovieName+ "' and showingDateTime >'"+StartDate+"'and showingDateTime < '"+EndDate+"'  and Movie.idMovie=Showing.Movie_idMovie and TheatreRoom_RoomNumber=RoomNumber and Showing_idShowing = idShowing ")

	else: 
		query=("select MovieName,ShowingDateTime, RoomNumber, TicketPrice  from Movie, TheatreRoom, Showing, Genre where Movie.idMovie=Genre.Movie_idMovie and Showing.TheatreRoom_RoomNumber = TheatreRoom.RoomNumber and Showing.Movie_idMovie=Movie.idMovie and Genre='"+GenreSelect+"'")

	cursor.execute(query)
	Showings =cursor.fetchall()

	cnx.close()
	return Showings