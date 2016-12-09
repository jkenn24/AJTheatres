from flask import Flask, render_template, request, url_for, redirect
import mysql.connector
from Movie import listMovies, editMovie, addMovie, deleteMovie
from User import getUser, signin
from searchMovie import getYear, getGenre, searchMovies
from purchase import purchaseMovie

app = Flask(__name__)

#################################################################################
#																				#
#								Customer Pages									#
#																				#
#################################################################################

@app.route("/")
def index():
	Users = getUser()
	return render_template("signin.html", Users = Users)

@app.route("/index")
def home():
	return render_template("index.html")

@app.route("/loggedIn")
def loggedInHome():
	return render_template("loggedIn.html")

@app.route("/profile")
def profile():
	return render_template("profile.html")

@app.route("/signin", methods="GET")
def signInSubmit():
	idCustomer=request.form['idCustomer']
	UserInfo = signin(idCustomer)
	return render_template("signin.html", UserInfo=UserInfo)

@app.route("/purchase")
def purchaseTicket():
	MovieList = listMovies()
	return render_template("purchase.html",MovieList = MovieList)

@app.route("/searchedShowings")
def searchedShowings():
	Years = getYear()
	Genres = getGenre()
	return render_template("searchedShowings.html", Years = Years, Genres = Genres)

@app.route("/searchedShowingsSubmit", methods=["POST"])
def searchShowingResults():	
	Showings = searchMovies()
	return render_template("searchedShowingsSubmit.html", Showings = Showings)


#################################################################################
#																				#
#								Staff Pages 									#
#																				#
#################################################################################


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


if __name__ == "__main__":
    app.run(host="192.168.33.10", debug=True)