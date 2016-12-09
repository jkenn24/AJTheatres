from flask import Flask, render_template, request, url_for, redirect, session
import mysql.connector
from Movie import listMovies, editMovie, addMovie, deleteMovie
from Genre import listGenres, addGenre, deleteGenre
from Room import listRooms, editRoom, addRoom, deleteRoom
from Showing import listShowings, editShowing, addShowing, deleteShowing
from Customer import listCustomers, editCustomer, addCustomer, deleteCustomer
from Attendance import listAttendance
from User import getUser, signin, getRatings, getSeenMovies, addRatings
from searchMovie import getYear, getGenre, searchMovies, findMovie
from purchase import availableMovies, purchaseMovie

app = Flask(__name__)

app.secret_key = 'super secret key'

@app.route("/signin", methods={'GET','POST'})
def index():
	Users = getUser()
	#if request.method == "POST":
		#print("hi")
		#select = request.form.get('comp_select')
		#print(select)
		#return redirect("/loggedIn", ID=select)
	return render_template("signin.html", Users = Users)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/loggedIn", methods={'GET','POST'})
def loggedInHome():
	if request.method == "POST":
		CustID = request.form.get('comp_select')
		session['CustID'] = CustID
	return render_template("loggedIn.html")

@app.route("/profile", methods={'GET','POST'})
def profile():
	CustID = session.get('CustID',None)
	if request.method == "POST":
		MovieShowing = request.form.get('ratingMovie')
		print(MovieShowing)
		Rating = request.form.get('giveRating')
		addRatings(CustID, MovieShowing, Rating)
	Customer = signin(CustID)
	Ratings = getRatings(CustID)
	seenMovies = getSeenMovies(CustID)
	return render_template("profile.html", Customer=Customer, Ratings=Ratings, seenMovies = seenMovies)

@app.route("/purchase", methods={'GET', 'POST'})
def purchaseTicket():
	if request.method == "POST":
		CustID = session.get('CustID',None)
		ShowingID = request.form.get('selectMovie')
		try:
			purchaseMovie(CustID, ShowingID)
		except:
			print("Invalid Option")
	MovieList = availableMovies()
	return render_template("purchase.html",MovieList = MovieList)

@app.route("/searchedShowings", methods={'GET', 'POST'})
def searchedShowings():
	Years = getYear()
	Genres = getGenre()
	return render_template("searchedShowings.html", Years = Years, Genres = Genres)

@app.route("/searchedShowingsSubmit", methods={'GET', 'POST'})
def searchShowingResults():
	print("1")
	if request.method == "POST":
		print("2")
		MovieName= request.form['MovieTitle']
		print(MovieName)
		Genre=request.form.get('Genre')
		print(Genre)
		StartDate=request.form.get('StartDate')
		print(StartDate)
		EndDate=request.form.get('EndDate')
		print(EndDate)
		Flag=request.form.get('seatsAvailable')
		print(Flag)
		Showings = searchMovies(MovieName, Genre, StartDate, EndDate, Flag)
		return render_template("searchedShowingsSubmit.html", Showings = Showings)
	return render_template("searchedShowingsSubmit.html")



#################################################################################
#																				#
#								Staff Pages 									#
#																				#
#################################################################################


@app.route("/StaffIndex")
def StaffHomePage():
	Years = getYear()
	Genres = getGenre()
	return render_template("StaffIndex.html", Years = Years, Genres = Genres)



@app.route("/StaffMovie", methods={'GET','POST'})
def MoviePage():
	if request.method == "POST":
		if "edit" in request.form:
			oldID = request.form['editCurrentMovieID']
			newTitle = request.form['editNewMovieTitle']
			newYear = request.form['editNewMovieYear']
			editMovie(oldID,newTitle,newYear)
		elif "add" in request.form:
			newID = request.form['addNewMovieID']
			newTitle = request.form['addNewMovieTitle']
			newYear = request.form['addNewMovieYear']
			addMovie(newID,newTitle,newYear)
		elif "delete" in request.form:
			ID = request.form['deleteMovieID']
			Title = request.form['deleteMovieTitle']
			Year = request.form['deleteMovieYear']
			deleteMovie(ID,Title,Year)
	MovieList = listMovies()
	return render_template("StaffMovie.html", MovieList = MovieList)


@app.route("/StaffGenre", methods={'GET','POST'})
def GenrePage():
	if request.method == "POST":
		if "add" in request.form:
			ID = request.form['addGenreID']
			Genre = request.form['addGenreName']
			addGenre(ID,Genre)
		elif "delete" in request.form:
			ID = request.form['deleteGenreID']
			Genre = request.form['deleteGenreName']
			deleteGenre(ID,Genre)
	GenreList=listGenres()
	return render_template("StaffGenre.html", GenreList=GenreList)

@app.route("/StaffRoom", methods={'GET','POST'})
def RoomPage():
	if request.method == "POST":
		if "edit" in request.form:
			RoomNum = request.form['editRoomNum']
			capacity = request.form['editRoomCapacity']
			editRoom(RoomNum,capacity)
		elif "add" in request.form:
			RoomNum = request.form['addRoomNum']
			capacity = request.form['addRoomCapacity']
			addRoom(RoomNum,capacity)
		elif "delete" in request.form:
			RoomNum = request.form['deleteRoomNum']
			capacity = request.form['deleteRoomCapacity']
			deleteRoom(RoomNum,capacity)
	RoomList=listRooms()
	return render_template("StaffRoom.html", RoomList=RoomList)

@app.route("/StaffShowing", methods={'GET','POST'})
def ShowingPage():
	if request.method == "POST":
		if "edit" in request.form:
			ShowID = request.form['editShowingID']
			ShowDate = request.form['editShowingDate']
			MovieID = request.form['editShowingMovieID']
			RoomNum = request.form['editShowingRoom']
			Price = request.form['editShowingPrice']
			editShowing(ShowID, ShowDate, MovieID, RoomNum, Price)
		elif "add" in request.form:
			ShowID = request.form['addShowingID']
			ShowDate = request.form['addShowingDate']
			MovieID = request.form['addShowingMovieID']
			RoomNum = request.form['addShowingRoom']
			Price = request.form['addShowingPrice']
			addShowing(ShowID, ShowDate, MovieID, RoomNum, Price)
		elif "delete" in request.form:
			ShowID = request.form['deleteShowingID']
			ShowDate = request.form['deleteShowingDate']
			MovieID = request.form['deleteShowingMovieID']
			RoomNum = request.form['deleteShowingRoom']
			Price = request.form['deleteShowingPrice']
			deleteShowing(ShowID, ShowDate, MovieID, RoomNum, Price)
	ShowingList=listShowings()
	return render_template("StaffShowing.html", ShowingList=ShowingList)

@app.route("/StaffCustomer", methods={'GET','POST'})
def CustomerPage():
	if request.method == "POST":
		if "edit" in request.form:
			CustomerID = request.form['editCustomerID']
			Fname = request.form['editCustomerFName']
			Lname = request.form['editCustomerLName']
			Email = request.form['editCustomerEmail']
			Sex = request.form['editCustomerSex']
			editCustomer(CustomerID, Fname, Lname, Email, Sex)
		elif "add" in request.form:
			CustomerID = request.form['addCustomerID']
			Fname = request.form['addCustomerFName']
			Lname = request.form['addCustomerLName']
			Email = request.form['addCustomerEmail']
			Sex = request.form['addCustomerSex']
			addCustomer(CustomerID, Fname, Lname, Email, Sex)
		elif "delete" in request.form:
			CustomerID = request.form['deleteCustomerID']
			Fname = request.form['deleteCustomerFName']
			Lname = request.form['deleteCustomerLName']
			Email = request.form['deleteCustomerEmail']
			Sex = request.form['deleteCustomerSex']
			deleteCustomer(CustomerID, Fname, Lname, Email, Sex)
	CustomerList=listCustomers()
	return render_template("StaffCustomer.html", CustomerList=CustomerList)

@app.route("/StaffAttendance", methods={'GET','POST'})
def AttendancePage():
	AttendanceList=listAttendance()
	return render_template("StaffAttendance.html", AttendanceList=AttendanceList)

#################################################################################
#																				#
#								SQL Injection Page								#
#																				#
#################################################################################


@app.route("/sqlInjection", methods=['GET','POST'])
def injection():
	MovieList = [""]
	if request.method=="POST":
		ID = request.form['searchMovieID']
		MovieList = findMovie(ID)
	return render_template("sqlInjection.html", MovieList=MovieList)

if __name__ == "__main__":
    app.run(host="192.168.33.10", debug=True)