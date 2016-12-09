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
