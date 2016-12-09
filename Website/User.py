import mysql.connector
from flask import Flask  

def getUser():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select * from Customer")
	cursor.execute(query)
	Users = cursor.fetchall()
	cursor.close()
	cnx.close()
	return Users

def signin(idCustomer):
	if(idCustomer != 0):
		cnx = mysql.connector.connect(user="root", database='MovieTheatre')
		cursor = cnx.cursor()

		query = ("select * from Customer where idCustomer="+idCustomer)
		cursor.execute(query)
		UserInfo = cursor.fetchall()
		cursor.close()
		cnx.close()
		return UserInfo
	else:
		print("Invalid Character ID")

def getRatings(idCustomer):
	cnx = mysql.connector.connect(user="root", database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select MovieName, Rating from ((Attend inner join Showing on Showing_idShowing=idShowing) inner join Movie on Movie_idMovie=idMovie) where Customer_idCustomer="+idCustomer)
	cursor.execute(query)
	UserInfo = cursor.fetchall()
	cursor.close()
	cnx.close()
	return UserInfo

def getSeenMovies(idCustomer):
	cnx = mysql.connector.connect(user="root", database='MovieTheatre')
	cursor = cnx.cursor()
	#Duplicate MovieNames, need a way to get distinct names as well as their idShowing
	query = ("select MovieName, idShowing from ((Attend inner join Showing on Showing_idShowing=idShowing) inner join Movie on Movie_idMovie=idMovie) where Customer_idCustomer="+idCustomer+" and Rating is NULL")
	cursor.execute(query)
	seenMovies = cursor.fetchall()
	cursor.close()
	cnx.close()
	return seenMovies

def addRatings(idCustomer, idShowing, Rating):
	cnx = mysql.connector.connect(user="root", database='MovieTheatre')
	cursor = cnx.cursor()

	insert_stmt = ("update Attend set Rating="+Rating+" where Customer_idCustomer="+idCustomer+" and Showing_idShowing="+idShowing)
	cursor.execute(insert_stmt)

	cnx.commit()
	cursor.close()
	cnx.close()
	return
