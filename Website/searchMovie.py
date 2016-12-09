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

def searchMovies(MovieName, Genre, StartDate, EndDate, Flag):
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	query1=""
	query2=""
	query3=""
	query4=""
	query5=""
	query0="select MovieName, Genre, ShowingDateTime, TicketPrice, RoomNumber, idShowing as ID, Capacity-(Select count(*) from Attend where Showing_idShowing=ID) as seatsleft from Movie, Genre, Showing, TheatreRoom, Attend where Movie.idMovie=Genre.Movie_idMovie and Genre.Movie_idMovie=Showing.Movie_idMovie and Showing.TheatreRoom_RoomNumber=TheatreRoom.RoomNumber and Attend.Showing_idShowing=Showing.idShowing"
	#"select MovieName, showingDateTime, TheatreRoom_RoomNumber,TicketPrice,Capacity-count(Customer_idCustomer),idShowing as ID from Movie,Showing,Attend, TheatreRoom where MovieName='"+ MovieName+ "' and showingDateTime >'"+StartDate+"'and showingDateTime < '"+EndDate+"'  and Movie.idMovie=Showing.Movie_idMovie and TheatreRoom_RoomNumber=RoomNumber and Showing_idShowing = idShowing "
	
	if Genre is not None and len(Genre) is not 0 and Genre!="":
		query2=" and Genre='"+Genre+"'"
	
	if StartDate is not None and len(StartDate) is not 0 and StartDate!="":
		query3=" and ShowingDateTime>='"+StartDate+"'"
	
	if EndDate is not None and len(EndDate) is not 0 and EndDate!="":
		query4=" and ShowingDateTime<='"+EndDate+"'"
	
	if MovieName is not None and len(MovieName) is not 0 and MovieName!="":
		query5 =" and MovieName like '"+MovieName+"'"
	
	if Flag != None:
		query1=" and (Capacity-(Select count(*) from Attend where Showing_idShowing=idShowing))> 0"
	query= query0+query1+query2+query3+query4+query5
	cursor.execute(query)
	Showings = cursor.fetchall()
	cursor.close()
	cnx.close()
	return Showings

def findMovie(idMovie):
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	if idMovie!="":
		query=("Select * from Movie where idMovie='"+idMovie+"'")
		cursor.execute(query)
		Showings =cursor.fetchall()
	cursor.close()
	cnx.close()
	return Showings


#select MovieName, Genre, ShowingDateTime, TicketPrice, RoomNumber, Capacity-Count(Customer_idCustomer) from Movie, Genre, Showing, TheatreRoom, Attend where Movie.idMovie=Genre.Movie_idMovie and Genre.Movie_idMovie=Showing.Movie_idMovie and Showing.TheatreRoom_RoomNumber=TheatreRoom.RoomNumber and Genre='Drama' and ShowingDateTime>='2016-03-12 19:00:00' and ShowingDateTime<='2016-03-21 19:00:00' and MovieName like %s

#select MovieName, Genre, ShowingDateTime, TicketPrice, RoomNumber, Capacity-Count(Customer_idCustomer) from Movie, Genre, Showing, TheatreRoom, Attend where Movie.idMovie=Genre.Movie_idMovie and Genre.Movie_idMovie=Showing.Movie_idMovie and Showing.TheatreRoom_RoomNumber=TheatreRoom.RoomNumber and Genre='Drama' and ShowingDateTime>='2016-03-12 19:00:00' and ShowingDateTime<='2016-03-21 19:00:00' and MovieName like %s

#(u"select MovieName, Genre, ShowingDateTime, TicketPrice, RoomNumber, Capacity-Count(Customer_idCustomer) from Movie, Genre, Showing, TheatreRoom, Attend where Movie.idMovie=Genre.Movie_idMovie and Genre.Movie_idMovie=Showing.Movie_idMovie and Showing.TheatreRoom_RoomNumber=TheatreRoom.RoomNumber and Genre='Drama' and ShowingDateTime>='2016-03-12 19:00:00' and ShowingDateTime<='2016-03-21 19:00:00' and MovieName like %s", u'Aloha')

#select MovieName, Genre, ShowingDateTime, TicketPrice, RoomNumber, Capacity-Count(Customer_idCustomer) from Movie, Genre, Showing, TheatreRoom, Attend where Movie.idMovie=Genre.Movie_idMovie and Genre.Movie_idMovie=Showing.Movie_idMovie and Showing.TheatreRoom_RoomNumber=TheatreRoom.RoomNumber and Attend.Showing_idShowing=Showing.idShowing group by idShowing

#select MovieName, Genre, ShowingDateTime, TicketPrice, RoomNumber, idShowing as ID, Capacity-(Select count(*) from Attend where Showing_idShowing=ID) as seatsleft from Movie, Genre, Showing, TheatreRoom, Attend where Movie.idMovie=Genre.Movie_idMovie and Genre.Movie_idMovie=Showing.Movie_idMovie and Showing.TheatreRoom_RoomNumber=TheatreRoom.RoomNumber and Attend.Showing_idShowing=Showing.idShowing and (Capacity-(Select count(*) from Attend where Showing_idShowing=ID))> 0
